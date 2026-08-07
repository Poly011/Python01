'''import math
op = float(input('Comprimento do cateto oposto:'))
ad = float(input('Comprimento do cateto adjacente:'))
hip = math.sqrt((op ** 2) + (ad ** 2))
print('A hipotenusa vai medir {:.2f}'.format(hip))'''

from math import hypot
op = float(input('Comprimento do cateto oposto:'))
ad = float(input('Comprimento do cateto adjacente:'))
hip = hypot(op, ad)
print('A hipotenusa vai medir {:.2f}'.format(hip))