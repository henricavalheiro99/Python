nova = []
listapar = []
listaimpar = []
somapar = 0
somaimpar = 0
while True:
    num = int(input("Insira um núemro inteiro(digite 0 para sair): "))
    if num == 0:
        break
    nova.append(num)
for x in nova:
    if x % 2 == 0:
        listapar.append(x)
        somapar+=x
    else:
        listaimpar.append(x)
        somaimpar+=x
listapar.sort()
listaimpar.sort()
print(f"Os números pares são: {listapar} e sua somatória é {somapar}")
print(f"Os números impares são: {listaimpar} e sua somatória é {somaimpar}")