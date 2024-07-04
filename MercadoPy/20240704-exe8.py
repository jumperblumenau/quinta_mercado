numeros = []

for i in range(6):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)

reverso = numeros.reverse()

print(numeros)
