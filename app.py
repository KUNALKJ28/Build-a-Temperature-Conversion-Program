def convert_temperature(value, unit):
    unit = unit.lower()

    if unit == 'c':
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return fahrenheit, kelvin

    elif unit == 'f':
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return celsius, kelvin

    elif unit == 'k':
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return celsius, fahrenheit

    else:
        return None


value = float(input("Enter temperature value: "))
unit = input("Enter unit (C/F/K): ")

result = convert_temperature(value, unit)

if result is None:
    print("Invalid unit!")
else:
    if unit.lower() == 'c':
        print(f"Fahrenheit: {result[0]:.2f}")
        print(f"Kelvin: {result[1]:.2f}")

    elif unit.lower() == 'f':
        print(f"Celsius: {result[0]:.2f}")
        print(f"Kelvin: {result[1]:.2f}")

    else:
        print(f"Celsius: {result[0]:.2f}")
        print(f"Fahrenheit: {result[1]:.2f}")
