list = [{'nome': 'João', 'idade': 25}, {'nome': 'Maria', 'idade': 30}, {'nome': 'Pedro', 'idade': 20}]

def ordenar_idade(dict):
    return dict['idade']

list.sort(key=ordenar_idade, reverse=True)
print(list)