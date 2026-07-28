largura = float(input('Qual a largura da parede?'))
altura = float(input('Qual a altura da parede?'))
area = largura * altura
print('Sua parede tem a dimensao de {}x{} e sua area e de {}'.format(largura, altura, area))
tinta = area / 2
print('Para pintar a parede, vc precisa de {}l de tinta'.format(tinta))