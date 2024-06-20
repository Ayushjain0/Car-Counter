from ultralytics import YOLO
import cv2
model=YOLO('../yolo-weights/yolov8m.pt')
results=model("images\WIN_20230302_19_30_48_Pro.jpg",show=True)
cv2.waitKey(0)