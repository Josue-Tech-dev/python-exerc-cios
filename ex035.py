print('=' * 40)
print('           Analisador de Triângulos')
print('=' * 40)

r1 = float(input('Primeiro segmento:\n'))
r2 = float(input('Segundo segmento:\n'))
r3 = float(input('Terceiro segmento:\n'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
