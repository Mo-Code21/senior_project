# 5/3/21
# Mohammed
# Processing sensor data and controlling motor

# Importing Libraries
import os
import serial
import time
import csv
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.animation import FuncAnimation


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

def motor():
    window = tk.Tk()
    window.configure(background="white")
    window.geometry("220x80")
    window.title("Motor Control")

    def collect_data():
        # read sensor data
        raw_data = arduino.readline()
        data = str(raw_data.decode('utf-8'))
        print(data)
        time.sleep(0.5)

        # saving reding to file
        with open("data.csv", 'a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow([str(data)])
            print("data printed")

        window.after(500, collect_data)

    def run():
        arduino.write(b'r')
        print('run')

    def close():
        arduino.write(b'c')
        print('close')
        arduino.close()
        window.destroy()

    b1 = tk.Button(window, text="Run", command=run)

    b2 = tk.Button(window, text="Close", command=close)

    b1.grid(row=1, column=0)

    b2.grid(row=1, column=2)

    window.after(500, collect_data)

    window.mainloop()


if 'arduino' in globals():
    arduino.close()
# Establish Arduino serial connection
arduino = serial.Serial(port='COM3', baudrate=57600,)
print('Established serial connection to Arduino')

t = 0  # initiate time variable
# while True:
motor()

# x = input("run(r) or not(any):")
# if x == 'r'r:
#     arduino.write(bytes(x, 'utf-8'))
# plotting the voltage data
# plt.style.use('fivethirtyeight')
# plt.plot([], [])
# ani = FuncAnimation(plt.gcf(), animate, fargs=(t, data), interval=500)
# plt.tight_layout()
# plt.show()
