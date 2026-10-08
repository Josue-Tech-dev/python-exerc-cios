from datetime import date

actual = date.today().year
ano = int(input('Ano de nascimento: \n'))
idade = actual - ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, actual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento.'.format(saldo))
    ano = actual + saldo
    print('O seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = actual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
