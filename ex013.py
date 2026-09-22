salario = float(input('Digite o seu sálario: \nR$'))
aumento = salario * 15 / 100
print('O sálario do funcionário que é de R${:.2f}, vai subir para R${:.2f} com aumento de 15%.'.format(salario , salario + aumento))
