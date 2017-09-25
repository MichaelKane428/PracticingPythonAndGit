class Calculations(object):
    '''
    create_expression: Create a list of characters to be evaluated and return it to the GUI.
    display_sum_total: Take the list of characters and convert it to a string, replacing all quotes with white space.
                       Then evaluate the expression,
                       upon completion of the evaluation clear the list of strings,
                       and return it to the GUI.
    '''
    def __init__(self, my_expression=[]):
        self.my_expression = my_expression

    def create_expression(self, num):
        self.my_expression.append(num)
        return str(self.my_expression)

    # The purpose of this function is too remove all single quotes from the current expression using repr,
    # then we clear the expression, and evaluate then return the temp string,
    # eval treats a string as a numeric expression.
    def display_sum_total(self):
        temp_string = ""
        temp_string = temp_string.join(repr(str(value)) for value in self.my_expression).replace('\'', '')
        self.my_expression.clear()
        return eval(temp_string)

    def clear_list(self):
        self.my_expression.clear()
        return u"Cleared"
