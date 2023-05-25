try:
    numero = int(input("Informe um número: "))
except:
    print("Está errado")
    exit()
resultado = 0

while resultado <= 10:
    print(str(resultado) + " x " + str(numero) + " = " + str(resultado * numero))
    resultado = resultado + 1