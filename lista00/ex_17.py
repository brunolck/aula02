'''
17 - Cria uma lista para armazenar 5 nomes fixos. Após inserir os 5
nome da lista mostre-os no console (utilize um for).
'''

nomes = []
for i in range(5):
    nomes.append(input("Digite nome fixo:"))

for i in range(5):
    print("Nome fixo: ", nomes[i])