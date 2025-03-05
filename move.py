import os
import shutil

def move_first_1000_images(source_folder, destination_folder):
    # Ensure destination folder exists, if not, create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List all files in the source folder
    all_files = os.listdir(source_folder)
    all_files.sort()
        
    # Select the first 1000 image files
    files_to_move = all_files[:1000]

    # Move the files to the destination folder
    for file in files_to_move:
        src_path = os.path.join(source_folder, file)
        dest_path = os.path.join(destination_folder, file)
        shutil.move(src_path, dest_path)
        print(f'Moved: {file}')

source_folder = '/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/3/test' + '/call'  # Replace with the path to your source folder
destination_folder = '/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/images/train/'+'call'  # Replace with the path to the "val" folder
move_first_1000_images(source_folder, destination_folder)

source_folder = '/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/3/test_labels/call'  # Replace with the path to your source folder
destination_folder = '/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/labels/train/'+'call'  # Replace with the path to the "val" folder
move_first_1000_images(source_folder, destination_folder)