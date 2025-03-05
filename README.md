# Real-Time Hand Gesture Recognition using YOLOv10

## Overview
This project focuses on developing an advanced object detection model capable of recognizing 15 distinct hand gestures. The model has been trained and optimized to deliver high accuracy and real-time performance, making it suitable for various applications such as sign language interpretation, human-computer interaction, and gesture-based control systems. We have also included sample images to demonstrate the model’s capabilities.

![image](https://github.com/user-attachments/assets/5cea56f0-9db0-4f9b-b1fe-f8f8c1ba109b)

## Features
- **High Accuracy:**
  - **Precision:** 94.5%
  - **Recall:** 95.6%
  - **mAP@50:** 97%
  - **mAP@50-95:** 82.7%
- **Real-Time Performance:** Optimized for fast inference with minimal latency
- **Robust Training:** Fine-tuned on diverse datasets for better generalization

  
![confusion_matrix_normalized](https://github.com/user-attachments/assets/85aa3f2e-5a48-4b1a-9c14-d38d7ce103ea)
![val_batch2_labels](https://github.com/user-attachments/assets/9541bcf4-9cd7-4343-a70c-c7e108c25073)

## Model Architecture
The model is based on **Ultralytics YOLOv10n**, a lightweight and efficient version of the YOLO family, optimized for real-time object detection. We leveraged a pre-trained YOLOv10n model on the **Hagrid dataset** and fine-tuned it for recognizing our specific set of 15 hand gestures. 

## Training Data
To ensure a robust and well-generalized model, we constructed our dataset using:
- **Filtered classes from the Hagrid dataset** to focus on relevant hand gestures
- **Sign language hand gesture datasets** to enhance recognition of specific gestures
- **Synthetic image generation** to expand dataset size and improve class diversity, ensuring better performance in real-world scenarios

## Applications
This model can be utilized in various real-world applications, including:
- **Sign language translation systems**
- **Gesture-based user interfaces**
- **Augmented reality (AR) and virtual reality (VR) interactions**
- **Human-computer interaction for accessibility**

## Contributors
- **Zahra Kazemi**
- **Milad Tavakoli**

