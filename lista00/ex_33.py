'''
33 - Incremente o exercício anterior para receber 3 notas para cada aluno, onde deve ser possível efetuar as
operações de adicionar, atualizar e deletar e mostre a média. (se possível você pode aproveitar exercícios anteriores)

'''

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.media = 0
        self.notas = []

    def mostrar(self):
        print(f'Aluno: {self.nome} \tNotas: {self.notas}\tMédia: {self.media}')

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
            op = (input(f'Alterar notas aluno({a.nome}) nota({a.notas[i]})<s/n>?: '))
            if (op == "s"):
                a.notas[i] = (float(input(f'Alterar notas aluno({a.nome}) nota({ a.notas[i]}): ')))

def deletar_notas():
    for a in alunos:
        for i in range(len(a.notas)):
            op = (input(f'Deletar notas aluno({a.nome}) nota({a.notas[i]})<s/n>?: '))
            if(op == "s"):
                del a.notas[i]

def calcular_media():
    for a in alunos:
        a.media = sum(a.notas)/len(a.notas)

cadastrar_alunos()
print("\n")
cadastrar_notas()
cadastrar_notas()
cadastrar_notas()
print("\n")
alterar_notas()
print("\n")
deletar_notas()
calcular_media()

for a in alunos:
    a.mostrar()