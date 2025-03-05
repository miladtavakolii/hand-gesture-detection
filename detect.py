import cv2
import supervision as sv
from ultralytics import YOLOv10

model = YOLOv10('/home/milad/deeplearning/hand-gesture-detection/runs/detect/train11/weights/best.pt')


cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.flip(image, 1)

    results = model(image)[0]
    detections = sv.Detections.from_ultralytics(results)

    bounding_box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    annotated_image = bounding_box_annotator.annotate(
        scene=image, detections=detections)
    annotated_image = label_annotator.annotate(
        scene=annotated_image, detections=detections)

    image = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)

    cv2.imshow('Gesture Detection', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()