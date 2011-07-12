#coding:latin-1
import unittest
from should_dsl import should
from produto import Produto
from estoque import Estoque

class TesteEstoque(unittest.TestCase):

    def teste_estoque(self):
        estoque = Estoque()
        estoque.lista_produtos |should| equal_to([])

    def teste_cadastrar_produtos(self):
        estoque = Estoque()
        produto = Produto('Computador', 'Dell', 'SN2011', 1500)
        estoque.cadastrar_produto(produto)
        estoque.lista_produtos |should| have(1).itens
        estoque.lista_produtos[0].descricao |should| equal_to('Computador')
        produto1 = Produto('Computador', 'CCE', 'SN2011', 1300)
        estoque.cadastrar_produto(produto1)
        estoque.lista_produtos |should| have(2).itens
        estoque.lista_produtos[1].marca |should| equal_to('CCE')

    def teste_inserir_item_produto(self):
        estoque = Estoque()
        produto = Produto('Computador', 'Dell', 'SN2011', 1500)
        estoque.cadastrar_produto(produto)
        produto1 = Produto('Computador', 'CCE', 'SN2011', 1300)
        estoque.cadastrar_produto(produto1)
        estoque.inserir_item_produto(0, 'powqieowqiepowq')
        estoque.lista_produtos[0].numero_serie |should| have(1).itens
        estoque.lista_produtos[0].numero_serie[0] |should| equal_to('powqieowqiepowq')
        estoque.inserir_item_produto(0, '11111111111111')
        estoque.lista_produtos[0].numero_serie |should| have(2).itens
        estoque.lista_produtos[0].numero_serie[1] |should| equal_to('11111111111111')

    def teste_buscar_produto(self):
        estoque = Estoque()
        produto = Produto('Computador', 'Dell', 'SN2011', 1500)
        estoque.cadastrar_produto(produto)
        produto1 = Produto('Mouse', 'CCE', 'SN2011', 1300)
        estoque.cadastrar_produto(produto1)
        estoque.inserir_item_produto(0, 'powqieowqiepowq')
        estoque.inserir_item_produto(0, '11111111111111')
        estoque.buscar_produto('Mouse') |should| equal_to(1)
        estoque.buscar_produto('Computador') |should| equal_to(0)
        estoque.buscar_produto('Ricks') |should| equal_to(None)

    def teste_buscar_numero_serie(self):
        estoque = Estoque()
        produto = Produto('Computador', 'Dell', 'SN2011', 1500)
        estoque.cadastrar_produto(produto)
        produto1 = Produto('Mouse', 'CCE', 'SN2011', 1300)
        estoque.cadastrar_produto(produto1)
        estoque.inserir_item_produto(0, 'powqieowqiepowq')
        estoque.inserir_item_produto(0, '11111111111111')
        produto_encontrado = estoque.buscar_produto('Computador')
        estoque.buscar_numero_serie(produto_encontrado) |should| equal_to('powqieowqiepowq')
        produto_encontrado = estoque.buscar_produto('Mouse')
        estoque.buscar_numero_serie(produto_encontrado) |should| equal_to(None)

    def teste_relacao_aparelhos(self):
        estoque = Estoque()
        produto = Produto('Computador', 'Dell', 'SN2011', 1500)
        estoque.cadastrar_produto(produto)
        produto1 = Produto('Mouse', 'CCE', 'SN2011', 1300)
        estoque.cadastrar_produto(produto1)
        estoque.inserir_item_produto(0, 'powqieowqiepowq')
        estoque.inserir_item_produto(0, '11111111111111')
        estoque.lista_produtos |should| have(2).itens
        estoque.lista_produtos[0].numero_serie |should| have(2).itens
        estoque.lista_produtos[1].numero_serie |should| have(0).itens
        estoque.relacao_aparelhos()

    def teste_vender_produto(self):
        estoque = Estoque()
        produto = Produto('Computador', 'Dell', 'SN2011', 1500)
        estoque.cadastrar_produto(produto)
        estoque.inserir_item_produto(0, 'powqieowqiepowq')
        estoque.inserir_item_produto(0, '11111111111111')
        estoque.vender_produto('Computador')
        estoque.lista_produtos[0].numero_serie[0] |should| equal_to('11111111111111')

    def teste_trocar_aparelho(self):
        estoque = Estoque()
        produto = Produto('Computador', 'Dell', 'SN2011', 1500)
        estoque.cadastrar_produto(produto)
        estoque.inserir_item_produto(0, 'powqieowqiepowq')
        estoque.inserir_item_produto(0, '11111111111111')
        estoque.vender_produto('Computador')
        estoque.lista_produtos[0].numero_serie[0] |should| equal_to('11111111111111')
    
if __name__ == '__main__':
    unittest.main()
