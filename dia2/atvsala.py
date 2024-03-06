class Animal():
    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor


    
    def som(self):
        pass
    
class Cachorro(Animal):
    def som(self):
        return ': AU AU !!'

class Gato(Animal):
    def som(self):
        return": MIAUUU !!"        



meu_animal = Cachorro("Loky", "Huskey", "cinza")
print(meu_animal.nome, meu_animal.raca, meu_animal.cor, meu_animal.som())


meu_animal = Gato("Garfild", "gato da rua", "laranja")
print(meu_animal.nome, meu_animal.raca, meu_animal.cor, meu_animal.som())