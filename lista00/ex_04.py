'''
4 - Faça um programa que receba um valor que é o valor pago, um segundo valor que é o
preço do produto e retorne o troco a ser dado.
'''

while(True):

    try:
        valor_pago = float(input("Digite Valor Pago: "))
        valor_produto = float(input("Digite Valor Produto: "))
        if(valor_pago < valor_produto):
            print("Valor pago precisa ser maior que valor produto!")
        else:
            break
    except ValueError as e:
        print(f'Entrada Inválida! {e}')

valor_troco = valor_pago - valor_produto
print(f'Troco: {valor_troco:.2f}')

'''
4 - Faça um programa que receba um valor que é o valor pago, um segundo valor que é o preço do produto e retorne
o troco a ser dado. (modifique para receber um valor de desconto e subtraia do valor do produto)
'''

valor_produto = float(input("Digite valor produto: "))
valor_desconto = float(input("Digite valor desconto: "))
valor_pago = float(input("Digite valor pago:"))

valor_troco = valor_pago - (valor_produto - valor_desconto)
print(f'Troco: {valor_troco}')