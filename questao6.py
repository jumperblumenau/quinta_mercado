def questao6():
    vetor = []
    for i in range(10):
        valor = int(input("digite o valor: "))
        vetor.append(valor)

    maior = max(vetor)
    menor = min(vetor)
    print(f"o maior valor é: {maior} ")
    print(f"e o menor valor é: {menor} ")


questao6()