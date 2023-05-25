n = ""

while n == "":
    n = input("informe um valor: ").strip()
    if(n != "" or n in '0123456789'):
        n = float(n)
    else: 
        print("Inválido")



if(n > 0 ):
    print("Positivo")
elif (n < 0): 
    print("Negativo")
else:
    print("Zero")