math_operation = input()
first_element = int(math_operation.split()[0])
second_element = int(math_operation.split()[2])
input_operator = math_operation.split()[1]


def calculate(first_comp, second_comp,operator):
    if operator == '+':
        return first_comp + second_comp
    elif operator == '-':
        return first_comp - second_comp
    else:
        return first_comp * second_comp


print(calculate(first_element, second_element, input_operator))
