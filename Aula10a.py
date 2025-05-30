# Condicionais

#nome = str(input('Digite seu nome: '))
#if nome == 'José':
    #print('Que nome lindo! {} '.format(nome))
#else:
    #print('Seu nome é bem normal! {}'.format(nome))
#print('Bom dia, {}'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f} '.format(m))
if m > 6.0:
    print('Sua média foi {} Parabéns! '.format(m))
else:
    print('Sua média foi {}, estude mais! '.format(m))

#print('Parabens' if m >= 6 else 'Estude mais') #Condição simplificada