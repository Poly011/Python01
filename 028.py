from random import randint
computador = randint(0,5)
print('_'*70)
print('Vou pensar em um numero entre 0 e 5 tente adivinhar...')
print('_'*70)
jogador = int(input('Em que numero eu pensei? '))
if jogador == computador:
    print('PARABENS! VC VENCEU')
else:
    print('GANHEI! Eu pensei no numero {} nao o {}'.format(computador, jogador))