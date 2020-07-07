class pessoa:
    def __init__(self, *filhos, nome= None, idade= 37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    Renata = pessoa(nome='Renata')
    Villas = pessoa(Renata, nome='Villas')
    print(pessoa.cumprimentar(Renata))
    print(id(Villas))
    print(Renata.cumprimentar())
    print('Nome', Renata.nome)
    print('Idade', Renata.idade)
    for filho in Renata.filhos:
        print( filho.filhos)
    Renata.sobrenome = 'Guarnelli'
    del Villas.filhos
    print(Renata.__dict__)
    print(Villas.__dict__)


