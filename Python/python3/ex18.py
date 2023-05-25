qtd = float(input("Informe a quantidade de fitas: "))
v = float(input("Valor de cada fita: "))
fa = qtd/3

total = qtd / 10
total = qtd + total
total = total - (total * 0.02)

print(f"Faturamento: R${12*v*(fa)}")
print(f"Valor multas mensal: {(fa/10)*(v/10)}")
print(f"Total de fitas: {total}")