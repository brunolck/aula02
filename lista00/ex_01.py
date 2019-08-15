'''
1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não.
Receba os dados pela console e chame este método.
'''

#definição de classe e método
class Foo:
    def maior_idade(self, idade):
        return idade >= 18 and "Maior De Idade" or "Menor De Idade"


foo = Foo()
#entrada de dados
while(True):
    try:
        print(f'Pessoa: {foo.maior_idade(int(input("Digite Idade: ")))}')
        break
    except ValueError as e:
        print(f'Tipo de entrada inválida!{e}')


'''
1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não.
Receba os dados pela console e chame este método. (modifique este exercício para receber 5 alunos,
3 notas para cada um e calcule a média mostrando se está aprovado ou não)
'''

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.media = 0
        self.notas = []

    def mostrar(self):
        print(f'Nome: {self.nome}\tMedia: {self.media}\tNotas: {self.notas}')

numero_alunos = 5
numero_notas = 3
alunos = []

#Preencher dados do aluno
for i in range(0, numero_alunos):
    aluno = Aluno(input(f'Digite nome aluno{i+1}: '))
    for j in range(0, numero_notas):
        aluno.notas.append(float(input(f'Nota{j+1}: ')))
    alunos.append(aluno)

#calcular média
for aluno in alunos:
    for nota in aluno.notas:
        aluno.media += nota
    aluno.media /= numero_notas

#Mostrar Informações do aluno
for aluno in alunos:
    aluno.mostrar()
#Verificar se aluno está aprovado ou não
for aluno in alunos:
    print(f'Nome: {aluno.nome} \t {aluno.media >= 6.0 and "APROVADO" or "REPROVADO"}')
