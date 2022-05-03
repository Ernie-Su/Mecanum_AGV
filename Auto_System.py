import pyautogui
import time

def new_tab():
    pyautogui.hotkey('ctrl', 'shift', 't')
    time.sleep(1.0)

def new_window():
    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(3.0)

def source():
    pyautogui.typewrite('source devel/setup.bash')
    pyautogui.hotkey('\n')


# create roscore tab
new_tab()

pyautogui.typewrite('roscore')
pyautogui.hotkey('\n')
time.sleep(2)

# create Joystick tab
new_tab()

pyautogui.typewrite('cd ~/AGV_ws')
pyautogui.hotkey('\n')

source()

pyautogui.typewrite('rosrun JoyStick joystick /dev/input/js0')
pyautogui.hotkey('\n')

# create move_robot tab
new_tab()

pyautogui.typewrite('cd ~/AGV_ws')
pyautogui.hotkey('\n')

source()

pyautogui.typewrite('rosrun move_robot move_robot /dev/teensy_4 115200')
pyautogui.hotkey('\n')


# create sick_tim tab
new_tab()

pyautogui.typewrite('cd ~/AGV_ws')
pyautogui.hotkey('\n')

source()


pyautogui.typewrite('rosrun sick_tim sick_tim551_2050001_YuAn 192.168.0.100 192.168.0.101')
pyautogui.hotkey('\n')

# create laser_merger
new_tab()

pyautogui.typewrite('cd ~/Two_Hokuyo_ws')
pyautogui.hotkey('\n')

source()


pyautogui.typewrite('rosrun ira_laser_tools laserscan_multi_merger')
pyautogui.hotkey('\n')


# create Anhung Control tab
new_tab()

pyautogui.typewrite('cd ~/AGV_ws')
pyautogui.hotkey('\n')

source()

pyautogui.typewrite('rosrun AnhungControl AnhungControl 192.168.43.146 9930')
pyautogui.hotkey('\n')

# create LegDetect tab
new_tab()

pyautogui.typewrite('cd ~/Obs_Detector_ws')
pyautogui.hotkey('\n')

source()

pyautogui.typewrite('rosrun obstacle_detector obstacle_extractor_node')
pyautogui.hotkey('\n')

# create LegDetect tab
new_tab()

pyautogui.typewrite('cd ~/Obs_Detector_ws')
pyautogui.hotkey('\n')

source()

pyautogui.typewrite('rosrun obstacle_detector LegDetect_node')
pyautogui.hotkey('\n')

# create Dispatch tab
new_tab()

pyautogui.typewrite('cd ~/Dispatch_ws')
pyautogui.hotkey('\n')

source()

pyautogui.typewrite('rosrun subscriber agvDispatch.py')
pyautogui.hotkey('\n')

# create hector_slam tab
new_tab()

pyautogui.typewrite('cd ~/AGV_ws')
pyautogui.hotkey('\n')

source()

pyautogui.typewrite('roslaunch hector_slam_launch tutorial.launch')
pyautogui.hotkey('\n')