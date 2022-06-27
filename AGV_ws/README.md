# Joystick Control
## Button Configuration

220506 YuAn : 

補齊F710搖桿中所有按鈕, 彈簧板機以及蘑菇頭定義，只有MODE跟Vibration按下去沒有button id。

![Button Configuration](https://github.com/Ernie-Su/Ardentec_AGV/blob/main/img/joystick.PNG)

# move_robot pkg
move_robot中包含了兩個重要的library : All_dir.h 和 move_robot.h

```All_dir.h```中的```timercallback()```會判斷現在是否為搖桿控制(```isReveice_joystick```)，是的話進入手動遙控模式 ; 如果不是的話進入自動導航模式並呼叫```State_Machine()```判斷```P_STATE```。

* 當狀態是```P_STATE_MOVE```的時候會呼叫```Navigation_move()```，進入```Trajectory_Tracking()```裡面的```Tracking_Trajectory()```，也就是主要的導航程式。

* 當狀態是```P_STATE_MISSON```的時候會呼叫```move_robot.h```中的```Misson_state()```，裡面會判斷```MISSON_TYPE```去作出相應的動作，例如 : 頂昇下降或是充電。

## All_dir.h
### 導航流程

欣銓AGV使用的是麥輪，所以只需注意CarKind為```omni```的部分，```diff```跟```omni_2```都可不看;我們也沒用到裏頭的避障，可以忽略。

1. 當狀態是```P_STATE_MOVE```時會進行導航移動，由```Navigation_move()```進入```Trajectory_Tracking()```裡面的```Tracking_Trajectory()```。
2. ```Tracking_Trajectory()```中會以```Path_size```的值來判斷現在要進行的是前面80%還是後面20%的導航。
3. 前80%的導航會進行x, y位置的修正，後20%則在到達x, y位置後修正heading。
4. x, y位置的導航使用```robot_pos```與目標任務點的直線距離```dis_error```當作PID控制的輸入，PID輸出為直線速度。取AGV與目標點的夾角```way_theta```套入計算x, y方向的速度分量```Vx, Vy```。
5. heading修正的部分須注意修正heading的PID控制函式是```Calculate_W_rw()```。

## move_robot.h
### 任務執行

AGV到達任務點後就會執行點上的任務，```Misson_state()```會判斷當前任務。

任務列表可參考type :

### Important variables 
#### (Updated by Yu-An Su, 2022/05/12)

#### 1. p_state

| p_state               | number |
| --------------------- | ------ |
| P_STATE_MISSON        | 1      |
| P_STATE_MOVE          | 2      |
| P_STATE_TIME_DELAY    | 10     |
| P_STATE_CENTER_LOCATE | 12     |

#### 2. type

| type                       | number |
| -------------------------- | ------ |
| MISSON_Loading_Time        | 3      |
| MISSON_Loading_Interrupt   | 4      |
| MISSON_unLoading_Interrupt | 6      |
| MISSON_Charge              | 20     |
| MISSON_Uncharge            | 21     |
| MISSON_Center_Locate       | 22     |
| MISSON_SleepWall           | 23     |
| MISSON_Close_Obs           | 24     |
| MISSON_Close_FrontWall     | 25     |

#### 3. Navigation's accuracy control
x, y coordination's tolerance : ```dis_error```

angular tolerance : ```angular_error```
***

# Anhung Control

Anhung Control receives navigation point packets and prints out robot's pose. 

## Dataflow
For example : 
```
E;NULL,252.127.0.0,0;E
I;NULL,-1,252.127.0.0,open,0;E
Sc;NULL,-1,252.127.0.0,ivam,20;E
```

***

```Dataflow = ```
```head + CarName```, ```Carnumber```, ```IP_buf```, ```MAP_NAME```, ```robot_pose_x```, ```robot_pose_y```, ```robot_pose_z```, ```real_pose_x```, ```real_pose_y```, ```real_pose_z```, ```robot_V```, ```missState```, ```State```, ```pos_id```, ```Voltage_st```, ```Current_st```, ```RelativeSOC1_st```, ```RelativeSOC2_st```, ```RelativeSOC3_st```, ```RelativeSOC4_st```, ```AbsoluteSOC1_st```, ```AbsoluteSOC2_st```, ```AbsoluteSOC3_st```, ```AbsoluteSOC4_st```, ```Temp1_st```, ```Temp2_st```, ```Temp3_st```, ```Temp4_st```, ```send_opentime```, ```send_missiontime```, ```send_all_dis_now```, ```send_mission_dis_now```, ```Battery_volt + v + tail```;

***

# hector_slam_anhung
To run hector slam, click ```2D estimation``` on ```rviz``` and give robot a pose on the map first. 

## udp_send.py

### Format

A turning back mission :
```
Mr;0,0,-0.201,0.104,0.039,omni,0,1.0;1,6,3.665,-2.130,0.010,omni,0,1.0;2,6,0.201,0.104,0.039,omni,0,1.0;E
```
### Format Explanation

Take the first point as example :
```Mr```; ```0```, ```0```, ```-0.201,0.104,0.039```, ```omni```, ```0```, ```1.0```

| 封包格式           | 說明                                 |
| ------------------ | ------------------------------------ |
| Mr                 | Real_Mission，導航任務會使用這個封頭 |
| 0                  | id : 任務索引                        |
| 0                  | type : 任務種類                      |
| -0.201,0.104,0.039 | position : 任務點位(x, y, z)         |
| omni               | CarKind : AGV種類                    |
| 0                  | 直線或曲線                           |
| 1.0                | 曲線旋轉半徑                         |
| 0                  | 走空點時為 time_delay                |

***

There's another argument called ```time```, which is at the last position.

```0``` : ```time```, the time argument for type 3.
**Use ```type:3, time:0``` for middle points of the navigation.**


### A_misson
```A_misson``` is composed of a vector of self-defined structure ```SUB_MISSONPATH```. A ```SUB_MISSONPATH``` is composed of two vectors called ```SUB_MISSONPATH_SUBPOINT``` and ```NODE_recv```.

## Written by Yu-An, Su. 2021/09/07
## Updated by Yu-An, Su. 2022/05/16