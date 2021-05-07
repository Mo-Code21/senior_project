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
from matplotlib.animation import FuncAnimation
from sensor import *
from motor import *


# def animate(i):
#     with open("data.csv", "r") as file:
#         data = file.readlines()
#         for line in data:
#             # data = file.readline()
#             line = line.strip().split(',')
#             x = line[0]
#             y = line[1]
#     print(x)

#     ax = plt.gca()
#     line = ax.lines

#     line.set_data(x, y)

#     xlim_low, xlim_high = ax.get_xlim()
#     ylim_low, ylim_high = ax.get_ylim()

#     ax.set_xlim(xlim_low, (x.max() + 5))

#     ymax = y.max()

#     ymin = y.min()

#     ax.set_ylim((ymin - 5), (ymax + 5))


arduino.close()
# Establish Arduino serial connection
arduino = serial.Serial(port='COM3', baudrate=57600,)
print('Established serial connection to Arduino')

t = 0  # initiate time variable
while True:

    # read sensor data
    raw_data = arduino.readline()
    data = int(raw_data.decode("utf-8"))
    print(data)
    t += 1
    time.sleep(0.5)

    # saving reding to file
    with open("data.csv", 'a') as file:
        file.write(str(t)+",")
        file.write(str(data)+",")
        file.write('\n')
        print("data printed")

    # plotting the voltage data
    # plt.style.use('fivethirtyeight')
    # plt.plot([], [])
    # ani = FuncAnimation(plt.gcf(), animate, fargs=(t, data), interval=500)
    # plt.tight_layout()
    # plt.show()


# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data


# while True:
#     num = input("Enter a number: ")  # Taking input from user
#     value = write_read(num)
#     print(value)  # printing the value
