class Produto: 
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def pegar_nome(self):
        return self.nome
        
    def pegar_preco(self):
        return self.preco
        
    def pegar_quantidade(self):
        return self.quantidade

    def todas_infos(self):
        return f'Nome:{self.nome}\nPreço:{self.preco}\nQuantidade: {self.quantidade}'
