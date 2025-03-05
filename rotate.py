import os
from PIL import Image
import random


def rotate_images_in_folder(input_folder, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):  # Supported formats
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            rotation_angle = 90
            try:
                with Image.open(input_path) as img:
                    rotated_img = img.rotate(rotation_angle, expand=True)
                    rotated_img.save(output_path)
                    print(f"Rotated and saved: {output_path}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

input_folder = "/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/images/val/call"  # Replace with your input folder path
output_folder = "/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/images/val/call2"  # Replace with your output folder path
rotate_images_in_folder(input_folder, output_folder)
