def converter(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = converter(celsius) 
print(f"{celsius}°C is equal to {fahrenheit}°F")