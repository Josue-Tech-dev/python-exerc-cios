salário = float(input('Qual é o salário do funcionário? R$:\n'))

if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)

print('O funcionário que ganhava R$ {:.2f}, passa a ganhar R$ {:.2f}.'.format(salário, novo))
