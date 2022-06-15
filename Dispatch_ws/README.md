# Dispatch_ws

## Structure

agvDispatch.py --> main function

dispatchTCP.py --> receive dispatch command from server and upload AGV status to server

anhungUDP.py   --> send navigation points to ROS

## Usage

**Reminder : Remember to execute ```sudo chmod 777 agvDispatch.py```**

```python3 agvDispatch.py (AGV's IP address)```

Example : ```python3 agvDispatch.py 192.168.1.98```
