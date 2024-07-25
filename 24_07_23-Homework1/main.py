# YouTube URL from where the project is taken:
# https://www.youtube.com/watch?v=HXDD7-EnGBY&ab_channel=Murtaza%27sWorkshop-RoboticsandAI

import cv2
import os

cap = cv2.VideoCapture(0)  # 0 for native webcam, 1 for phone webcam
cap.set(3, 640)
cap.set(4, 480)

classFile = os.getcwd() + "/Object_Detection_Files/coco.names"
with open(classFile, "rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = (
    os.getcwd() + "/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
)
weightPath = os.getcwd() + "/Object_Detection_Files/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

try:
    while True:
        success, img = cap.read()
        if not success:
            break

        classIds, confs, bbox = net.detect(img, confThreshold=0.5)

        for classId, confidence, box in zip(classIds, confs, bbox):
            label = f"{classNames[classId - 1]}: {confidence:.2f}"
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv2.putText(
                img,
                label,
                (box[0], box[1]),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )

        cv2.imshow("Object Detection", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    cap.release()
    cv2.destroyAllWindows()
