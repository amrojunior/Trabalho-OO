#coding:latin-1
import unittest
from should_dsl import should
from produto import Produto

class TesteProduto(unittest.TestCase):

    def teste_produto(self):
        produto = Produto('Computador', 'Dell', 'SN2011', 1500)
        produto.descricao |should| equal_to('Computador')
        produto.marca |should| equal_to('Dell')
        produto.modelo |should| equal_to('SN2011')
        produto.preco |should| equal_to(1500)

if __name__ == '__main__':
    unittest.main()
