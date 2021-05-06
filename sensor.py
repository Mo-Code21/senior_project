# 5/3/21
# Mohammed
# sensor code


# Importing Libraries
import serial
import time
import csv
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


def write_read():
    # arduino.write(bytes(x, 'utf-8'))
    # time.sleep(0.05)
    raw_data = arduino.readline()
    data = str(arduino_data.decode("utf-8"))

    return data


def save_data(data):
    # filename = time.strftime("%Y-%m-%d_%H%M")
    if not os.path.isfile("data.csv"):
        print("hi")
        with open("data.csv", 'w') as file:
            file.write("time,")
            file.write("readings,")
            file.write('\n')

    with open("data.csv", 'a') as file:
        file.write(str(data[0])+",")
        file.write(str(data[1])+",")
        file.write('\n')
        return print("data printed")


def main():
    print('hi main')


if __name__ == '__main__':
    main()
