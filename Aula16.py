# Tuplas entre [] são imutáveis posso usar for c in variável. Várias formas de usar o for
from operator import index

#lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
#print(lanche[1])
#print(lanche[-4])
#print(lanche[1:3])

#for comida in range(0,4): funciona mas traz a numeração
#for cont in range(0, len(lanche)):
    #print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#for pos, comida in enumerate(lanche):
    #print(f'Vou comer {comida} na posição {pos}')

#for comida in lanche:
    #print(f'Eu vou comer {comida}')

#print(sorted(lanche)) # sorted traz a tupla em ordem alfabética rigorosa pela primeira letra da palavra
#print('Comi pra caramba!!')

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
#print(c)
print(d)
print(f'A tupla D tem {len(d)} elementos' )
print(f'O número 8 aparece {d.count(8)} vezes. ')
print(f'O número 5 está na posição {d.index(5)}')'''

pessoa = ('José', 58, 'anos', 57, 'kilos')
#del(pessoa) podemos apagar a tupla
print(pessoa) # posso ter vários tipos de dados numa mesma tupla
