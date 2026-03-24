
from models.produtos import Produto

from services.estoque import Estoque

estoque = Estoque() 

produto1 = Produto("teclado", 10)
produto2 = Produto("mouse", 20)

estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)

estoque.listar_produtos()

estoque.buscar_produto("teclado")

estoque.atualizar_quantidade("mouse", 15)

estoque.listar_produtos()