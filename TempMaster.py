def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def temperature_converter():
    print("Temperature Converter")
    print("--------------------")
    print("Options:")
    print("1: Celsius")
    print("2: Fahrenheit")
    print("3: Kelvin")
    
    from_unit = input("Enter the number of the unit you want to convert from: ")
    to_unit = input("Enter the number of the unit you want to convert to: ")
    
    try:
        value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    result = None

    if from_unit == "1":  # Celsius
        if to_unit == "2":
            result = celsius_to_fahrenheit(value)
        elif to_unit == "3":
            result = celsius_to_kelvin(value)
        elif to_unit == "1":
            result = value
    elif from_unit == "2":  # Fahrenheit
        if to_unit == "1":
            result = fahrenheit_to_celsius(value)
        elif to_unit == "3":
            result = fahrenheit_to_kelvin(value)
        elif to_unit == "2":
            result = value
    elif from_unit == "3":  # Kelvin
        if to_unit == "1":
            result = kelvin_to_celsius(value)
        elif to_unit == "2":
            result = kelvin_to_fahrenheit(value)
        elif to_unit == "3":
            result = value
    else:
        print("Invalid unit selection.")
        return

    print(f"The converted temperature is: {result:.2f}")

# Run the converter
temperature_converter()
