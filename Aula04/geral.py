import random


frutas = ["Maçã", "Banana", "Uva", "Laranja", "Tomate"]


fruta_lista = frutas
fruta_set = set(frutas)
fruta_tupla = tuple(frutas)
fruta_dict = {i + 1: fruta for i, fruta in enumerate(frutas)}

def gerar_dados(qtd, valormin, valormax):
    return [random.randint(valormin, valormax) for _ in range(qtd)]

numeros_aleatorios = gerar_dados(8, 1, 35)

print("Lista de frutas:", fruta_lista)
print("Conjunto de frutas:", fruta_set)
print("Tupla de frutas:", fruta_tupla)
print("Dicionário de frutas:", fruta_dict)
print("Números aleatórios:", numeros_aleatorios)
