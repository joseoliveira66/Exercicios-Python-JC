# Encontrar a média entre duas notas de um aluno
Aluno = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('O aluno {}, tirou {} na primeira nota e {} na segunda nota, ficando com média final de {}'.format(Aluno, n1, n2, m))