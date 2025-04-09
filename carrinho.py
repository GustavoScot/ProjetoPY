from produto import *

class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto: Produto, quantidade: int):
        if quantidade <= produto.quantidade:
            item = Produto(produto.nome, produto.preco, quantidade)
            self.produtos.append(item)
            produto.quantidade -= quantidade
            print(f'{quantidade}x {produto.nome} adicionado ao carrinho!')
        else:
            print('Estoque insuficiente!')
            
    def calcular_total(self):
        return sum(produto.preco * produto.quantidade for produto in self.produtos)

    def esvaziar_carrinho(self):
        self.produtos.clear()

    def mostrar_carrinho(self):
        if not self.produtos:
            print('O carrinho está vazio!')
        else:
            print('Produtos no carrinho:')
            for produto in self.produtos:
                print(produto.todas_infos())
            print(f'\nTotal: R${self.calcular_total():.2f}')
