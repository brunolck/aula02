'''
32 - Lançar nota final para 3 alunos, deve ser possível adicionar, atualizar e deletar.
Apresente o resultado somente a nota de cada aluno ao final das operações.

'''

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def mostrar(self):
        print(f'Aluno: {self.nome} \tNotas: {self.notas}')

alunos = []
def cadastrar_alunos():
    for i in range(3):
        alunos.append(Aluno(input("Digite nome aluno: ")))

def cadastrar_notas():
    for a in alunos:
        a.notas.append(float(input("Cadastrar nota aluno({0}): ".format(a.nome))))

def alterar_notas():
    for a in alunos:
        for i in range(len(a.notas)):
            a.notas[i] = (float(input("Alterar notas aluno({0}) nota({1}): ".format(a.nome, a.notas[i]))))

def deletar_notas():
    for a in alunos:
        for i in range(len(a.notas)):
            op = (input("Deletar notas aluno({0}) nota({1})<s/n>?: ".format(a.nome, a.notas[i])))
            if(op.lower() == 's'):
                a.notas.pop(i)

cadastrar_alunos()
cadastrar_notas()
alterar_notas()
deletar_notas()

for a in alunos:
    a.mostrar()