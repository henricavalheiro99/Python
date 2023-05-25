l = ""

while l == "":
    l = input("Informe uma letra: ").strip
    if(l != ""):
        l = l
    else: 
        print(l)

if(l not in 'abcdefghijklmnopqrstuvwxyz' and l not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    print("Inválido")

elif(l not in 'aeiou' and 'AEIOU'):
    print("Sua letra é consoante")
else: 
    print("Sua letra é vogal")