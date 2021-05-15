# 5/14/21
# Mohammed
# Processing sensor data and controlling motor

# Importing Libraries
import serial
import time
import csv
import numpy as np
import tkinter as tk

# Main function


def motor():
    window = tk.Tk()
    window.configure(background="white")
    # window.geometry("220x80")
    window.title("Motor Control")

    def collect_data():
        # read sensor data
        raw_data = arduino.readline()
        data = raw_data.decode('utf-8').strip()
        print(data)
        time.sleep(0.5)

        # saving reding to file
        with open("data.csv", 'a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow([data])

        window.after(500, collect_data)

    def run_1():
        arduino.write(b'o')
        with open("data.csv", 'a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['1.3Pa'])
        print('1.3Pa')

    def run_2():
        arduino.write(b't')
        with open("data.csv", 'a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['2.6Pa'])
        print('2.6Pa')

    def run_3():
        arduino.write(b'h')
        with open("data.csv", 'a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['4.0Pa'])
        print('4.0Pa')

    def run_4():
        arduino.write(b'f')
        with open("data.csv", 'a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['5.3Pa'])
        print('5.3Pa')

    def run():
        arduino.write(b'r')
        with open("data.csv", 'a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['run'])
        print('run')

    def close():
        with open("data.csv", 'a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['close'])
        print('close')
        arduino.close()
        window.destroy()

    b1 = tk.Button(window, text="Run", command=run)

    b2 = tk.Button(window, text="Close", command=close)

    b3 = tk.Button(window, text="1.3 Pa", command=run_1)

    b4 = tk.Button(window, text="2.6 Pa", command=run_2)

    b5 = tk.Button(window, text="4.0 Pa", command=run_3)

    b6 = tk.Button(window, text="5.3 Pa", command=run_4)

    # b1.grid(row=1, column=0)

    # b2.grid(row=1, column=2)

    b1.pack(side='top')
    b2.pack(side='top')
    b3.pack(side='bottom')
    b4.pack(side='bottom')
    b5.pack(side='bottom')
    b6.pack(side='bottom')

    window.after(500, collect_data)

    window.mainloop()


if 'arduino' in globals():
    arduino.close()
# Establish Arduino serial connection
arduino = serial.Serial(port='COM3', baudrate=57600)
print('Established serial connection to Arduino')

# Running the motor function which would display the GUI
motor()
