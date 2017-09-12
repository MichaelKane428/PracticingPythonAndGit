from Calculator.Calculations import Calculations as Calculations
from tkinter import *


class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="red")
        self.parent = parent
        self.widgets()

    def widgets(self):
        self.label = Label(self, text="")
        self.label.grid(row=0, columnspan=4)

        self.number1 = Button(self, text="1")
        self.number1.grid(row=1, column=0)

        self.number2 = Button(self, text="2")
        self.number2.grid(row=1, column=1)

        self.number3 = Button(self, text="3")
        self.number3.grid(row=1, column=2)

        self.equals = Button(self, text="=")
        self.equals.grid(row=1, column=3)

    def calculate(self):
        my_sum = Calculations()
        print(my_sum.addition(1, 1))


class Interface(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.main_widgets()

    def main_widgets(self):
        self.window = MainFrame(self)
        self.window.grid(row=0, column=10, rowspan=2)


if __name__ == '__main__':
    app = Interface(None)
    app.mainloop()
