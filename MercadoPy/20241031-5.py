meus_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def media_numeros(numeros):
    return sum(numeros) / len(numeros)

print(media_numeros(meus_numeros))

def desvio_padrao_numeros(numeros):
    media = media_numeros(numeros)
    return (sum([(x - media) ** 2 for x in numeros]) / len(numeros)) ** 0.5

print(desvio_padrao_numeros(meus_numeros))