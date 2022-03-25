# Faça um Programa que verifique
# se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino,
# M - Masculino,
# Sexo Inválido.

genero = input('Digite f para o genero feminino ou m para o genero masculino: ')
if (genero == 'f'):
    print ('F - Feminino')
elif (genero == 'm'):
    print('M - Masculino')
else:
    print('Sexo Inválido')

