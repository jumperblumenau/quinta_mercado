def questao4():
    vetor = []
    for i in range(8):
        valor = int(input("digite o valor: "))
        vetor.append(valor)
    x = int(input("digite o valor x: "))
    y = int(input("digite o valor y: "))
    soma = vetor[x] + vetor[y]
    print("a soma de x e y é: {soma}".format(soma=soma))

questao4()