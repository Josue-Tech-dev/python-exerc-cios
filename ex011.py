largura = float(input('Digite a largura: \n'))
altura = float(input('Digite a altura: \n'))

area = largura * altura

print('Sua parede tem a dimensão {} × {} e sua área é de {}m².'.format(
    largura, altura, area
))

# Cada litro (L) de tinta pinta uma área de 2m²

tinta_necessaria = area / 2

print('Para pintar essa parede você precisará de {}L de tinta.'.format(
    tinta_necessaria
))
