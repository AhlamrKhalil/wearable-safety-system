# Read the M5StickS3 accelerometer and gyroscope
# Runs on the device with uiflow2 (MicroPython)
# Run with: py -m mpremote connect COM4 run src/m5stick/read_imu.py

import time
import M5
from M5 import *

# must be called before using the IMU
M5.begin()

# take 20 readings, one every 0.1 seconds (about 2 seconds)
for i in range(20):
    M5.update()
    
    accel = Imu.getAccel()
    gyro = Imu.getGyro()

    print("accel:", accel, "gyro:", gyro)
    time.sleep_ms(100)

print("Finished")