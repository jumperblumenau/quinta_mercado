def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

texto = input("Digite um texto: ")
num_palavras = contar_palavras(texto)
print(f"O texto tem {num_palavras} palavras.")