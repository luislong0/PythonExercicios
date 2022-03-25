genero = input('digite seu genero *f ou *m : ')
feminino = 'f'
masculino = 'm'
pesoideal = 0
altura = float(input('digite sua altura : '))


if genero == feminino:
    pesoideal = (62.1*altura) - 44.7
    print('seu peso ideal é',  '{:.2f}'.format(pesoideal))
else:
    pesoideal = (72.7*altura) - 58
    print('seu peso ideal é',  '{:.2f}'.format(pesoideal))



