'''
18 - Crie uma classe animal com o método comer, este método deve  escrever na tela "o animal esta comendo".
Depois disso crie as classes cachorro, cavalo e gato e implemente o método comer de acordo com o que cada animal come.
Crie uma classe AnimalTeste e coloque os três animais dentro de uma lista de animais e chame o método comer
polimorficamente (com um for)

'''

class Animal:
    def comer(self):
        print(f'Animal está comendo')

class Cachorro(Animal):
    def comer(self):
        print(f'Cachorro está comendo ração')

class Cavalo(Animal):
    def comer(self):
        print(f'Cavalo está comendo capim')

class Gato(Animal):
    def comer(self):
        print(f'Gato está comendo rato')


class AnimalTeste:
    animais = [Cachorro(), Cavalo(), Gato()]

    def animais_comendo(self):
        for i in range(len(self.animais)):
            self.animais[i].comer()

teste = AnimalTeste()
teste.animais_comendo()