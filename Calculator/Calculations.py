class Calculations(object):
    def __init__(self, my_expression=[]):
        self.my_expression = my_expression

    def create_expression(self, num):
        self.my_expression.append(num)
        return str(self.my_expression)

    def display_sum_total(self):
        total = ''
        total = total.join(str(self.my_expression))
        total = eval(total)
        self.my_expression.clear()
        return total

