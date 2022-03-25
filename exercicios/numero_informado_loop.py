while True:
    try:
        numero = int(input("informe um numero: "))
        if not int:
            print("erro")
    except ValueError as e:
            print("Valor inválido:", e)
    else:
        break

print(numero)

