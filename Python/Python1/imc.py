p = float(input("informe seu peso: "))
a = float(input("informe sua altura: "))

result = p / (a*a)

print(f"Seu IMC é: {result}")

if result < 18.5:
    print("Magreza")
elif result > 18.5 and result < 24.9:
    print("Normal")
elif result > 24.9 and result < 29.9:
    print("Obesidade")
elif result < 29.9 and result < 34.9:
    print("Obesidade grau 1")
elif result < 34.9 and result < 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")
