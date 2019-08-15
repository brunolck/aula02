'''
13 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres (considere que as
idades dos homens serão sempre diferentes entre si, bem como as das mulheres). Calcule e
escreva a soma das idades do homem mais velho com a mulher mais nova, e o produto das idades
do homem mais novo com a mulher mais velha.
'''

idade_homem = []
idade_mulher = []

def ler_idade(lista):
    i = 0
    while(i < 2):
        idade = int(input("Digite Idade: "))
        if idade in lista:
            print("Idade Repetida")
        else:
            lista.append(idade)
            i += 1

#Ler Idades
print("Digite Idade Homens...")
ler_idade(idade_homem)
print("Digite Idade Mulheres...")
ler_idade(idade_mulher)

print(f'Soma: {max(idade_homem)} + {min(idade_mulher)} = {max(idade_homem)+min(idade_mulher)}')
print(f'Produto: {min(idade_homem)} * {max(idade_mulher)} = {min(idade_homem)*max(idade_mulher)}')
