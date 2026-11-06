from sense_hat import SenseHat
import csv
import time
from datetime import datetime

sense = SenseHat()

filename = "sensor_readings.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "accel_x", "accel_y", "accel_z",
        "gyro_x", "gyro_y", "gyro_z"
    ])
    while True:
        accel = sense.get_accelerometer_raw()
        gyro = sense.get_gyroscope_raw()
        timestamp = datetime.now().isoformat(timespec="milliseconds")

        writer.writerow([
            timestamp,
            accel["x"], accel["y"], accel["z"],
            gyro["x"], gyro["y"], gyro["z"]
        ])

        file.flush()
        time.sleep(0.05)