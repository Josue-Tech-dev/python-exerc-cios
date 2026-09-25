nome = str(input('Digite o seu nome completo: \n'))

print('Analisando o seu nome...')

print('O seu nome em maiúsculas é {}.'.format(nome.upper()))
print('O seu nome em minúsculas é {}.'.format(nome.lower()))

print('O seu nome ao todo tem {} letras.'.format(
    len(nome) - nome.count(' ')
))

separa = nome.split()

print('Seu primeiro nome é {} e ele tem {} letras.'.format(
    separa[0],
    len(separa[0])
))
