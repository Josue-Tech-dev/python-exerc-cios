from random import shuffle

n1 = str(input('Primeiro aluno: \n'))
n2 = str(input('Segundo aluno: \n'))
n3 = str(input('Terceiro aluno: \n'))
n4 = str(input('Quarto aluno: \n'))

lista = [n1, n2, n3, n4]

shuffle(lista)

print('A ordem de apresentação será:')
print(lista)
