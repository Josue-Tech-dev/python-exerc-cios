num = int(input('Digite o número que quer analisar: \n'))

print('''Escolha uma conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

opção = int(input('Escolha uma opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
