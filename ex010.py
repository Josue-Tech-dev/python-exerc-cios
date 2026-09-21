dinheiro = float(input('Quanto dinheiro você tem? \nR$'))
dolar = 3.27
conversao = dinheiro / dolar

print('Com R${} você pode comprar US${:.2f}.'.format(dinheiro, conversao))
