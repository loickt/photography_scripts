import os
import shutil
import sys

def copy_files(src_folder, dest_folder, exclude_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Get a list of files in the source folder
    src_files = os.listdir(src_folder)

    # Get a list of files in the exclude folder
    exclude_files = set(os.listdir(exclude_folder))

    # Copy files from the source folder to the destination folder
    for file_name in src_files:
        src_file_path = os.path.join(src_folder, file_name)
        dest_file_path = os.path.join(dest_folder, file_name)

        # Check if the file is not in the exclude folder
        if file_name not in exclude_files:
            shutil.copy(src_file_path, dest_file_path)
            print(f"Copied: {file_name}")

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py source_folder dest_folder exclude_folder")
        sys.exit(1)

    source_folder = sys.argv[1]
    dest_folder = sys.argv[2]
    exclude_folder = sys.argv[3]

    if not os.path.exists(source_folder) or not os.path.exists(exclude_folder):
        print("Source folder or exclude folder does not exist.")
        sys.exit(1)

    copy_files(source_folder, dest_folder, exclude_folder)
    os.startfile(dest_folder)
