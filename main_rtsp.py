#!/usr/bin/env python3.6

import cv2
import os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

# Set your RTST configuration
user_id = ""  #"admin" 
user_pw = ""  #"password" 
host = "127.0.0.1"  #host's ip address
port = "8554"

if (user_id) and (user_pw):
    print("ID and Password is enterd")
    cap = cv2.VideoCapture(f"rtsp://{user_id}:{user_pw}@{host}/")
else:
    print("ID and Password is empty")
    cap = cv2.VideoCapture(f"rtsp://{host}:{port}/")

print("loading...")

while(True):
    try:
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('HELLO-RTSP', frame)
        cv2.waitKey(1)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break

cap.release()
cv2.destroyAllWindows()
