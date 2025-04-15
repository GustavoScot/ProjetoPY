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

    def aplicar_desconto(self, percentual: float):
        if 0 <= percentual <= 100:
            desconto = self.preco * (percentual / 100)
            self.preco -= desconto
            print(f"Desconto de {percentual}% aplicado! Novo preço: R${self.preco:.2f}")
        else:
            print("Percentual inválido. Deve ser entre 0 e 100.")

    def todas_infos(self):
        return f'Nome: {self.nome} - Preço: R${self.preco:.2f} - Quantidade: {self.quantidade}'