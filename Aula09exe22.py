# Ler um nome e apresentar com todas as letras maiusculas e minusculas.
# quantas letras sem considerar espaços e quantas letras do primeiro nome

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em letras maiúsculas é {} : '.format(nome.upper()))
print('Seu nome em letras minúsculas é {} : '.format(nome.lower()))
print('Quantidade de letras sem espaços {} '.format(len(nome) - nome.count(' ')))
#print('A quantidade de letras do seu primeiro nome é {}: '.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))
