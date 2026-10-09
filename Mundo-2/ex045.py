from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''SUAS OPÇÕES
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))

if jogador not in (0, 1, 2):
    print('Opção inválida! Escolha 0, 1 ou 2.')

else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)

    print('-=' * 15)
    print('O computador jogou {}.'.format(itens[computador]))
    print('O jogador jogou {}.'.format(itens[jogador]))
    print('-=' * 15)

    if computador == jogador:
        print('EMPATE!')

    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print('O JOGADOR VENCE!')

    else:
        print('O COMPUTADOR VENCE!')
