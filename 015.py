dias = int(input('Quantos dias com o carro?'))
km = float(input('Quantos km com o carro?'))
pago = (dias * 60) + (km * 0.15)
print('O total a ser pago e R${:.2f}'.format(pago))