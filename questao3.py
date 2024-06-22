def questao3():
    vetor = []
    vetor_quadrado = []
    for i in range(10):
        numero = float(input("Digite o valor real {i=1}: "))
        vetor.append(numero)
        quadrado = numero ** 2
        vetor_quadrado.append(quadrado)

    print(vetor)
    print(vetor_quadrado)

questao3()