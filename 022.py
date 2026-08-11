nome = str(input('Digite seu nome completo: ')).strip()
print('Analizando o seu nome...')
print('Seu nome em maiusculas e {}'.format(nome.upper()))
print('Seu nome em minusculas e {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
'''separa = nome.split()
print('Seu Primeiro tem {} letras'.format(separa[0], len(separa[0])))'''