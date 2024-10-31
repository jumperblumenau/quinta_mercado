def numero_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Digite um número: "))
if numero_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")

