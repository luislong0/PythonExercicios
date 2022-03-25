# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário
# , mostrando uma mensagem de erro e voltando a pedir as informações.

nome1 = input('Cadastre seu nome: ')
senha1 = input('Cadastre sua senha: ')

nome2 = input('Informe seu nome: ')
senha2 = input('Informe sua senha: ')

while (nome1 != nome2 and senha1 != senha2):
        if (nome1 != nome2 and senha1 != senha2):
            print('Erro, tente novamente')
            nome2 = input('Informe seu nome: ')
            senha2 = input('Informe sua senha: ')

print()
print('Logado com sucesso')