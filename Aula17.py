# Listas

'''num = [2, 5, 9, 1]
num[0] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
#num.pop() # elimina o ultimo elemento (2)
num.pop(2) # elimina na posição solicitada
if 2 in num:
    num.remove(2) # elimina o primeiro elemento caso exixtam iguais
else:
    print('O número não existe.')
print(num)
print(f'Esta lista tem {len(num)} elementos')'''

#valores = list()

'''valores.append(9)
valores.append(3)
valores.append(6)'''

#print(valores)

'''for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v} !')
print('Cheguei ao final da lista!!')'''

a = [2, 3, 4, 7]
#b = a # Cria uma ligação
b = a[:]
b[2] = 8
print(f'Lista A: {a} ')
print(f'Lista B: {b} ')
