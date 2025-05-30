# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

#from datetime import date

#data_atual = date.today().year

soma_idade = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(1, 5):
    print('----------------------------{}ª PESSOA---------------------------------'.format(i))
    nome = str(input('Digite seu nome: ')).strip().upper()
    idade = int(input('Quantos anos você tem? '))
    sexo = str(input('Qual o seu sexo. Digite [F] para feminino e [M] para masculino: ')).strip().upper()

    # Somando as idades para calcular a média
    soma_idade += idade

    # Verificando se a pessoa é homem e se é o mais velho até o momento
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    # Verificando quantas mulheres têm menos de 20 anos
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

# Calculando a média de idades
media_idade = soma_idade / 4

# Exibindo os resultados
print('A media de idade do grupo é {} '.format(media_idade))
if nome_homem_mais_velho:
    print('O homem mais velho se chama {} e tem {} anos !'.format(nome_homem_mais_velho, idade_homem_mais_velho))
else:
    print('Não há homens no grupo !')
print('Ao todo há {} mulher(res) com menos de 20 anos no grupo! '.format(mulheres_menos_20))
