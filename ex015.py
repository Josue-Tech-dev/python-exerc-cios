dias = int(input('Por quantos dias o carro foi alugado: \n'))
km = float(input('Quantos km o carro rodou: \n'))

custo_dias = dias * 60
custo_km = km * 0.15

print('O carro foi alugado por {} dias e percorreu {:.1f} km.'
      ' O preço a pagar é R${:.2f}.'.format(
          dias, km, custo_dias + custo_km
      ))
