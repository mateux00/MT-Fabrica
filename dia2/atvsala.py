class Animal():
    def __init__(self, nome):
        self.nome = nome


    
    def som(self):
        pass
    
class Cachorro(Animal):
    def som(self):
        return ': AU AU !!'

class Gato(Animal):
    def som(self):
        return"MIAUUU !!"        



meu_animal = Cachorro("Loky")
print(meu_animal.nome, meu_animal.som())
