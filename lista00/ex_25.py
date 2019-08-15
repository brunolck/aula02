'''
25 - Faça uma função que receba uma lista e exiba os elementos da última metade na frente dos elementos da primeira metade
'''

numeros = list(range(0, 10))
print("Lista Original")
print(numeros)

def foo(lista):
    print(lista[int(len(lista)/2):len(lista)] + lista[0 : int(len(lista)/2)])

print("Lista Modificada...")
foo(numeros)