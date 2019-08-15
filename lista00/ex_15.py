'''
15 - Ler 10 valores (considere que não serão lidos valores iguais) e escrever o maior deles.
'''

i = 0
numeros = []
while(i < 10):
    numero = float(input("Digite numero: "))
    if(numero in numeros):
        print("Número Repetido! Digite Novamente...")
    else:
        numeros.append(numero)
        i += 1
print(f'Maior Número: {max(numeros)}')

