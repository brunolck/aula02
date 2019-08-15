'''
22 - Crie a classe Imóvel, que possui um endereço e um preço.
a. crie uma classe Novo, que herda Imóvel e possui um adicional no preço. Crie
métodos de acesso e impressão deste valor adicional.
b. crie uma classe Velho, que herda Imóvel e possui um desconto no preço. Crie
métodos de acesso e impressão para este desconto.

'''

class Imovel:
    def __init__(self, preco, endereco):
        self.preco = preco
        self.endereco = endereco

    def mostrar(self):
        print(f'Preço: {self.preco} \t Endereço: {self.endereco}')

class Novo(Imovel):
    def __init__(self, preco, endereco): super().__init__(preco, endereco)

    def adicional(self, valor):
        print(f'Adional: {valor}')
        self.preco += valor


class Velho(Imovel):
    def __init__(self, preco, endereco): super().__init__(preco, endereco)

    def desconto(self, valor):
        print(f'Desconto: {valor}')
        self.preco -= valor

class Teste:
    imoveis = [Novo(100000, 'Rua Do Vento'), Velho(80000, 'Rua Das Rochas')]

    def checar_imoveis(self):
        self.imoveis[0].adicional(12000)
        self.imoveis[1].desconto(5000)

        for imov in self.imoveis:
            imov.mostrar()

teste = Teste()
teste.checar_imoveis()
