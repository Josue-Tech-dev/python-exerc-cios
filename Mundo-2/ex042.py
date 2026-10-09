r1 = float(input('Primeiro segmento: \n'))
r2 = float(input('Segundo segmento: \n'))
r3 = float(input('Terceiro segmento: \n'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')

    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima não podem formar um triângulo.')
