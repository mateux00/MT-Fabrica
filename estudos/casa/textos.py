faturamento = 1000
custo = 700

lucro = faturamento - custo

print(F"Faturamento: {faturamento} Custo: {custo} Lucro: {lucro} ")
#as duas maneiras de fazer
print("Faturamento: " + str(faturamento) + ", Custo: " + str(custo) + ", Lucro: " + str(lucro))

email = "EMAILtexte@gmail.com"

print(email.lower())
print(email.find("@")) #dentro do find esta a caractere que estmos procurando 

posicao = email.find("@")
servidor = email[posicao+1:] #os 2 pontos pega tudo dps da caractere desejada
# o mais 1 sendo usado pra pegar o caractere dps do @
print(servidor)


#como pegar o tamanho de um texto ( quantidade de caracteres)
tamanho = len(email)
print(tamanho)

#trocar uma parte do texto
email_trocado = email.replace("gmail.com","hotmail.com")
print(email_trocado.lower())


#editar o nome (exemplo as letras inicias minusculas)
nome = "mateus carvalho"
print(nome.capitalize()) #deixa a 1 letra do texto maiuscula
print(nome.title()) #deixa todas as 1 letras do texto maiuscula

#casos especiais de formatacao de texto
print(F"Faturamento: R${faturamento:,.2f}\nCusto: {custo}\nLucro: {lucro}\n ")     
#so fazer essa formatacao no final por que se nao a variavel vira texto e formata
