import os
import re
from datetime import datetime, timedelta
from PIL import Image

#todo : 
# print at the end how many files to rename manually
# beeing able to ad phone pictures after having renamed previous phone pictures


def get_image_date(file_path):
    try:
        with Image.open(file_path) as img:
            # Extract the date from the image metadata (EXIF data)
            exif_info = img._getexif()
            if exif_info:
                date_taken = exif_info.get(0x9003)  # 0x9003 is the tag for DateTimeOriginal
                if date_taken:
                    return datetime.strptime(date_taken, "%Y:%m:%d %H:%M:%S")
    except (IOError, AttributeError, KeyError):
        pass

    return None

def get_files_with_incorrect_date(folder_path):
    incorrect_date_pattern = re.compile(r'(\d{8}_\d{6})\S*')
    files_with_incorrect_date = []
    files_to_keep_non_changed = []
    for filename in os.listdir(folder_path):
        match = incorrect_date_pattern.search(filename)
        if match:
            files_with_incorrect_date.append((filename, match.group(1)))
        else:
            files_to_keep_non_changed.append(filename)
    return files_with_incorrect_date,files_to_keep_non_changed

def get_file_dates(folder_path,files_to_keep_non_changed):
    file_dates = []
    for filename in files_to_keep_non_changed:
        file_path = os.path.join(folder_path, filename)
        image_date = get_image_date(file_path)

        if image_date:
            file_dates.append(image_date)

    return file_dates

def get_closest_valid_date(current_date_str,folder_path, files_to_keep_non_changed):
    current_date = datetime.strptime(current_date_str, "%Y%m%d_%H%M%S")
    image_dates = get_file_dates(folder_path,files_to_keep_non_changed)
    if not image_dates:
        return None
    closest_valid_date, is_before = min([(date, date > current_date) for date in image_dates], key=lambda x: abs(x[0] - current_date))
    closest_valid_date_filename = next(filename for filename in files_to_keep_non_changed if get_image_date(os.path.join(folder_path, filename)) == closest_valid_date)
    if is_before:
        picture_number =  int(closest_valid_date_filename[-8:-4])
        closest_valid_date_filename=closest_valid_date_filename[:-8]+str(picture_number-1)+closest_valid_date_filename[-4:]
    
    
    return closest_valid_date_filename


def rename_files(folder_path):
    files_with_incorrect_date,files_to_keep_non_changed = get_files_with_incorrect_date(folder_path)
    
    for filename, incorrect_date in files_with_incorrect_date:
        closest_valid_date_filename = get_closest_valid_date(incorrect_date,folder_path,files_to_keep_non_changed)

        new_filename = f"{closest_valid_date_filename[:-4]}_phone_{len([f for f in os.listdir(folder_path) if closest_valid_date_filename[:-4] in f]) + 1}{filename[-4:]}"

        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    print(str(len(files_with_incorrect_date))+" file"+"s"*(len(files_with_incorrect_date)>1)+ " renamed")

if __name__ == "__main__":
    print("Paste folder path :")
    folder_path= input()
    rename_files(folder_path)
