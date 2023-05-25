while True:
# Enquanto for verdade
    pergunta = input("Você gosta de python? ")
    pergunta = pergunta.upper()
    # Adaptar para funcionar qualquer resposta em maiúsculo ou minúsculo
    if pergunta == "SIM":
        print("Resposta correta!")
        break
    else:
        print("Errou")   
