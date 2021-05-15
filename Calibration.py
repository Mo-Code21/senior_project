# 5/13/21
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
    window.geometry("220x80")
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

    def run():
        arduino.write(b'r')
        # arduino.write(b'run')
        with open("data.csv", 'a') as file:
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(['Inf'])
        print('run')

    def close():
        arduino.write(b'c')
        # arduino.write(b'close')
        print('close')
        arduino.close()
        window.destroy()

    b1 = tk.Button(window, text="Run", command=run)

    b2 = tk.Button(window, text="Close", command=close)

    # b1.grid(row=1, column=0)

    # b2.grid(row=1, column=2)

    b1.pack()
    b2.pack()

    window.after(500, collect_data)

    window.mainloop()


if 'arduino' in globals():
    arduino.close()
# Establish Arduino serial connection
arduino = serial.Serial(port='COM3', baudrate=57600)
print('Established serial connection to Arduino')

# Running the motor function which would display the GUI
motor()
