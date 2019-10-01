class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=57):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        """

        :rtype: str
        """
        return f'Olá, meu nome é {self.nome}'

    def dander_dict(self):
        print(self.__dict__)
        print(self.__dict__.items())
        print(self.__dict__.__repr__())
        print(self.__dict__.values())
        print(id(self))

    @staticmethod
    def metodo_estatico():
        return 2019

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return '{cls} - olhos {cls.olhos}'


class Pai(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Bom dia meus filhos!'


class Filho(Pessoa):
    pass


if __name__ == '__main__':
    dav = Filho(nome='dav', idade=18)
    lis = Pessoa(nome='lis', idade=19)
    pol = Pessoa(nome='pol', idade=28)
    ben = Pai(dav, lis, pol, nome='ben')
    print(ben.cumprimentar())
    print(dav.cumprimentar())
    print(lis.cumprimentar())
    print(pol.cumprimentar())

    for f in ben.filhos:
        print(f.nome)

    # ben.sobrenome = 'cohen'
    # ben.olhos = 3
    # ben.dander_dict()
    # dav.dander_dict()
    # lis.dander_dict()
    # pol.dander_dict()
    # print(ben.nome_e_atributos_de_classe(),dav.metodo_estatico())
