# Lista dentro de lista

#teste = list()
#teste.append('Gustavo')
#teste.append(40)

#galera = list()
#galera.append(teste[:])
#teste[0] = 'Maria'
#teste[1] = 22
#galera.append(teste[:])
#print(galera)

#galera =[['JOÃO', 19], ['ANA', 33], ['JOAQUIM', 13], ['MARIA', 45]]
#print(galera[0][1])
#for p in galera:
    #print(p) # geral
    #print(p[0]) # Só nomes
    #print(p[1]) # Só idade
    #print(f'{p[0]} tem {p[1]} anos de idade!')

galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 2):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]}, é maior de idade!! ')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade!! ')
        totmen += 1

print(f'Temos {totmai} de pessoa(s) maiores de idade e {totmen} pessoa(s) menores de idade')


