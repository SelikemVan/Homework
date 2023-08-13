def convert_temperature(temperature, unit_from, unit_to):

    """This function converts temperature from one unit to another.

    :arguments:
        temperature: The temperature to be converted.
        unit_from: The unit of the temperature to be converted.
        unit_to: The unit to convert to.

    Returns:
        The converted temperature.
    """

    # Check if the unit from and unit to are valid.

    if unit_from not in ["Celsius", "Fahrenheit", "Kelvin"]:
        raise ValueError("Invalid unit from!")
    if unit_to not in ["Celsius", "Fahrenheit", "Kelvin"]:
        raise ValueError("Invalid unit to!")

    # Calculate the converted temperature.

    if unit_from == "Celsius":
        if unit_to == "Fahrenheit":
            return temperature * 9 / 5 + 32
        elif unit_to == "Kelvin":
            return temperature + 273.15
    elif unit_from == "Fahrenheit":
        if unit_to == "Celsius":
            return (temperature - 32) * 5 / 9
        elif unit_to == "Kelvin":
            return (temperature + 459.67) * 5 / 9
    elif unit_from == "Kelvin":
        if unit_to == "Celsius":
            return temperature - 273.15
        elif unit_to == "Fahrenheit":
            return temperature * 9 / 5 - 459.67


def main():

    temperature = float(input("Enter the temperature: "))
    print("What unit should the temperature be? For example, Celsius, Fahrenheit, and Kelvin")
    unit_from = input("Enter the unit of the temperature: ")
    unit_to = input("Enter the unit to convert to: ")
    try:
        float(temperature)
    except ValueError:
        print("Invalid temperature!")
    converted_temperature = convert_temperature(temperature, unit_from, unit_to)
    print("The converted temperature is:", converted_temperature)

    main()
