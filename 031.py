dis = float(input('Qual e a distancia da sua viagem?'))
print('Voce vai fazer uma viagem de {}km'.format(dis))
if dis <= 200:
    preco = dis * 0.50
else:
    preco = dis * 0.45
print('E o preco da sua passagem sera de R${:.2f}'.format(preco))