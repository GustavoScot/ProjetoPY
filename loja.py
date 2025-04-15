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
            print(f"{i}. {produto.todas_infos()}")

    def vender_produto(self, indice, quantidade, carrinho):
        if indice < 1 or indice > len(self.produtos):
            print("Produto inválido.")
            return

        produto = self.produtos[indice - 1]

        if quantidade > produto.pegar_quantidade():
            print("Quantidade em estoque insuficiente.")
            return

        carrinho.adicionar(produto, quantidade)
        print(f"{quantidade}x {produto.pegar_nome()} adicionado ao carrinho.")

    def aplicar_desconto_em_produto(self, indice, percentual):
        if indice < 1 or indice > len(self.produtos):
            print("Produto inválido.")
            return

        produto = self.produtos[indice - 1]
        produto.aplicar_desconto(percentual)

    def finalizar_compra(self, carrinho):
        while True:
            total = carrinho.calcular_total()
            if total == 0:
                print("Carrinho vazio. Nada para comprar.")
                return

            print(f"\nTotal da compra: R${total:.2f}")
            print("Escolha a forma de pagamento:")
            print("1. Dinheiro")
            print("2. Cartão de Crédito")
            print("3. Cartão de Débito (5% de desconto!)")
            print("4. Pix (5% de desconto!)")
            opcao = input("Opção: ")

            if opcao == "1":
                valor_pago = 0.0
                while valor_pago < total:
                    try:
                        adicional = float(input(f"Digite o valor (Falta R${total - valor_pago:.2f}): "))
                        valor_pago += adicional
                    except ValueError:
                        print("Entrada inválida. Tente novamente.")

                troco = valor_pago - total
                print(f"Pagamento aprovado! Troco: R${troco:.2f}")
                break

            elif opcao == "2":
                print("1. Efetuar pagamento no crédito")
                print("2. Voltar")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    print("Pagamento aprovado no crédito.")
                    break
                elif escolha == "2":
                    continue
                else:
                    print("Opção inválida.")
                    continue

            elif opcao == "3" or opcao == "4":
                desconto = total * 0.05
                total_com_desconto = total - desconto
                print(f"Você ganhou 5% de desconto! Novo total: R${total_com_desconto:.2f}")
                print("1. Efetuar pagamento")
                print("2. Voltar")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    print("Pagamento com desconto aprovado.")
                    break
                elif escolha == "2":
                    continue
                else:
                    print("Opção inválida.")
                    continue

            else:
                print("Opção inválida.")
                continue

        carrinho.esvaziar_carrinho()
        print("Compra finalizada com sucesso!")
