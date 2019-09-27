class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=57):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"Olá!!! {id(self)} {self.nome} {self.idade}"

    def __str__(self):
        return self.nome


class Homen(Pessoa):
    # def __init__(self):
    #     self.idade=35
    pass


class Mutante(Pessoa):
    olhos = 3


if __name__ == "__main__":

    dav = Homen(nome='David')
    ben = Mutante(dav, nome='ben')
    print(Pessoa.cumprimentar(ben))
    for filho in ben.filhos:
        print(filho)
    print(ben.__dict__)
    print(dav.__dict__)

    print(ben.cumprimentar())
    print(ben.olhos)
