
'''
2 - Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo,
e mostre-o por extenso. Este número deverá variar entre 1 e 5. Se o usuário introduzir um
número que não pertença a este intervalo, mostre a frase “número inválido”.
'''

numero_extenso = ["um", "dois", "tres", "quatro", "cinco"]

numero = 0
while(numero < 1 or numero > 5):
    numero = int(input("Digite número <1 a 5>: "))
    print((numero < 1 or numero > 5) and "Número Inválido" or "Número Válido")

print(f'Número digitado: {numero_extenso[numero-1]}')



