produto = float(input('Digite o preço do produto: \nR$'))

desconto = produto * 5 / 100

print('Na liquidação da loja o produto de R${:.2f} está com desconto de 5%'
      '\nou seja, vai custar só R${:.2f}.'.format(produto, produto - desconto))
