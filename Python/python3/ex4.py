n = int(input("Informe um valor: "))

print(f"Centena: {int(n/100)} \nDezena: {int((n/100)-int(n/100))*10} \nUnidade:  {str(float(n))[str(n).__len__()-1]}")