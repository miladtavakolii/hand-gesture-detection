import cv2
import mediapipe as mp
import os

# Initialize MediaPipe hand detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.2, min_tracking_confidence=0.2)
mp_drawing = mp.solutions.drawing_utils
folder = '/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/images/val/8'
folder1 = '/run/media/milad/Local Disk/Downloads/Compressed/hagridv2_512/2/images/val/81'

for filename in os.listdir(folder):
    # Load the image
    image_path = os.path.join(folder,filename)
    print(image_path)
    image = cv2.imread(image_path)

    # Convert the image to RGB (MediaPipe works with RGB images)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and get the hand landmarks
    results = hands.process(image_rgb)
    annotations = []

    # If hands are detected, draw bounding boxes and generate COCO labels
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the hand's bounding box coordinates (from min/max x, y values of landmarks)
            x_min = min([landmark.x for landmark in hand_landmarks.landmark]) - 0.03
            x_max = max([landmark.x for landmark in hand_landmarks.landmark]) + 0.03
            y_min = min([landmark.y for landmark in hand_landmarks.landmark]) - 0.03
            y_max = max([landmark.y for landmark in hand_landmarks.landmark]) + 0.03
            w = x_max - x_min
            h = y_max - y_min
            x_mid = (x_min + x_max) / 2
            y_mid = (y_min + y_max) / 2
            print(x_mid)
        filename = filename[:-3] + 'txt'
        file_path = os.path.join(folder1,filename)
        newline = f'8 {x_mid} {y_mid} {w} {h}'
        with open(file_path, "w") as file:
            file.writelines(newline)