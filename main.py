import cv2
from ultralytics import YOLO

# Load a pretrained YOLO model
# model = YOLO("yolo11n.pt")
model = YOLO("runs/detect/train4/weights/best.pt")

for i in range(1,12):
    # Perform object detection on an image
    results = model(f"img\img ({i}).jpeg")

    # Visualize the results
    # for result in results:
    #     result.show()
        
    for result in results:
        result.save(filename=f"results/result{i}.jpg")

# Perform object detection on an image
# results = model(f"WhatsApp Video 2025-02-12 at 17.02.44.mp4")
# Visualize the results
# for result in results:
#     result.show()

# i = 1
# for result in results:
#     i += 1
#     result.save(filename=f"results/result{i}.jpg")