# Achar o tamanho da hipotenusa sabendo quais são os valores dos catetos
#oposto e adjacente

#co = float(input('Digite o valor do cateto oposto: '))
#ca = float(input('Digite o valor do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2) #Método matemático
#print('O comprimento da hipotenusa é {:.2f}'.format(hi))

import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot (co, ca) #Método com import math
print('O comprimento da hipotenusa é {:.2f}'.format(hi))