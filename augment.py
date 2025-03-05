import cv2
import os
import random
import numpy as np
import shutil

def colorjitter(img, cj_type="b"):
    if cj_type == "b":
        value = np.random.choice(np.array([-50, -40, -30, 30, 40, 50]))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        if value >= 0:
            lim = 255 - value
            v[v > lim] = 255
            v[v <= lim] += value
        else:
            lim = np.absolute(value)
            v[v < lim] = 0
            v[v >= lim] -= np.absolute(value)

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    elif cj_type == "s":
        value = np.random.choice(np.array([-50, -40, -30, 30, 40, 50]))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        if value >= 0:
            lim = 255 - value
            s[s > lim] = 255
            s[s <= lim] += value
        else:
            lim = np.absolute(value)
            s[s < lim] = 0
            s[s >= lim] -= np.absolute(value)

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    elif cj_type == "c":
        brightness = 10
        contrast = random.randint(40, 100)
        dummy = np.int16(img)
        dummy = dummy * (contrast/127+1) - contrast + brightness
        dummy = np.clip(dummy, 0, 255)
        img = np.uint8(dummy)
        return img

def noisy(img, noise_type="gauss"):
     if noise_type == "gauss":
        image=img.copy() 
        mean=0
        st=0.7
        gauss = np.random.normal(mean,st,image.shape)
        gauss = gauss.astype('uint8')
        image = cv2.add(image,gauss)
        return image
    
     elif noise_type == "sp":
        image=img.copy() 
        prob = 0.05
        
        if len(image.shape) == 2:
            black = 0
            white = 255            
        else:
            colorspace = image.shape[2]
            if colorspace == 3:  # RGB
                black = np.array([0, 0, 0], dtype='uint8')
                white = np.array([255, 255, 255], dtype='uint8')
            else:  # RGBA
                black = np.array([0, 0, 0, 255], dtype='uint8')
                white = np.array([255, 255, 255, 255], dtype='uint8')
        probs = np.random.random(image.shape[:2])
        image[probs < (prob / 2)] = black
        image[probs > 1 - (prob / 2)] = white
        return image
     
def zoom_out(original_image):
    # Load the original image
    original_height, original_width = original_image.shape[:2]


    # Zoom-out scale factor (greater than 1)
    scale_factor = random.uniform(1.0,2.5)

    # Calculate new dimensions for zoomed-out image
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    # Create a blank canvas with new dimensions
    canvas = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Place the original image at a random position on the canvas
    x_offset = random.randint(0, new_width - original_width)
    y_offset = random.randint(0, new_height - original_height)
    canvas[y_offset:y_offset + original_height, x_offset:x_offset + original_width] = original_image


    return canvas

def augment_image_with_label(image_path, label_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found: {image_path}")
    random_name = f"augmented_{random.randint(1000000, 9999999)}"
    new_image_path = os.path.join(image_path[:-4] + f"{random_name}.png")

    new_label_path = os.path.join(label_path[:-4] + f"{random_name}.txt")

    try:
        with open(label_path, 'r') as label_file:
            label_content = label_file.read()
        with open(new_label_path, 'w') as new_label_file:
            new_label_file.write(label_content)
    except OSError as e:
        print()

    # Apply augmentation
    augmented_img = noisy(img, noise_type=np.random.choice(['sp','gauss']))

    # Generate a random name for the new image and label

    # Save the augmented image
    cv2.imwrite(new_image_path, augmented_img)

    print(f"Augmented image saved: {new_image_path}")
    print(f"Augmented label saved: {new_label_path}")

# Example usage
image_path = "/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/images/train/eight"  # Replace with your image path
label_path = "/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/labels/train/eight"  # Replace with your label path
for filename in os.listdir(image_path):
    augment_image_with_label(os.path.join(image_path,filename), os.path.join(label_path,filename[:-3]+'txt'))