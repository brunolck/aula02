'''
Crie uma classe chamada Ingresso que possui um valor em reais e um método
imprimeValor().
a. crie uma classe VIP, que herda Ingresso e possui um valor adicional. Crie um
método que retorne o valor do ingresso VIP (com o adicional incluído).
b. crie uma classe Normal, que herda Ingresso e possui um método que imprime:
"Ingresso Normal".
c. crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos
para acessar e imprimir esta localização) e uma classe CamaroteSuperior, que é
mais cara (possui valor adicional). Esta última possui um método para retornar o
valor do ingresso. Ambas as classes herdam a classe VIPame o método  aumentaSalario de cada um.

'''

class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f'Valor ingresso: {self.valor}')

'''
a. crie uma classe VIP, que herda Ingresso e possui um valor adicional. Crie um
método que retorne o valor do ingresso VIP (com o adicional incluído).
'''
class Vip(Ingresso):
    def __init__(self, valor, valorAdicional):
        super().__init__(valor)
        self.valorAdicional = valorAdicional

    def getValor(self):
        return self.valor + self.valorAdicional

'''
b. crie uma classe Normal, que herda Ingresso e possui um método que imprime:
"Ingresso Normal".
'''

class Normal(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimeTipo(self):
        print('Ingresso Normal')

'''
c. crie uma classe CamaroteInferior (que possui a localização do ingresso e métodos
para acessar e imprimir esta localização) e uma classe CamaroteSuperior, que é
mais cara (possui valor adicional). Esta última possui um método para retornar o
valor do ingresso. Ambas as classes herdam a classe VIPame o método  aumentaSalario de cada um.

'''

class CamaroteInferior(Vip):
    def __init__(self, valor, localizacao):
        super().__init__(valor)
        self.localizacao = localizacao

    def getLocalizacao(self):
        return self.localizacao

    def imprimeLocalizacao(self):
        print(f'Localização: {self.localizacao}')

class CamaroteInferior(Vip):
    def __init__(self, valor, valorAdicional, localizacao):
        super().__init__(valor)
        self.valorAdicional = valorAdicional
        self.localizacao = localizacao

    def getLocalizacao(self):
        return self.localizacao

    def imprimeLocalizacao(self):
        print(f'Localização: {self.localizacao}')