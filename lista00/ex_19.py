'''
19 - Crie uma classe chamada Bicicleta. Ela terá os seguintes métodos: quantidadeMarchas();
tipoFreio() e marca(); Crie também duas classes que estendem esta classe, uma se chamará
BicicletaPasseio e a outra BicicletaProfissional. Para ﬁnalizar crie uma classe onde deverá
estar o método main e crie uma instancia de cada tipo de bicicleta e mostre o resultado dos métodos.

'''

class Bicicleta:
    def __init__(self, quant_marchas, tipo_freio, marca):
        self.quant_marchas = quant_marchas
        self.tipo_freio = tipo_freio
        self.marca = marca

    def quantidadeMarchas(self):
        print(f'Quantidade de marchas: {self.quant_marchas}')
    def tipoFreio(self):
        print(f'Tipo de freio: {self.tipo_freio}')
    def marcaa(self):
        print(f'Marca: {self.marca}')


class BicicletaPasseio(Bicicleta):
    def __init__(self, quant_marcha, tipo_freio, marca): Bicicleta.__init__(self, quant_marcha, tipo_freio, marca)

    def quantidadeMarchas(self):
        print(f'BicicletaPasseio: Quantidade de marchas: {self.quant_marchas}')
    def tipoFreio(self):
        print(f'BicicletaPasseio: Tipo de freio: {self.tipo_freio}')
    def marcaa(self):
        print(f'BicicletaPasseio: Marca: {self.marca}')

class BicicletaProfissional(Bicicleta):
    def __init__(self, quant_marcha, tipo_freio, marca): Bicicleta.__init__(self, quant_marcha, tipo_freio, marca)

    def quantidadeMarchas(self):
        print(f'BicicletaProfissional: Quantidade de marchas: {self.quant_marchas}')
    def tipoFreio(self):
        print(f'BicicletaProfissional: Tipo de freio: {self.tipo_freio}')
    def marcaa(self):
        print(f'BicicletaProfissional: Marca: {self.marca}')


class Main:

    bicicletas = [BicicletaPasseio(18, 'Freio De Pé', 'Caloi'), BicicletaProfissional(24, 'Freio De Mão', 'GIO')]
    def main(self):
        for i in range(len(self.bicicletas)):
            self.bicicletas[i].quantidadeMarchas()
            self.bicicletas[i].tipoFreio()
            self.bicicletas[i].marcaa()


teste = Main()
teste.main()