# print('Always on')


# def ts():
#     print(1)
#     n = input('enter a number:')
#     n = int(n)
#     while n > 0:
#         n -= 1
#         if n == 2:
#             break
#         print(n)
#     print('Loop ended.')


# def main():
#     ts()


# if __name__ == '__main__':
#     main()
################################################################

# # Importing Libraries
# import serial
# import time
# arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data


# while True:
#     num = input("Enter a number: ")  # Taking input from user
#     value = write_read(num)
#     print(value)  # printing the value
#########################################################################
# import csv
# import os


# def save_data(data):
#     # filename = time.strftime("%Y-%m-%d_%H%M")
#     if not os.path.isfile("data.csv"):
#         print("hi")
#         with open("data.csv", 'w') as file:
#             file.write("time,")
#             file.write("readings,")
#             file.write('\n')

#     with open("data.csv", 'a') as file:
#         file.write(str(data[0])+",")
#         file.write(str(data[1])+",")
#         file.write('\n')
#         return print("data printed")


# data = [4, 2]
# save_data(data)
#########################################################################
# import serial
# import time
# from itertools import count
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # arduino.close()
# # Establish Arduino serial connection
# arduino = serial.Serial(port='COM3', baudrate=57600,)
# print('Established serial connection to Arduino')
# x = []
# plt.style.use('fivethirtyeight')
# plt.plot([], [])

# x = []
# y = []


# def animate(i):
#     # with open("data.csv", "r") as file:
#     #     data = file.readlines()
#     #     for line in data:
#     #         # data = file.readline()
#     #         line = line.strip().split(',')
#     #         x.append(line[0])
#     #         y.append(line[1])
#     #         print(x, y)
#     raw_data = arduino.readline()
#     data = str(raw_data.decode('utf-8'))
#     data = data.strip().split('/r/n')
#     x.append(data)
#     print(x)

#     # ax = plt.gca()
#     # line = ax.lines

#     # line.set_data(x, y)

#     # xlim_low, xlim_high = ax.get_xlim()
#     # ylim_low, ylim_high = ax.get_ylim()

#     # ax.set_xlim(xlim_low, (x.max() + 5))

#     # ymax = y.max()

#     # ymin = y.min()

#     # ax.set_ylim((ymin - 5), (ymax + 5))


# ani = FuncAnimation(plt.gcf(), animate, interval=500)
# plt.tight_layout()
# plt.show()
# # ########################################################################
# from tkinter import *
# import threading

# root = Tk()


# def task():
#     print("hello")
#     root.after(2000, task)  # reschedule event in 2 seconds


# root.after(2000, task)
# root.mainloop()
########################################################################

from tkinter import *

root = Tk()
root.geometry('250x150')

button1 = Button(text="button1")
button1.pack(side=BOTTOM, pady=6)

button2 = Button(text="button2")
button2.pack(side=BOTTOM, pady=3)

root.mainloop()
