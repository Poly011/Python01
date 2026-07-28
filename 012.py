preco = float(input('Qual o preco do produto? R$'))
desc =  preco - (preco * 0.05)
print('O produto que custava R${}, com 5% de desconto fica R${}'.format(preco, desc))