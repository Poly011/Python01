sal = float(input('Me diga seu salario atual: R$ '))
if sal <= 1250.00:
    novo = sal + (sal * 15 / 100)
else:
   novo =  sal + (sal * 10 / 100)
print('Seu novo salario e R${:.2f}'.format(novo))