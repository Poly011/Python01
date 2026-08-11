'''nu = int(input('Digite um numero: '))
n = str(nu)
print('Analizando o numero {}'.format(n))
print('Unidade: {}'.format(n[3]))
print('Dezenas: {}'.format(n[2]))
print('Centenas: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))'''

nu = int(input('Digite um numero: '))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10
print('Analisando o numero {}'.format(nu))
print('Unidade: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))