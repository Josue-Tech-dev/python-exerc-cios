
n = int(input('Que número você quer a TABUADA: '))
print('{:=^40}'.format('TABUADA'))

for c in range(1, 1001):
    print('{} × {} = {}'.format(n, c, n * c))
  
