from Calculator.Interface import Interface as Interface
import tkinter


def main():
    screen = tkinter.Tk()
    main_screen = Interface(screen)
    main_screen.mainloop()
    # my_sum = Calculations()
    # print(my_sum.addition(1, 1))


if __name__ == '__main__':
    main()
