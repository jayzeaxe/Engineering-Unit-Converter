# July 17 2025

unit_data = {
    "Length": {
        "m": (1, "Meter"),
        "km": (1000, "Kilometer"),
        "cm": (0.01, "Centimeter"),
        "mm": (0.001, "Millimeter"),
        "in": (0.0254, "Inch"),
        "ft": (0.3048, "Foot")
    },

    "Mass": {
        "kg": (1, "Kilogram"),
        "g": (0.001, "Gram"),
        "mg": (0.000001, "Milligram"),
        "lb": (0.453592, "Pound")
    },

    "Area": {
        "m2": (1, "Square Meter"),
        "km2": (1000000, "Square Kilometer"),
        "cm2": (0.0001, "Square Centimeter"),
        "ft2": (0.092903, "Square Foot")
    },

    "Volume": {
        "L": (1, "Liter"),
        "mL": (0.001, "Milliliter"),
        "m3": (1000, "Cubic Meter"),
        "gal": (3.78541, "US Gallon")
    },

    "Time": {
        "s": (1, "Second"),
        "min": (60, "Minute"),
        "hr": (3600, "Hour")
    },

    "Speed": {
        "m/s": (1, "Meters per Second"),
        "km/h": (0.277778, "Kilometers per Hour"),
        "mph": (0.44704, "Miles per Hour")
    },

    "Pressure": {
        "Pa": (1, "Pascal"),
        "kPa": (1000, "Kilopascal"),
        "bar": (100000, "Bar"),
        "psi": (6894.76, "Pounds per Square Inch")
    },

    "Force": {
        "N": (1, "Newton"),
        "kN": (1000, "Kilonewton"),
        "lbf": (4.44822, "Pound-force")
    },

    "Energy": {
        "J": (1, "Joule"),
        "kJ": (1000, "Kilojoule"),
        "cal": (4.184, "Calorie"),
        "Wh": (3600, "Watt-hour")
    },

    "Power": {
        "W": (1, "Watt"),
        "kW": (1000, "Kilowatt"),
        "hp": (745.7, "Horsepower")
    },

    "Voltage": {
        "V": (1, "Volt"),
        "mV": (0.001, "Millivolt"),
        "kV": (1000, "Kilovolt")
    },

    "Current": {
        "A": (1, "Ampere"),
        "mA": (0.001, "Milliampere"),
        "uA": (0.000001, "Microampere")
    },

    "Resistance": {
        "ohm": (1, "Ohm"),
        "kohm": (1000, "Kiloohm"),
        "Mohm": (1000000, "Megaohm")
    }
}


def convert_standard_unit(value, category, from_unit, to_unit):
    units = unit_data[category]


    base_value = value * units[from_unit][0]

  
    result = base_value / units[to_unit][0]

    return result
