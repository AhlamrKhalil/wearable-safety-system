from sense_hat import SenseHat
sense = SenseHat()

accel = sense.get_accelerometer_raw()
gyro = sense.get_gyroscope_raw()

print("Accelerometer:", accel)
print("Gyroscope:", gyro)