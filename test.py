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


# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    num = input("Enter a number: ")  # Taking input from user
    value = write_read(num)
    print(value)  # printing the value
