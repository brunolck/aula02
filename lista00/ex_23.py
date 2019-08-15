'''
23 - Crie uma programa que recebe uma lista qualquer e:
a. retorne o maior elemento
b. retorne a soma dos elementos
c. retorne o número de ocorrências do primeiro elemento da lista
d. retorne a média dos elementos

'''

import random

numeros = []
for i in range(10):
    numeros.append(random.randint(0, 100))
print(numeros)
print(f'Maior: {max(numeros)} \tSoma: {sum(numeros)} \t Ocorrência({numeros[0]}):{numeros.count(numeros[0])} \t Média: {sum(numeros)/len(numeros)}')