import random

score = 0


def calculate(first_comp, second_comp, operator):
    if operator == '+':
        return first_comp + second_comp
    elif operator == '-':
        return first_comp - second_comp
    else:
        return first_comp * second_comp


def check_result(user_result, correct_result):
    global score
    if user_result == correct_result:
        score += 1
        return "Right!"
    else:
        return "Wrong!"


def main():
    for task in range(5):
        first_element = random.randint(2, 9)
        second_element = random.randint(2, 9)
        random_operator = random.choice(['+', '-', '*'])
        print(f"{first_element} {random_operator} {second_element}")
        user_result = input()
        while not user_result.lstrip("-").isdigit():
            print("Incorrect format.")
            user_result = input()
        result = calculate(first_element, second_element, random_operator)
        print(check_result(int(user_result), result))
    print(f"Your mark is {score}/5.")


if __name__ == "__main__":
    main()


