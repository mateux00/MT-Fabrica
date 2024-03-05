nome = input("Digite aqui seu Nome: ")
email = input("Digite agora seu email")


# 1 passo descobrir o servidor do email 
print(email.lower())
posicao = email.find("@")
servidor = email[posicao:] 
print(servidor)

# 2 passo pegar o primero nome do ususario 
posicao = nome.find(" ")
primeiro_nome = nome[ : posicao]
print(primeiro_nome)

# 3 passo contruir a mensgem de cadastro completo
mensagem = f"Usuario {primeiro_nome} cadastrado com sucesso com o email : {email}"
print(mensagem)
 
# 4 passo fazer a mensagem do enviamos o email com os cracteres privados 
primeiro_letra = email[0]
mensagem2 = f"Enviamos um link de confirmação para o email {primeiro_letra}***{servidor}"
print(mensagem2)