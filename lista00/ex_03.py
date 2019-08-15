'''
3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão).
 O usuário deve informar dois números e o programa deve fazer as quatro operações.
'''

class Calculadora:

    def soma(self, num1, num2):
        return num1 + num2

    def subtracao(self, num1, num2):
        return  num1 - num2

    def multiplicacao(self, num1, num2):
        return num1 * num2

    def divisao(self, num1, num2):
        return num1 / (num2 != 0 and num2 or 1)


while(True):
    try:
        numero1 = float(input("Digite número 1: "))
        numero2 = float(input("Digite número 2: "))
        break;
    except ValueError as e:
        print(f'Entrada inválida! {e}')


calculadora = Calculadora()
print(f'soma: {numero1} + {numero2} = {calculadora.soma(numero1, numero2)}')
print(f'subtração: {numero1} - {numero2} = {calculadora.subtracao(numero1, numero2)}')
print(f'multiplicação: {numero1} * {numero2} = {calculadora.multiplicacao(numero1, numero2)}')
print(f'divisão: {numero1} / {numero2} = {calculadora.divisao(numero1, numero2)}')


'''
3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão).
O usuário deve informar dois números e o programa deve fazer as quatro operações.
(modifique para calcular tudo no mesmo método, somando 1 ao resultado de cada operação)
'''

class Calculadora:
    numero1 = 0
    numero2 = 0
    def calcular(self):
        #soma
        print(f'Soma: {self.numero1} + {self.numero2} + 1 = {self.numero1 + self.numero2 + 1}')
        #subtração
        print(f'Subtração: {self.numero1} - {self.numero2} + 1 = {self.numero1 - self.numero2 + 1}')
        #multiplicação
        print(f'Multiplicação: {self.numero1} * {self.numero2} + 1 = {(self.numero1 * self.numero2) + 1}')
        #divisão
        print(f'Divisão: {self.numero1} / {self.numero2} + 1 = {(self.numero1 / (self.numero2 != 0 and self.numero2 or 1)) + 1}')

calculadora = Calculadora()
calculadora.numero1 = float(input("Digite numero1: "))
calculadora.numero2 = float(input("Digite numero2: "))
calculadora.calcular()