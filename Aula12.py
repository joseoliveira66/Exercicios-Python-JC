# Condição simples

'''nome = str(input('Digite seu nome: ')).strip()
if nome == 'José':
    print('Que nome bonito!')
print('Tenha um bom dia, {}!'.format(nome))'''

''''# Estrutura condicional composta
nome = str(input('Digite seu nome: ')).strip()
if nome == 'José':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))'''

# Estrutura condicional aninhada com elif
nome = str(input('Digite seu nome: ')).strip()
if nome == 'José':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ester Ivy':
    print('Que nome feminino bonito')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))


