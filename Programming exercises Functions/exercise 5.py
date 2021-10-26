# convert the temperature from fahrenheit to celsius and kelvin
def convert_temp():
    temp_in_F = eval(input("Enter a temperature in Fahrenheit: "))

    def convert_to_celsius():
        return (5 / 9) * (temp_in_F - 32)

    def convert_to_kelvin():
        return convert_to_celsius() + 273.15

    print()
    print(f"The temperature in fahrenheit is: {temp_in_F}")
    print(f'The temperature in celsius is: {convert_to_celsius()}')
    print(f'The temperature in kelvin is: {convert_to_kelvin()} ')


convert_temp()
