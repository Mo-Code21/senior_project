# 5/3/21
# Mohammed
# sensor code


def read_sensor():
    # arduino.write(bytes(x, 'utf-8'))
    # time.sleep(0.05)
    raw_data = arduino.readline()
    data = str(arduino_data.decode("utf-8"))
    print("data Recoded")

    return data


def get_voltage(data):
    A = 128*((2**24)-1)
    print("Pressure calculated")
    return str(5*(data/A))


def animate(data):
    x = range(0, length(data)-1)
    y = data

    ax = plt.gca()
    line = ax.lines

    line.set_data(x, y)

    xlim_low, xlim_high = ax.get_xlim()
    ylim_low, ylim_high = ax.get_ylim()

    ax.set_xlim(xlim_low, (x.max() + 5))

    ymax = y.max()

    ymin = y.min()

    ax.set_ylim((ymin - 5), (ymax + 5))


def save_data(filename, data):
    # filename = time.strftime("%Y-%m-%d_%H%M")
    if not os.path.isfile("data.csv"):
        print("hi")
        with open(filename+".csv", 'w') as file:
            file.write("time,")
            file.write("readings,")
            file.write('\n')

    with open(filename+".csv", 'a') as file:
        file.write(str(data[0])+",")
        file.write(str(data[1])+",")
        file.write('\n')
        return print("data printed")


def main():
    print('hi main')


if __name__ == '__main__':
    main()
