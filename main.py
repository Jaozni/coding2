from tqdm import tqdm
import time

# Cria uma barra de progresso para um loop
for i in tqdm(range(100), desc="Carregando"):
    time.sleep(0.005)  # Simula uma tarefa (ex: download, processamento)



from models.produtos import Produto

from services.estoque import Estoque


print("=========================================================== ✨  BEM VINDO  ✨ ===========================================================")
print("                                                        Seja muito bem-vindo ao sistema. ")
print("                             tudo foi carregado com sucesso e agora você está pronto para visualizar as funcionalidades disponíveis.")              
print("====================================================== Sistema inicializado com sucesso! ===========================================================")


estoque = Estoque() 

produto1 = Produto("teclado", 10)
produto2 = Produto("mouse", 20)

estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)

estoque.listar_produtos()

estoque.buscar_produto("teclado")

estoque.atualizar_quantidade("mouse", 15)

estoque.listar_produtos()

