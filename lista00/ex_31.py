'''
31 - Crie um dict com 5 nomes e profissões e remova o ultimo elemento
'''

def mostrar(dic):
    print("\n")
    for k, v in dic.items():
        print("Nome: ", k, "- Profissão: ", v)

pessoas = {"João":"Pedreiro", "Pedro": "Carpinteiro", "Lucas": "Engenheiro", "Gustavo":"Programador", "Bruno":"Pintor"}
mostrar(pessoas)
pessoas.popitem()
mostrar(pessoas)