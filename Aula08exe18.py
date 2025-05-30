# Ler um ângulo e calcular o seno, cosseno e tangente

import math
ang = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Para o ângulo de {}, o seno será {:.2f}, o cosseno será {:.2f} e a tangente será {:.2f}'.format(ang, seno, cos, tang))
