# Joystick Control
## Button Configuration

220506 YuAn : 

補齊F710搖桿中所有按鈕, 彈簧板機以及蘑菇頭定義，只有MODE跟Vibration按下去沒有button id。

![Button Configuration](https://github.com/Ernie-Su/Ardentec_AGV/blob/main/img/joystick.PNG)

# move_robot
move_robot中包含了兩個重要的library : All_dir.h 和 move_robot.h

```All_dir.h```中的```timercallback()```會判斷現在是否為搖桿控制(```isReveice_joystick```)，是的話進入手動遙控模式 ; 如果不是的話進入自動導航模式並呼叫```State_Machine()```判斷```P_STATE```。

* 當狀態是```P_STATE_MOVE```的時候會呼叫```Navigation_move()```，進入```Trajectory_Tracking()```裡面的```Tracking_Trajectory()```，也就是主要的導航程式。

* 當狀態是```P_STATE_MISSON```的時候會呼叫```move_robot.h```中的```Misson_state()```，裡面會判斷```MISSON_TYPE```去作出相應的動作，例如 : 頂昇下降或是充電。

## All_dir.h
### Flow explanation

We're using omni mode in this AGV project, so just focus on ```elif``` part in car model switch.
1. Everything starts from ```Trajectory_Tracking()```.
2. The first entry point is ```Tracking_Trajectory()``` in ```Trajectory_Tracking()```.
3. In ```if(confirm_diff_endengle && dis_error <= 0.01 && !Endangle)```, the variable ```confirm_diff_endengle``` is always true in omni mode. For the variable ```Endangle```, it is initialized as false and will be true when the if clause above is true. The crucial factor is ```dis_error```, it controls the ***x, y coordinate's accuracy*** of navigation.
4. Once getting into ```if(confirm_diff_endengle && dis_error <= 0.01 && !Endangle)```, ```Endangle``` is set to true and ```angular_error``` is set to 100. It allows us to enter ```if(Endangle)``` clause and execute ```Calculate_W_rw()```.
5. In ```Calculate_W_rw()```, ```special``` is set to false, so ```if(!special)``` is true. ```if(fabs(angular_error) > M_PI)``` is also true because ```angular_error``` is set to 100. Angular speed (w) 's PID parameter's adjustments will be calculated there. 
6. In ```if(fabs(angular_error) <= 0.03)```, ```angular_error``` controls the ***heading accuracy*** of the navigation.
7. When the navigated position is acceptable, ```endangle_count``` will start counting to 10. Once the counting is done, ```isFinish``` will be set to true. And it goes back to ```Trajectory_Tracking()```.

## move_robot.h

Define every global variable in ```move_robot.h```.

```Misson_state()``` is for mission control. Namely, **State controls type**.
The most used states are ```P_STATE_MOVE``` and ```P_STATE_MISSON```. For example, when AGV is loading and unloading, p_state changes to ```P_STATE_MISSON```, and changes back to ```P_STATE_MOVE``` after the mission is finished.

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

***
For package's head and tail:

```Mr``` : ```Real_Mission```, the navigation package always starts with this. Separate the rest with ```;```.

```E``` : ```End```, the end of the mission.

```;``` : separate ```Mr```, ```mission point``` and ```E```.

As for the mission point :

```0``` : ```id```, the index of navigation mission path.

```0``` : ```type```, the action of this mission point.

```-0.201,0.104,0.039``` : ```position```, it's composed of ```x, y, heading```.

```omni``` : ```kind```, the car model.

```0``` : ?

```1.0``` : ?

***

There's another argument called ```time```, which is at the last position.

```0``` : ```time```, the time argument for type 3.
**Use ```type:3, time:0``` for middle points of the navigation.**


### A_misson
```A_misson``` is composed of a vector of self-defined structure ```SUB_MISSONPATH```. A ```SUB_MISSONPATH``` is composed of two vectors called ```SUB_MISSONPATH_SUBPOINT``` and ```NODE_recv```.

## Written by Yu-An, Su. 2021/09/07
## Updated by Yu-An, Su. 2022/05/16