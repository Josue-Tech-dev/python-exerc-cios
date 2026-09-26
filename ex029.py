velocidade = float(input('Qual é a velocidade do seu carro: \n'))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite de 80 km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma MULTA de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança.')
