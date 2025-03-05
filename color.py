import cv2
import numpy as np
import random

def apply_random_color_on_black(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Check if the image has an alpha channel
    has_alpha = image.shape[-1] == 4

    # Create a mask for the black parts (assuming RGB(0, 0, 0))
    if has_alpha:
        bgr_image = image[:, :, :3]
    else:
        bgr_image = image

    # Create a mask for black areas (tolerance for near-black values can be adjusted)
    mask = cv2.inRange(bgr_image, (0, 0, 0), (20, 20, 20))

    # Create random color background
    random_color = [random.randint(0, 255) for _ in range(3)]

    # Create a color image of the same size
    background = np.full_like(bgr_image, random_color, dtype=np.uint8)

    # Blend the original image with the random background on black parts
    colored_image = cv2.bitwise_and(bgr_image, bgr_image, mask=cv2.bitwise_not(mask))
    background_on_black = cv2.bitwise_and(background, background, mask=mask)
    result = cv2.add(colored_image, background_on_black)

    # If the original image had alpha, preserve it
    if has_alpha:
        result = np.dstack((result, image[:, :, 3]))

    # Save the result
    cv2.imwrite(output_path, result)

# Example usage
apply_random_color_on_black("/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/images/train/eight/rf52b6f29-45cd-4483-bd7a-34309d7bea59.rgb_0000augmented_6513024.png", "output_image.jpg")