import random


def calculate(first_comp, second_comp, operator):
    if operator == '+':
        return first_comp + second_comp
    elif operator == '-':
        return first_comp - second_comp
    else:
        return first_comp * second_comp


def main():
    first_element = random.randint(2, 9)
    second_element = random.randint(2, 9)
    random_operator = random.choice(['+', '-', '*'])
    print(f"{first_element} {random_operator} {second_element}")
    user_result = int(input())
    result = calculate(first_element, second_element, random_operator)
    if user_result == result:
        print("Right!")
    else:
        print("Wrong!")


if __name__ == "__main__":
    main()


