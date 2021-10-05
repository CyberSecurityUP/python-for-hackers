class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return self.nome

joas = Pessoa('Joas')
print(joas)
michael = Pessoa('Michael')
print(michael)
lucas = Pessoa('Lucas')
print(lucas)
