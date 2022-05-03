# 台科大-欣銓 AGV產學合作案
# Ardentec Industrial-Academic Cooperation AGV Project

## This repo contains the ROS codes and Arduino codes for Ardentec's AGV.
### These contents were backuped at 05/03/2022, documented by Yu-An, Su.

### 1. AGV_ws
Function : Mission Navigation, Motion Control, SICK LiDAR SLAM, Cabinet Center Locate.
### 2. Two_Hokuyo_ws
Function : Merge two scan topic (ira_laser_merger)
### 3. Obs_Detector_ws
Function : LiDAR obstacle detection (Wall, Fence), Cabinet centerPoint Publish.
### 4. Dispatch_ws
Function : Receive Missions, Send AGV status to Dispatch Server.
### 5. Mecanum_Kinematic_220502
Function : Mecanum wheel kinematics, Motor control, Receive speed command from ROS.
### 6. missionGUI
Function : GUI for editing mission points.
### 7. Auto_Two_Sick_Slam.py
Function : Automatically type commands in terminal.
### 8. udp_send_auto.py
Function : Locally send navigation mission to AGV.
### 9. Ardentec AGV Data Format.xlsx
Function : Protocols for AGV status update, mission command, battery serial connection.
