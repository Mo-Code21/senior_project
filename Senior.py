# 5/3/21
# Mohammed
# Processing sensor data and controlling motor

# Importing Libraries
import os
import serial
import time
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from sensor import *
from motor import *

# Establish Arduino serial connection
arduino = serial.Serial(port='COM3', baudrate=57600, timeout=10)
print('Established serial connection to Arduino')

# read sensor data
# row_data = read_sensor()
# print(row_data)
# time.sleep(1)

# convert the row data to voltage
# voltage = get_voltage(row_data)

# plotting the voltage data
# plt.style.use('fivethirtyeight')
# plt.plot([], [])
# ani = FuncAnimation(plt.gcf(), animate, interval=100)
# plt.tight_layout()
# plt.show()

# save_data(voltage_data, voltage)


# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data


# while True:
#     num = input("Enter a number: ")  # Taking input from user
#     value = write_read(num)
#     print(value)  # printing the value
