'''
12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.
'''

numero1 = 0
numero2 = 0
while(numero1 == numero2):
    numero1 = float(input("Digite numero1: "))
    numero2 = float(input("Digite numero2: "))
    print(numero1 == numero2 and "Números Inválidos: números iguais" or "Números Válidos")

maior = numero1 > numero2 and numero1 or numero2

print(f'Maior: {numero1 > numero2 and "numero1" or "numero2"} \t{maior}')