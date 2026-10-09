print('{:=^40}'.format('CONCENTRA'))

preço = float(input('Preço das compras: \nMT '))

print('''FORMAS DE PAGAMENTO
[1] À vista em dinheiro/cheque
[2] À vista no cartão
[3] Em 2x no cartão
[4] Em 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 10 / 100)
    print('Pagamento à vista com 10% de desconto.')

elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('Pagamento no cartão com 5% de desconto.')

elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de MT {:.2f} sem juros.'.format(parcela))

elif opção == 4:
    totparc = int(input('Quantas parcelas? '))

    if totparc >= 3:
        total = preço + (preço * 20 / 100)
        parcela = total / totparc
        print('Sua compra será parcelada em {}x de MT {:.2f} com juros.'.format(totparc, parcela))
    else:
        total = None
        print('Erro: escolha pelo menos 3 parcelas.')

else:
    total = None
    print('Opção de pagamento inválida.')

if total is not None:
    print('Sua compra de MT {:.2f} vai custar MT {:.2f} no final.'.format(preço, total))
