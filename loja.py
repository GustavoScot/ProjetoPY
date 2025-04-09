from produto import *
from carrinho import *

class Loja:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def exibir_produtos(self):
        if not self.produtos:
            print("Nenhum produto disponível.")
            return

        print("\nProdutos disponíveis:")
        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i}. {produto.pegar_nome()} - R${produto.pegar_preco():.2f} - Estoque: {produto.pegar_quantidade()}")

    def vender_produto(self, indice, quantidade, carrinho):
        if indice < 1 or indice > len(self.produtos):
            print("Produto inválido.")
            return

        produto = self.produtos[indice - 1]

        if quantidade > produto.pegar_quantidade():
            print("Quantidade em estoque insuficiente.")
            return

        carrinho.adicionar_produto(produto, quantidade)
        produto.quantidade -= quantidade
        print(f"{quantidade}x {produto.pegar_nome()} adicionado ao carrinho.")

    def finalizar_compra(self, carrinho):
        total = carrinho.calcular_total()
        if total == 0:
            print("Carrinho vazio. Nada para comprar.")
            return

        print(f"\nTotal da compra: R${total:.2f}")
        print("Pagamento realizado com sucesso! Obrigado pela compra.")
        carrinho.esvaziar()
