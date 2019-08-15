'''
26 - Faça um programa que receba duas listas e retorne True se são iguais ou False caso contrário, além do
número de ocorrências do primeiro elemento da lista.
'''

import random
numeros1 = [random.randint(0, 100) for a in range(10)]
numeros2 = [random.randint(0, 100) for a in range(10)]

print("numeros1: ", numeros1)
print("numeros2: ", numeros2)

print(numeros1 == numeros2 and "LISTAS IGUAIS" or "LISTAS DIFERENTES")
print(f'OCORRÊNCIA({numeros1[0]}) = {numeros1.count(numeros1[0])}')