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
import csv
import os


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


data = [4, 2]
save_data(data)