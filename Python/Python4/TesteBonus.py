while True:
    n = int(input("Informe um número: "))
    a = 0
    e = 0
    for i in range(1,11):
        n1 = int(input(f"Informe o resultado de {n} x {i}: "))
        if n1 == n*i:
            print("Resposta correta")
            a +=1
        else:
            print(f"Errou, a resposta era {n*i}")
            e +=1

    print(f"Total de acertos: {a}")
    print(f"Total de erros: {e}")

    continuar = str(input("Você quer continuar?(Digite S para sim ou N para não)"))
    continuar = continuar.upper()
    if continuar != "S":
        break
        

    
