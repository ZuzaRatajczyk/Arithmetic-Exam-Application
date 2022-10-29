import random


def select_level():
    levels_info = {"1": "simple operations with numbers 2-9", "2": "integral squares of 11-29"}
    message = f"""Which level do you want? Enter a number:
    1 - {levels_info["1"]}
    2 - {levels_info["2"]}
    """
    user_level = input(message)
    while user_level not in levels_info:
        user_level = input(message)
    return user_level, levels_info[user_level]


def calculate_first_level(first_comp, second_comp, operator):
    if operator == '+':
        return first_comp + second_comp
    elif operator == '-':
        return first_comp - second_comp
    else:
        return first_comp * second_comp


def calculate_second_level(number):
    return number ** 2


def check_result(user_result, correct_result):
    if user_result == correct_result:
        return 1
    else:
        return 0


def perform_first_level():
    score = 0
    for task in range(5):
        first_element = random.randint(2, 9)
        second_element = random.randint(2, 9)
        random_operator = random.choice(['+', '-', '*'])
        print(f"{first_element} {random_operator} {second_element}")
        user_result = input()
        while not user_result.lstrip("-").isdigit():
            print("Incorrect format.")
            user_result = input()
        result = calculate_first_level(first_element, second_element, random_operator)
        result_info = check_result(int(user_result), result)
        if result_info:
            score += 1
            print("Right!")
        else:
            print("Wrong!")
    return score


def perform_second_level():
    score = 0
    for task in range(5):
        number = random.randint(11, 29)
        print(number)
        user_result = input()
        while not user_result.lstrip("-").isdigit():
            print("Incorrect format.")
            user_result = input()
        result = calculate_second_level(number)
        result_info = check_result(int(user_result), result)
        if result_info:
            score += 1
            print("Right!")
        else:
            print("Wrong!")
    return score


def save_result_to_file(score, level, level_info):
    name = input("What is your name?")
    result_file = open("results.txt", "a")
    result_file.write(f"{name}: {score}/5 in level {level} ({level_info}).")
    print('The results are saved in "results.txt".')
    result_file.close()


def main():
    level, level_info = select_level()
    if level == "1":
        score = perform_first_level()
    else:
        score = perform_second_level()
    print(f"Your mark is {score}/5. Would you like to save the result? Enter yes or no.")
    save_result = input()
    if save_result in ["yes", "y", "YES", "Yes"]:
        save_result_to_file(score, level, level_info)


if __name__ == "__main__":
    main()


