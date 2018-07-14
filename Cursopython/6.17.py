estoque={ "tomate": [ 1000, 2.30],
          "alface": [   500, 0.45],
          "batata": [ 2001, 1.20],
          "feijão": [   100, 1.50] }
total = 0
print("Vendas:\n")
while True:
     produto = input("Nome do produto (fim para sair):")
     if produto == "fim":
        break
     if produto in estoque:
        quantidade = int(input("Quantidade:"))
        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade
            print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade,preço,custo))
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade solicitada não disponível")
     else:
        print("Nome de produto inválido")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items():
     print("Descrição: ", chave)
     print("Quantidade: ", dados[0])
     print("Preço: %6.2f\n" % dados[1])