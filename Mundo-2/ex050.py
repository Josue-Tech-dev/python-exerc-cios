
soma = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite {} número: \n'.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1

print('\033[2;38;43mVocê informou {} números PARES e a soma foi {}'.format(cont, soma))
                    
