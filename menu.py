def display_main_menu():
    
    print("[1] Convert Units")
    print("[2] View Conversion History")
    print("[3] Exit")
    print("")
 


def display_categories(categories):
    print("AVAILABLE CATEGORIES")

    for number, category in enumerate(categories, start=1):
        print(f"[{number}] {category}")


def display_units(units):
    print("AVAILABLE UNITS")

    for symbol, details in units.items():
        if isinstance(details, tuple):
            print(f"{symbol} - {details[1]}")
        else:
            print(f"{symbol} - {details}")