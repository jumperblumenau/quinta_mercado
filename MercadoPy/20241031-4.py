def gerar_senha(tamanho):
    import string
    import random
    tamanho >= 8 and tamanho <= 16
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

print(gerar_senha(10))