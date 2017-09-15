from Calculator.Calculations import Calculations as Calculations
import tkinter


class Interface(tkinter.Tk):
    '''
    main_widgets: Create Objects for the numbers 0-9,
                  and create a Label to display information.
                  Arrange these objects like a calculator e.g. the windows calculator.
                  I am using the lambda function as a way of calling create_expression,
                  and assigning the returned value to e.g. number1.
                  The lambda function is still new to me and I have no good way of explaining how it's used.
    create_expression: Pass the selected characters to the Calculations create_expression function,
                       and display a list of selected characters on-screen.
    calculate: When a user selects the = key call the calculate function in Calculations.
               This function will display the sum of the evaluated expression.
    '''
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.main_widgets()
        self.protocol("WM_DELETE_WINDOW", self.close)

    def main_widgets(self):
        self.grid()
        self.my_sum = Calculations()

        # Calculator Widgets
        self.number1 = tkinter.Button(self, text="1", command=lambda: self.create_expression(1))
        self.number1.grid(row=3, column=0, sticky='EW')

        self.number2 = tkinter.Button(self, text="2", command=lambda: self.create_expression(2))
        self.number2.grid(row=3, column=1, sticky='EW')

        self.number3 = tkinter.Button(self, text="3", command=lambda: self.create_expression(3))
        self.number3.grid(row=3, column=2, sticky='EW')

        self.number4 = tkinter.Button(self, text="4", command=lambda: self.create_expression(4))
        self.number4.grid(row=2, column=0, sticky='EW')

        self.number5 = tkinter.Button(self, text="5", command=lambda: self.create_expression(5))
        self.number5.grid(row=2, column=1, sticky='EW')

        self.number6 = tkinter.Button(self, text="6", command=lambda: self.create_expression(6))
        self.number6.grid(row=2, column=2, sticky='EW')

        self.number7 = tkinter.Button(self, text="7", command=lambda: self.create_expression(7))
        self.number7.grid(row=1, column=0, sticky='EW')

        self.number8 = tkinter.Button(self, text="8", command=lambda: self.create_expression(8))
        self.number8.grid(row=1, column=1, sticky='EW')

        self.number9 = tkinter.Button(self, text="9", command=lambda: self.create_expression(9))
        self.number9.grid(row=1, column=2, sticky='EW')

        self.number0 = tkinter.Button(self, text="0", command=lambda: self.create_expression(0))
        self.number0.grid(row=4, column=1, sticky='EW')

        self.period = tkinter.Button(self, text=".", command=lambda: self.create_expression('.'))
        self.period.grid(row=4, column=2, sticky='EW')

        self.equals = tkinter.Button(self, text="=", command=self.calculate)
        self.equals.grid(row=4, column=0, sticky='EW')

        self.divide = tkinter.Button(self, text="/", command=lambda: self.create_expression('/'))
        self.divide.grid(row=1, column=3, sticky='EW')

        self.multiply = tkinter.Button(self, text="*", command=lambda: self.create_expression('*'))
        self.multiply.grid(row=2, column=3, sticky='EW')

        self.plus = tkinter.Button(self, text="+", command=lambda: self.create_expression('+'))
        self.plus.grid(row=4, column=3, sticky='EW')

        self.minus = tkinter.Button(self, text="-", command=lambda: self.create_expression('-'))
        self.minus.grid(row=3, column=3, sticky='EW')

        self.clear = tkinter.Button(self, text="Clear", command=self.clear_list)
        self.clear.grid(row=5, column=0, columnspan=2, sticky='EW')

        self.exit = tkinter.Button(self, text="Exit", command=self.close)
        self.exit.grid(row=5, column=2, columnspan=2, sticky='EW')

        self.labelVariable = tkinter.StringVar()
        self.label = tkinter.Label(self, textvariable=self.labelVariable)
        self.label.grid(row=0, column=0, columnspan=4, sticky='EW')
        self.labelVariable.set(u"Hello")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.resizable(True, False)

    def create_expression(self, num):
        my_expression = self.my_sum.create_expression(num)
        self.labelVariable.set(my_expression)

    def clear_list(self):
        cleared_list = self.my_sum.clear_list()
        self.labelVariable.set(cleared_list)

    def calculate(self):
        self.labelVariable.set(self.my_sum.display_sum_total())

    def close(self):
        self.destroy()


if __name__ == '__main__':
    Interface(None).mainloop()
