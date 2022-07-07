# Mecanum Wheel-Driven AGV 麥克納姆輪自動導引車

## These contents were backuped at 05/03/2022, documented by Yu-An, Su.

### 1. AGV_ws
1. Mission Navigation
2. Motion Control
3. SICK LiDAR SLAM
4. Cabinet Center Locate.
### 2. Two_Hokuyo_ws
* Merge two scan topic (ira_laser_merger)
### 3. Obs_Detector_ws
1. LiDAR obstacle detection (Wall, Fence)
2. Cabinet centerPoint Publish.
### 4. Dispatch_ws
1. Receive navigation missions from Dispatch Server
2. Send updated AGV status to Dispatch Server.
### 5. Mecanum_Kinematic_220502
1. Receive speed command from ROS.
2. Calculate mecanum wheel kinematics.
3. Motor speed and direction control.
### 6. missionGUI
* GUI for editing mission points.
### 7. Auto_System.py
* Automatically type commands in terminal.
### 8. udp_send_auto.py
* Locally send navigation mission to AGV.
### 9. AGV Data Format.xlsx
* Protocols for AGV status update, mission command, battery serial connection.
