# Ler o nome de quatro alunos e criar uma lista sequancial aleatoria

from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A sequência para apresentação do trabalho será {}'.format(alunos))
