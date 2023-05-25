def retornarPN(argumento):
    if (argumento < 0):
        print(f"{argumento} é um número negativo")
    elif (argumento == 0):
        print(f"{argumento} vale 0")
    else:
        print(f"{argumento} é um número positivo")
argumento = int(input("Digite um número: "))
print(retornarPN(argumento))