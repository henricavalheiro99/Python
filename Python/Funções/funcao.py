valor = 100.00
def calculo():
    global valor 
    valor = valor - 10
    print(f"valor dentro da função: {valor}")
print(f"Valor da função: {valor}")
calculo()
calculo()
print(f"Valor fora da função: {valor}")