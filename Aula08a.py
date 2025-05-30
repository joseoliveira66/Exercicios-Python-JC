# Importação da biblioteca geral
import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))

# Importação da biblioteca por módulo
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é {:.2f}'.format(num, floor(raiz)))