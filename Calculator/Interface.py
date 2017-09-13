from Calculator.Calculations import Calculations as Calculations
import tkinter


class Interface(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.main_widgets()

    def main_widgets(self):
        self.grid()

        self.number1 = tkinter.Button(self, text="1", command=lambda: self.create_expression(1))
        self.number1.grid(row=3, column=0)

        self.number2 = tkinter.Button(self, text="2", command=lambda: self.create_expression(2))
        self.number2.grid(row=3, column=1)

        self.number3 = tkinter.Button(self, text="3", command=lambda: self.create_expression(3))
        self.number3.grid(row=3, column=2)

        self.number4 = tkinter.Button(self, text="4", command=lambda: self.create_expression(4))
        self.number4.grid(row=2, column=0)

        self.number5 = tkinter.Button(self, text="5", command=lambda: self.create_expression(5))
        self.number5.grid(row=2, column=1)

        self.number6 = tkinter.Button(self, text="6", command=lambda: self.create_expression(6))
        self.number6.grid(row=2, column=2)

        self.number7 = tkinter.Button(self, text="7", command=lambda: self.create_expression(7))
        self.number7.grid(row=1, column=0)

        self.number8 = tkinter.Button(self, text="8", command=lambda: self.create_expression(8))
        self.number8.grid(row=1, column=1)

        self.number9 = tkinter.Button(self, text="9", command=lambda: self.create_expression(9))
        self.number9.grid(row=1, column=2)

        self.number0 = tkinter.Button(self, text="0", command=lambda: self.create_expression(0))
        self.number0.grid(row=4, column=1)

        self.period = tkinter.Button(self, text=".", command=lambda: self.create_expression('.'))
        self.period.grid(row=4, column=2)

        self.equals = tkinter.Button(self, text="=", command=self.calculate)
        self.equals.grid(row=4, column=0)

        self.divide = tkinter.Button(self, text="/", command=lambda: self.create_expression('/'))
        self.divide.grid(row=1, column=3)

        self.multiply = tkinter.Button(self, text="*", command=lambda: self.create_expression('*'))
        self.multiply.grid(row=2, column=3)

        self.plus = tkinter.Button(self, text="+", command=lambda: self.create_expression('+'))
        self.plus.grid(row=4, column=3)

        self.minus = tkinter.Button(self, text="-", command=lambda: self.create_expression('-'))
        self.minus.grid(row=3, column=3)

        self.labelVariable = tkinter.StringVar()
        self.label = tkinter.Label(self, textvariable=self.labelVariable)
        self.label.grid(row=0, column=0, columnspan=4)
        self.labelVariable.set(u"Hello")

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

    def create_expression(self, num):
        my_sum = Calculations()
        my_expression = my_sum.create_expression(num)
        self.labelVariable.set(my_expression)

    def calculate(self):
        my_sum = Calculations()
        self.labelVariable.set(my_sum.display_sum_total())


if __name__ == '__main__':
    app = Interface(None)
    app.mainloop()
