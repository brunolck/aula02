'''
5 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo), se é par ou ímpar
'''

while(True):
    try:
        numero = int(input("Digite um número <inteiro>: "))
        mensagem = (numero >= 0 and "POSITIVO" or "NEGATIVO") + "\t" + (numero % 2 == 0 and "PAR" or "IMPAR")
        print(mensagem)
        break
    except ValueError as e:
        print(f'Valor Inválido! {e}')

