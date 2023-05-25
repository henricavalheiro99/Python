n = int(input("Digite um numero de 3 digitos: "))
inverso = int(str(n)[::-1])
dv = n+inverso
dv = int(dv/100) + int(((dv/100)-int(dv/100))*10)*2 + int(str(float(dv))[str(dv).__len__()-1])*3
dv = int((str(dv)[str(dv).__len__()-1]))
print(f"Digito Verificador: {dv}")



