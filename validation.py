import math


def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if not math.isfinite(value):
                print("Please enter a valid finite number.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a number.")


def get_menu_choice(prompt, minimum, maximum):
    while True:
        try:
            choice = int(input(prompt))

            if minimum <= choice <= maximum:
                return choice

            else:
                print(f"Please enter a number from {minimum} to {maximum}.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")


def get_unit(prompt, valid_units):
    valid_unit_set = {unit.lower() for unit in valid_units}

    while True:
        unit = input(prompt).strip()

        if unit.lower() in valid_unit_set:
            for valid_unit in valid_units:
                if unit.lower() == valid_unit.lower():
                    return valid_unit

        print("Invalid unit! Please choose from the displayed units.")
