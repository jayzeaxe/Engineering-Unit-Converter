def convert_temperature(value, from_unit, to_unit):

    # First, convert the input into Celsius
    if from_unit == "C":
        celsius = value

    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9

    elif from_unit == "K":
        celsius = value - 273.15

    else:
        raise ValueError("Invalid temperature unit.")

 
    if to_unit == "C":
        result = celsius

    elif to_unit == "F":
        result = (celsius * 9 / 5) + 32

    elif to_unit == "K":
        result = celsius + 273.15

    else:
        raise ValueError("Invalid temperature unit.")

    return result
