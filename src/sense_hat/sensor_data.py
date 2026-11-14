from sense_hat import SenseHat
import csv
import time
from datetime import datetime

sense = SenseHat()

filename = "sensor_test_01.csv"

# movements for the first sensor test
movements = [
    "No movement",
    "Side to side movement",
    "Forward and backward movement"
]

with open(filename, "x", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "timestamp", "movement",
        "accel_x", "accel_y", "accel_z",
        "gyro_x", "gyro_y", "gyro_z"
    ])

    for movement in movements:
        input("Press Enter to start: " + movement)
        print("Recording:", movement)

        # record each movement for 10 seconds
        start = time.time()

        while time.time() - start < 10:
            accel = sense.get_accelerometer_raw()
            gyro = sense.get_gyroscope_raw()
            timestamp = datetime.now().isoformat(timespec="milliseconds")

            writer.writerow([
                timestamp, movement,
                accel["x"], accel["y"], accel["z"],
                gyro["x"], gyro["y"], gyro["z"]
            ])

            file.flush()
            time.sleep(0.05)

        print("Finished!")

print("Data saved to:", filename)
