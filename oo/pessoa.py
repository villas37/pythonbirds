class pessoa:
    def __init__(self, nome= None, idade= 37):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = pessoa('Nome Renata')
    print(pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'villas'
    print('Nome',p.nome)
    print('Idade',p.idade)


