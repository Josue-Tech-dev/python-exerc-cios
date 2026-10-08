casa = float(input('preço da casa: \n'))
salário = float(input('sálario do comprador: \n'))
anos = int(input('anos de  finaciamento: \n'))
prestação = casa / (anos * 12)
minímo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos , a prestação sera R$ {:.2f} por mês'.format(casa , anos , prestação))
if prestação <= minímo:
print('Emprestimo pode ser  CONCEDIDO')
else :
print('Emprestimo NEGADO')
