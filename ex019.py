from random import choice

n1 = input('Primeiro aluno: \n')
n2 = input('Segundo aluno: \n')
n3 = input('Terceiro aluno: \n')
n4 = input('Quarto aluno: \n')

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O aluno escolhido foi {}.'.format(escolhido))
