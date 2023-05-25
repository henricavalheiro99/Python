nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1+nota2+nota3) / 3

print(f"Sua média foi: {media}")

if(media >= 7):
    print("Aprovado com a média: " + str(media))
elif(media >= 3):
    print("Exame com a média: " + str(media))
else: 
    print("Reprovado com a média: " + str(media))
