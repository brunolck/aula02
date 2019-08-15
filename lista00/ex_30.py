'''
30 - Crie um dict com 5 nomes e idades, crie um segundo dict duplicando os itens.

'''

def mostrar(dic):
    print("\n")
    for k, v in dic.items():
        print("Nome: ", k, "- Idade: ", v)

pessoas = {"João":25, "Pedro": 27, "Lucas": 32, "Felipe":33, "Bruno":37}
mostrar(pessoas)
pessoas_copia = pessoas.copy()
mostrar(pessoas_copia)

