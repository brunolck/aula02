'''
9 - faça um método que receba um número X e uma palavra no console e repita x vezes a essa frase.

'''

while(True):
    try:
        tamanho = int(input("Digite um número <inteiro>: "))
        break
    except ValueError as e:
        print(e)

palavra = input("Digite uma palavra: ")
for i in range(tamanho):
    print(f'{palavra}({i+1})')