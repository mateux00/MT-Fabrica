#loop com while

lista = ["ç", "~", "´", "^", "ã", "õ", "ê"]

while True:
    name = input("escreva seu nome sem usar caracteres epeciais: ")
    validarNome = True   
    for letra in name:
       if letra in lista:
           print("você utilizou caracteres invalidas ")
           validarNome = False
           break
       
    if validarNome:
       print("nome registrado")
    




#contador em while mias facil


# count = 0

# digito = int(input("digite quantos numeros você quer contar: "))
# while count <= digito:
#     print(count)
#     count += 1



