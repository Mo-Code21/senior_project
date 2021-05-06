# 5/3/21
# Mohammed
# Motor control
import serial
import tkinter as tk
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


def motor():
    window = tk.Tk()
    window.configure(background="white")
    window.geometry("220x80")
    window.title("Motor Control")

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

    window.mainloop()


def main():
    print('main fun')
    motor()


if __name__ == "__main__":
    motor()
