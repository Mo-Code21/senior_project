# 5/3/21
# Mohammed
# sensor code


# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


def lop():
    while True:
        num = input("Enter a number: ")  # Taking input from user
        value = write_read(num)
        print(value)  # printing the value

        if num == '0':
            break


def main():
    print('hi main')


if __name__ == '__main__':
    main()
