from math import hypot

co = float(input('Cateto oposto: \n'))
ca = float(input('Cateto adjacente: \n'))

hi = hypot(co, ca)

print('A hipotenusa de {} e {} é {:.2f}.'.format(co, ca, hi))
