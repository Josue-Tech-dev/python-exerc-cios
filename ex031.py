distância = float(input('Qual distância quer percorrer em km?\n'))

print('Você está prestes a começar uma viagem de {} km.'.format(distância))

if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45

print('O preço da sua viagem é R${:.2f}'.format(preço))
