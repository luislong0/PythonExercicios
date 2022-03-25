clientes = []

for i in range(3):
    cliente = str(input('Digite o nome do cliente: '))
    clientes.append(cliente)

cli = str(input('Digite o nome do cliente 1: '))
print (clientes)
if (cli in clientes):
    print (cli)


