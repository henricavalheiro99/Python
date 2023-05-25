n = ""

while n == "":
    n = input("Informe um número: ")
    if(n != ""):
        n = float(n)
    else: 
        print(n)

if(n > 0):
    print("Seu número é positivo")
elif(n == 0):
    print("Seu núemro é 0")
else: 
    print("Seu número é negativo")