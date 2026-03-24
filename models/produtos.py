class Produto: 
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
    
    def adicionar_produto(self, valor):
        self.quantidade += valor

    def remover_produto(self, valor):
        self.quantidade -= valor

    def atualizar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    def mostrar_dados(self):
        print(f"Produto: {self.nome}, Quantidade: {self.quantidade}")    