#nome = str(input('Qual é o seu nome: '))
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um número: '))
n2 = int(input('Outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d1 = n1 // n2
e = n1 ** n2
print('A soma é: {},\no produto é: {} e a divisão é: {:.2f} '.format(s, m, d), end = '')
print('A divisão inteira é: {} e a exponenciação é: {}'.format(d1, e))
