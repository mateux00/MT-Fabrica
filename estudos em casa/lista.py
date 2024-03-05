vendas =[100, 40, 130, 80, 120]

print(vendas[0]) # sempre pegar o ultimo da lista usar -1, contagem da direita pra esquerda

total_vendas = sum(vendas)
print(total_vendas)
quantidade_vendas = len(vendas)
print(quantidade_vendas)
valor_max = max(vendas)
valor_min = min(vendas)
print(valor_max, valor_min)

#saber a posicao do valor na lista 
posicao = vendas.index(130)
print(posicao)


print(vendas[:2]) # da posicao 2 ato o coemco 
print(vendas[2:]) # da posicao 2 ate o final

produtos = ["iphone", "ipad", "airpods"]
precos = [4000, 8000, 2000]

#edita um item
print("iphone" in produtos)
precos[0] = precos[0] * 1.1
print(precos)

#adciona um item
produtos.append("macbook")
precos.append(100000)
print(produtos, precos)

#remover um item
produtos.remove("macbook")
precos.pop(-1)
print(produtos, precos)

#inserir um valor
produtos.insert(1, "airpods")
print(produtos)

#contar valores
print(produtos.count("airpods"))