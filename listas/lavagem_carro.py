import time

fatura = 0
x = 0
lista = []


def menu():
    print('-' * 30)
    print(f'{"Escolha a opção":^30}')
    print('-' * 30)
    print(f'Placas de carros {lista}\n')
    print('''[1] Cadastrar Carro
[2] Lavagem Simples
[3] Lavagem Completa
[4] Passar Cera
[5] Lavagem Interna
[6] Sair do Programa''')
    opcao = int(input("\nOpção: "))
    return opcao


while (True):
    opcao = menu()
    if (opcao == 1):
        car = input('Digite a placa do carro: ')
        lista.append(car.upper())
    elif (opcao == 2):
        print('Lavagem Simples Valor de R$35,00')
        print('')
        mais = int(input('''Mais Alguma Coisa:\n[1] Sim\n[2] Não \n'''))
        if (mais == 1):

            print('''[1] Passar Cera\n[2] Lavagem Interna\n[3] Fazer os dois''')
            opcao2 = int(input('\nQual deseja fazer a mais: '))
            if (opcao2 == 1):
                print('\nFoi adicionar na sua conta Passagem de Cera no valor de R$15,00\n')
                print('Total da sua conta foi: R$50,00')
                time.sleep(2)
                fatura = fatura + 50
                lista.pop(0)

            elif (opcao2 == 2):
                print('\nFoi adicionado na sua conta Limpeza Interna no valor de R$20,00\n')
                print('Total da sua conta foi: R$55,00')
                time.sleep(2)
                fatura = fatura + 55
                lista.pop(0)

            else:
                print(
                    '\nFoi adicionado na sua conta Limpeza Interna e Passagem de cera no valor de R$20,00 e R$15,00\n')
                print('Total da sua conta foi: R$55,00')
                time.sleep(2)
                fatura = fatura + 55
                lista.pop(0)

        else:
            print('Só tem a limpeza Simples no valor de R$35,00')
            fatura = fatura + 35
            lista.pop(0)
            time.sleep(2)

    elif (opcao == 3):
        print('Lavagem Completa Valor de R$45,00')
        print('')
        mais = int(input('''Mais Alguma Coisa:\n[1] Sim\n[2] Não \n'''))
        if (mais == 1):

            print('''[1] Passar Cera\n[2] Lavagem Interna\n''')

            opcao2 = int(input('\nQual deseja fazer a mais: '))
            if (opcao2 == 1):
                print('\nFoi adicionar na sua conta Passagem de Cera no valor de R$15,00\n')
                print('Total da sua conta foi: R$60,00')
                time.sleep(2)
                fatura = fatura + 60
                lista.pop(0)
            else:
                print('\nFoi adicionado na sua conta Limpeza Interna no valor de R$20,00\n')
                print('Total da sua conta foi: R$55,00')
                time.sleep(2)
                fatura = fatura + 55
                lista.pop(0)
        else:
            print('Só tem a limpeza Completa no valor de R$45,00')
            fatura = fatura + 45
            lista.pop(0)
            time.sleep(2)

    elif (opcao == 4):
        print('\nFoi adicionar na sua conta Passagem de Cera no valor de R$15,00\n')
        print('Total da sua conta foi: R$15,00')
        time.sleep(2)
        fatura = fatura + 15
        lista.pop(0)

    elif (opcao == 5):
        print('\nFoi adicionado na sua conta Limpeza Interna no valor de R$20,00\n')
        print('Total da sua conta foi: R$20,00')
        time.sleep(2)
        fatura = fatura + 20
        lista.pop(0)
    else:
        print('-' * 30)
        print(f'Total do faturamento do dia foi R${fatura}')
        print('-' * 30)
        break
