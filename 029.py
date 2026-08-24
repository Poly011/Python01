vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! voce exedeu o limite permitido que e de 80km/h')
    multa = (vel - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia e dirija com seguranca!')