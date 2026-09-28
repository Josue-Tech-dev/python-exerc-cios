a = int(input('Primeiro número:\n'))
b = int(input('Segundo número:\n'))
c = int(input('Terceiro número:\n'))

# Verificando o menor número
menor = a

if b < menor:
    menor = b

if c < menor:
    menor = c

# Verificando o maior número
maior = a

if b > maior:
    maior = b

if c > maior:
    maior = c

print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))
