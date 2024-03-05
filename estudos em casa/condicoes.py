#faturamento = 1000
#custo =1800

#lucro = faturamento - custo

#if lucro >= 0:
    #print("Lcuro foi de ", lucro)
    
#else:
    #print("o prejuíozo foi de: ", custo)
    
    
    
#produtos = ["iphone", "ipad", "airpods"]
#novo_produto = input("Digite o produto que quer adicionar: ")
#novo_produto = novo_produto.lower()
    
#if novo_produto in produtos:
#    print("produto ja cadastrado ")
    
    
#else:
#    print("produto adicionado com sucesso")    
#    produtos.append(novo_produto)
        
#print(produtos)        


vendas = 20000

if vendas > 15000:
    bonus = 500

    
elif vendas > 10000:
    bonus = 150
    
    
elif vendas > 5000:
    bonus = 50
    

else:
    bonus = 0    


    
print("Bonus foi de: ", bonus)    

 
            