celsius = input("Digite uma temperatura em graus Celsius: ")
fahrenheit = (float(celsius) * 9 / 5) + 32
kelvin = float(celsius) + 273.15
print(f"{celsius} graus Celsius equivalem a {fahrenheit} graus Fahrenheit")
print(f"{celsius} graus Celsius equivalem a {kelvin} graus Kelvin")