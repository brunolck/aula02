'''
7 - Escreva um algoritmo que leia 10 números informados pelo usuário e, depois, informe o menor, número,
o maior número, a soma dos números informados e a média aritmética dos números informados.
'''

length = 10
numeros = []
for i in range(length):
    numeros.append(float(input("Digite um número: ")))

print(f'Menor: {min(numeros)} \tMaior: {max(numeros)} \tSoma: {sum(numeros)} \tMédia: {sum(numeros)/len(numeros)}')