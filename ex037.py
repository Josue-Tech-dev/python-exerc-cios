num = int(input('Digite o número que quer análisar: \n'))
print('''Escolhe uma conversão
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''' )
opção = int(input('Escolhe uma opção'))
if opção == 1:
print('{} convertido para  BINARIO é {}'.format(num , bin(num)[2:]))
elif opção ==2:
print('{} convertido para OCTAL é {}'.format(num , oct(num)[2:]))
elif opção ==3:
print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
print('Opção inválida .Tente novamente')
