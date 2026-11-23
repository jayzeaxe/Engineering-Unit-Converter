# July 17 2025

from converters.standard_converter import unit_data, convert_standard_unit
from converters.temperature_converter import convert_temperature
from menus.menu import display_main_menu, display_categories, display_units
from utilities.validation import get_number, get_menu_choice, get_unit
from utilities.history import add_to_history, display_history


def perform_conversion():
    categories = list(unit_data.keys()) + ["Temperature"]

    print("\nSELECT A CATEGORY")
    display_categories(categories)

    category_choice = get_menu_choice(
        "Choose a category: ", 1, len(categories)
    )

    category = categories[category_choice - 1]


    if category == "Temperature":
        units = {
            "C": "Celsius",
            "F": "Fahrenheit",
            "K": "Kelvin"
        }

    else:
        units = unit_data[category]

    display_units(units)

    value = get_number("\nEnter the value to convert: ")

    from_unit = get_unit("\nConvert from: ", units.keys())
    to_unit = get_unit("Convert to: ", units.keys())

    # Perform the conversion
    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    else:
        result = convert_standard_unit(
            value, category, from_unit, to_unit
        )

    print("")
    print("        CONVERSION RESULT")
    print("")
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")
    print("")

    add_to_history(
        value, from_unit, to_unit, result, category
    )


def main():
    print("Welcome to the Engineering Unit Converter!")

    while True:
        display_main_menu()

        choice = get_menu_choice("Enter your choice: ", 1, 3)

        if choice == 1:
            perform_conversion()

        elif choice == 2:
            display_history()

        elif choice == 3:
            print("\nThank you for using the Engineering Unit Converter!")
            print("Program terminated.")
            break


if __name__ == "__main__":
    main()
 