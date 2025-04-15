from produto import Produto
from loja import Loja
from carrinho import Carrinho

def main():
    loja = Loja()
    carrinho = Carrinho()

    loja.adicionar_produto(Produto("Manga", 5.50, 12))
    loja.adicionar_produto(Produto("Banana", 2.90, 10))
    loja.adicionar_produto(Produto("Morango", 4.50, 11))
    loja.adicionar_produto(Produto("Ovo", 20.00, 5))
    loja.adicionar_produto(Produto("Laranja", 2.50, 20))
    loja.adicionar_produto(Produto("Limao", 1.50, 35))

    while True:
        print("\nSeja Bem-vindo!")
        print("1.Ver produtos disponíveis")
        print("2.Adicionar produto ao carrinho")
        print("3.Ver carrinho")
        print("4.Finalizar compra")
        print("5.Aplicar desconto a um produto")
        print("6.Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            loja.exibir_produtos()

        elif opcao == "2":
            loja.exibir_produtos()

            try:
                indice = int(input("Digite o número do produto que deseja adicionar: "))
                quantidade = int(input("Quantidade: "))
                loja.vender_produto(indice, quantidade, carrinho)
            except ValueError:
                print("Entrada inválida.")

        elif opcao == "3":
            carrinho.mostrar_carrinho()

        elif opcao == "4":
            loja.finalizar_compra(carrinho)

        elif opcao == "5":
            loja.exibir_produtos()

            try:
                indice = int(input("Digite o número do produto para aplicar desconto: "))
                percentual = float(input("Digite o percentual de desconto (apenas o número, sem '%'): "))
                loja.aplicar_desconto_em_produto(indice, percentual)
            except ValueError:
                print("Entrada inválida.")

        elif opcao == "6":
            print("Volte sempre!")
            break

        else:
            print("Opção inválida.")

main()