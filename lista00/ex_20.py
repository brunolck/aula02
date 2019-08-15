'''
20 - Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter  um método  aumenta_salario.
Crie duas subclasses da classe funcionário, programador  e  analista, implementando o método  nas duas subclasses.
Para o programador some ao atributo salário mais 20 e ao analista some ao salário mais 30,  mostrando na tela o valor.
Depois disso, crie uma classe de testes instanciando os objetos programador e analista e chame o método
aumenta_salario de cada um.

'''

class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    #metodo abstrato
    def aumentar_salario(self):
        pass

    def mostrar(self):
        print(f'Nome: {self.nome} \t Idade: {self.idade} \tSalario: {self.salario}')

class Programador(Funcionario):
    def __init__(self, nome, idade, salario): super().__init__(nome, idade, salario)

    def aumentar_salario(self):
        self.salario += 20

class Analista(Funcionario):
    def __init__(self, nome, idade, salario): super().__init__(nome, idade, salario)

    def aumentar_salario(self):
        self.salario += 30

class Teste:
    funcionarios = [Programador('José', 25, 3000), Analista('João', 30, 4000)]

    def info_funcionarios(self):
        for func in self.funcionarios:
            func.aumentar_salario()
            func.mostrar()

teste = Teste()
teste.info_funcionarios()