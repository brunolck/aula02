'''
10 - receba três notas de um aluno e informe se ele passou ou reprovou
'''

notas = []
for i in range(3):
    notas.append(float(input("Digite nota: ")))
print(sum(notas)/len(notas) >= 6 and "APROVADO" or "REPROVADO")