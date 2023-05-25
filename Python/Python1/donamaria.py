tamanho = input("Informe o tamanho do seu ovo (digite P para pequeno, M para médio, G para grande): ")

result = 0

if tamanho == "P":
    result += 7.8 
    print(f"{result}")
elif tamanho == "M":
    result += 12.9
    print(f"{result}")
elif tamanho == "G":
    result += 23.95
    print(f"{result}")
else:
    exit

sabor = input("Informe o sabor do seu ovo (digite P para preto, B para branco, L para leite): ")

if sabor == "P":
    result += 9.67
    print(f"{result}")
elif sabor == "B":
    result += 4.5
    print(f"{result}")
elif sabor == "L":
    result += 9.32
    print(f"{result}")
else:
    exit

recheio = input("Informe o recheio do seu ovo (digite P para chocolate preto, B para chocolate branco, A para ambos): ")

if recheio == "P":
    result += 4.83
    print(f"{result}")
elif recheio == "B":
    result += 2.25
    print(f"{result}")
elif recheio == "A":
    result += 3.54
    print(f"{result}")
else:
    exit

adicionais = input("Informe se quer adicionais no seu ovo(digite K para kitkat, M para MM's, A ambos, N para não adicionar): ")

if adicionais == "K":
    result += 4.67
    print(f"{result}")
elif adicionais == "M":
    result += 5.43
    print(f"{result}")
elif adicionais == "A":
    result += 5.05
    print(f"{result}")
elif adicionais == "N":
    result = result
    print(f"{result}")
else:
    exit

presente = input("Informe se seu ovo será de presente(digite S para sim, N para não): ")

if presente == "S":
    result += 2.5
    print(f"{result}")
elif presente == "N":
    result = result
    print(f"{result}")
else:
    exit

entrega = input("Informe se seu ovo será para entrega(digite S para sim, N para não): " )

if entrega == "S":
    result += 5
    print(f"{result}")
elif entrega == "N":
    result = result
    print(f"{result}")
else:
    exit

pagamento = input("Informe a forma de pagamento do seu ovo(digite C para cartão, P para pix): ")

if pagamento == "C":
    result += 3.3
    print(f"{result}")
elif pagamento == "P":
    result = result - (result / 10)
    print(f"{result}")
else:
    exit

quantidade = float(input("informe a quantidade do seu ovo: "))

result = result * quantidade

print(f"O preço será: {result}")