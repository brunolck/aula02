'''
29 - Qual a diferença de lista e dicionário?
Dicionários armazenam elementos como pares chave,valor.
'''

dic = {'nome':'Felipe', 'idade':33}

#percorrendo dicionário
for key in dic:
    print(key, ": ", dic[key])

#mostrar todas as chaves
print(dic.keys())

#mostrar todos os valores
print(dic.values())

#recuperar os pares chave valor (c++ pair<key, value>)
print(dic.items(), "\n")

#outra forma de percorrer o dicionário
for key, value in dic.items():
    print(key, ": ", value)

