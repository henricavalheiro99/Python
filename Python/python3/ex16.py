v = float(input("Valor: "))
ta = float(input("Taxa: "))
te = float(input("Tempo: "))

print(f"Prestação: {v+(v*(ta/100)*te)}")
