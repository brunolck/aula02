'''
28 - Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da média dos valores da lista.
Exemplo: lista = [2.5, 7.5, 10.0, 4.0] (média = 6.0). Valor mais próximo da média = 7.5

'''

import random
numeros = [random.randrange(25, 100) for a in range(10)]
print(numeros)

media = sum(numeros)/len(numeros)
print(f'Média: {media}')

#achar o valor mais próximo da média
proximo = max(numeros)
diferenca = proximo
for n in numeros:
    if(abs(n - media) < diferenca):
        diferenca = abs(n - media)
        proximo = n

print(f'próximo: {proximo}')
