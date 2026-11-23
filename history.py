conversion_history = []


def add_to_history(value, from_unit, to_unit, result, category):
    record = {
        "category": category,
        "input": value,
        "from": from_unit,
        "to": to_unit,
        "result": result
    }

    conversion_history.append(record)


def display_history():
    print("")
    print("       CONVERSION HISTORY")
    print("")

    if not conversion_history:
        print("No conversions have been made yet.")

    else:
        for number, record in enumerate(conversion_history, start=1):
            print(f"\nConversion #{number}")
            print(f"Category: {record['category']}")
            print(f"Input: {record['input']} {record['from']}")
            print(f"Result: {record['result']:.4f} {record['to']}")

  
