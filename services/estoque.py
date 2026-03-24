class Estoque:
    def __init__(self):
        self.produtos = []        

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}")

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                print(f"Produto encontrado: {produto.nome} - Quantidade: {produto.quantidade}") 
                return
        print("Produto não encontrado.")  

    def atualizar_quantidade(self, nome, nova_quantidade):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                produto.quantidade = nova_quantidade
                print(f"Quantidade do produto '{produto.nome}' atualizada para {nova_quantidade}.")
                return
        print("Produto não encontrado para atualização.")      