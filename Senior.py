# 5/3/21
# Mohammed
# Processing sensor data and controlling motor

# Importing Libraries
import serial
import time
import matplotlib.pyplot as plt
import numpy as np


arduino = serial.Serial(port='COM3', baudrate=57600, timeout=.1)
print('Established serial connection to Arduino')


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    num = input("Enter a number: ")  # Taking input from user
    value = write_read(num)
    print(value)  # printing the value
