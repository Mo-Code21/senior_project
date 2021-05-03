# 5/3/21
# Mohammed
# Motor control

def motor():
    window = tk.Tk()
    window.configure(background="white")
    window.geometry("220x80")
    window.title("Motor Control")

    def run():
        arduino.write(b'r')

    def close():
        arduino.write(b'c')
        arduino.close()
        window.distroy()

    b1 = tk.Button(window, text="Run", command=run)

    b2 = tk.Button(window, text="Close", command=close)

    b1.grid(row=1, column=0, padx=5, pady=10)

    b2.grid(row=1, column=1, padx=5, pady=10)

    window.mainloop()


if __name__ == "__motor__":
    motor()
