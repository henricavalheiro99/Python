# Criei as listas com cada um
produtos = ["Tomate", "Batata", "Limão"]
estoque = [100, 200, 50]
estoquemin = [10, 20, 5]
# O for percorre a lista e printa as informações
for i in range(0, len(produtos)):
    print(f"A quantidade de {produtos[i]} é {estoque[i]} e o estoque mínimo é {estoquemin[i]}")
# Cria as variáveis que contém inputs
prod = input("Informe o nome do produto: ")
qtd = input("Informe a quantidade desse produto: ")
min = input("Informe o estoque mínimo desse produto: ")
# Salva o valor adicionado pelo usuário nas listas
produtos.append(prod)
estoque.append(qtd)
estoquemin.append(min)
# Percorre as listas e printa aqueles que estão com estoque mínimo
for num in range(0, len(produtos)):
    if estoque[num] <= estoquemin[num]:
        print(f"{produtos[num]} com quantidade mínima")
# Printa uma nova lista contendo as informações separadamente
# No caso isso condiz com a criação de uma matriz
lista = []
for num in range(len(produtos)):
    lista.append([produtos[num], estoque[num], estoquemin[num]])
# Elimina um produto da lista
while True:
    busca = input("Informe o nome do produto que você quer remover: ")
    if busca in produtos:
        break
    else:
        print("Produto não encontrado")
ind = produtos.index(busca)
produtos.remove(busca)
estoque.remove(estoque[ind])
estoquemin.remove(estoquemin[ind])
print(produtos, estoque, estoquemin)
# Escolha de produto para a comprar
pedidos = []
while True:
    pedprod = input("Informe o produto que deseja comprar: ")
    pedqtd = int(input("Informe a quantidade de produtos: "))
    pedidos.append([pedprod, pedqtd])
    repete = input("Deseja continuar S/N: ")
    if repete.upper() == "N":
        break
print(pedidos)
# Comparando as duas listas para descobrir se tal produto está à venda
for itens in pedidos:
    if itens[0] not in produtos:
        print(f"Produto {itens[0]} não está à venda")
    elif itens[1] < estoque[produtos.index(itens[0])]:
        print("Saldo insuficiente")
