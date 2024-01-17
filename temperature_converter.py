def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_input = float(input("Enter temperature in Celsius: "))

fahrenheit_result = celsius_to_fahrenheit(celsius_input)
 
print(f"{celsius_input} degrees Celsius is equal to {fahrenheit_result} degrees Fahrenheit.")
