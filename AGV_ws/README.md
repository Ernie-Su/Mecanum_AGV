# move_robot
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

### Important variables
Navigation's accuracy control : ```dis_error``` and ```angular_error```


## move_robot.h

```State_Machine()``` is the most important part because it controls the whole navigation. It is called in ```timerCallback()``` of ```AllDir.h```, and it calls ```Misson_state()``` for mission control. Namely, **state controls type**.
The most seen states are 2 (```P_STATE_MOVE```) and 1 (```P_STATE_MISSON```). When AGV is loading and unloading, state changes to ```P_STATE_MISSON```, and changes back to ```P_STATE_MOVE``` after the mission is finished.

### Important variables

#### 1. state
```P_STATE_MISSON : 1```
```P_STATE_MOVE : 2```
```P_STATE_TIME_DELAY : 10```

#### 2. type
```MISSON_Loading_Interrupt : 4```
```MISSON_unLoading_Interrupt : 6```

### A_misson
```A_misson``` is composed of a vector of self-defined structure ```SUB_MISSONPATH```. A ```SUB_MISSONPATH``` is composed of two vectors called ```SUB_MISSONPATH_SUBPOINT``` and ```NODE_recv```.

## Written by Yu-An, Su. 2021/09/07
