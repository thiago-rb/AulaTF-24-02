def adicionar_produto(inventario, codigo, nome, preco):
    inventario[codigo] = {"Nome": nome, "Preco": preco}
    print(f"Produto '{nome}' adicionado com sucesso.")

def remover_produto(inventario, codigo):
    if codigo in inventario:
        nome = inventario[codigo]['Nome']
        del inventario[codigo]
        print(f"Produto '{nome}' removido com sucesso.")
    else:
        print("Código do produto não encontrado.")

def listar_produtos(inventario):
    if inventario:
        for codigo, info in inventario.items():
            print(f"Código: {codigo}, Nome: {info['Nome']}, Preço: {info['Preco']}, Quantidade: {info['Quantidade']}")
    else:
        print("Inventário vazio.")

def main():
    inventario = {}
    while True:
        print("\n1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            adicionar_produto(inventario, codigo, nome, preco)
        elif escolha == '2':
            codigo = input("Digite o código do produto a ser removido: ")
            remover_produto(inventario, codigo)
        elif escolha == '3':
            listar_produtos(inventario)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()