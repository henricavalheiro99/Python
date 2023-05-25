sm = float(input("Salário Mínimo: "))
kwh = int(input("Quantidade Quilowatts: "))

print(f"Valor do quilowatts: R${(sm*(1/7)/100):.2f}")
print(f"Valor a ser pago: R${(sm*(1/7)*kwh/100):.2f}")
print(f"Valor a ser pago com 10% de desconto: R${((sm*(1/7)*kwh/100) - ((sm*(1/7)*kwh/100)/10)):.2f}")