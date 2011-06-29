#coding:latin-1
import unittest
from should_dsl import should
from estoque import Estoque

class TesteEstoque(unittest.TestCase):

    def teste_estoque(self):
        estoque = Estoque('20110001', 'Computador', 'Dell', 'Serie2011', '213qwe', 10, 1500)
        estoque.codigo_produto |should| equal_to('20110001')
        estoque.descricao |should| equal_to('Computador')
        estoque.marca |should| equal_to('Dell')
        estoque.modelo |should| equal_to('Serie2011')
        estoque.numero_serie |should| equal_to('213qwe')
        estoque.quantidade |should| equal_to(10)
        estoque.preco |should| equal_to(1500)


if __name__ == '__main__':
    unittest.main()
