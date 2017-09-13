class Calculations(object):
    def __init__(self, my_expression=[]):
        self.my_expression = my_expression

    def create_expression(self, num):
        self.my_expression.append(num)
        return str(self.my_expression)

    def display_sum_total(self):
        temp_string = ""
        temp_string = temp_string.join(repr(str(value)) for value in self.my_expression).replace('\'', '')
        self.my_expression.clear()
        return eval(temp_string)

