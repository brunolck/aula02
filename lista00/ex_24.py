'''
24 - Receba duas listas e exiba a união destas listas e a intercalação destas listas, isto é,
1º da 1ª lista, 1º da 2ª lista, 2º da 1ª lista, 2º da 2ª lista.
'''

numeros1 = list(range(0, 10, 1))
numeros2 = list(range(20, 30, 1))

print("Lista Originais...")
print(numeros1)
print(numeros2)

print("Junção Das Listas...")
print(numeros1 + numeros2)

numeros3 = []
for a, b in zip(numeros1, numeros2):
    numeros3.append(a)
    numeros3.append(b)

print("Listas Intercaladas")
print(numeros3)
