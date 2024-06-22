def questao5():
    vetor = []
    for i in range(10):
        valor = int(input("digite o valor: "))
        vetor.append(valor)
    pares = [valor for valor in vetor if valor % 2 == 0]
    print(f"a quantidade de pares é: {len(pares)}")
    print(f"os pares são: {pares}")

questao5()
