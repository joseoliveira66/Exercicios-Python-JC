# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo
# a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = []

while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    parar = str(input('Deseja continuar? [S/N] '))
    if parar in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>4}')
print('-=' * 15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>4.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar a nota de qual aluno? [999 interrompe]: '))
    if opc == 999:
        print('FINALIZANDO!!')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha [opc][0]} são {ficha[opc][1]}')
print('<<<VOLTE SEMPRE>>>')
