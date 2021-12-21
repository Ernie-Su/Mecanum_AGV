# 台科大-欣銓 AGV產學合作案
# Ardentec Industrial-Academic Cooperation AGV Project

## This repo contains the ROS codes and Arduino codes for Ardentec's AGV.
### These contents were backuped at 12/20/2021, documented by Yu-An, Su.

### 1. AGV_ws
Function : Motion Control, SICK LiDAR SLAM.
### 2. Two_Hokuyo_ws
Function : Merge two scan topic
### 3. Obs_Detector_ws
Function : LiDAR obstacle detection, obstacle publish
### 4. Dispatch_ws
Function : Receive dispatch packets from HMI and C# server.
### 5. Mecanum_Kinematic_1214
Function : Motor control, Serial connection between ROS and Arduino.
### 6. Auto_Two_Sick_Slam.py
Function : Automatically type commands in Terminal.
### 7. udp_send.py
Function : Send navigation mission to AGV.
