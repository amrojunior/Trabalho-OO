#coding:latin-1
import unittest
from should_dsl import should
from vendas import Vendas
from datetime import date

class TesteVendas(unittest.TestCase):

    def teste_vendas(self):
        vendas = Vendas('000111', '20110001', 'Computador','Dell', 'Modelo2011', 1500, 1, '213qwe', 'Marcos Antônio', 'Av. das Coves, 23')
        vendas.numero_venda |should| equal_to('000111')
        vendas.codigo_produto |should| equal_to('20110001')
        vendas.descricao |should| equal_to('Computador')
        vendas.data_venda |should| equal_to(date.today())
        vendas.marca |should| equal_to('Dell')
        vendas.modelo |should| equal_to('Modelo2011')
        vendas.preco_venda |should| equal_to(1500)
        vendas.quantidade_vendida |should| equal_to(1)
        vendas.numero_serie |should| equal_to('213qwe')
        vendas.cliente |should| equal_to('Marcos Antônio')
        vendas.endereco_cliente |should| equal_to('Av. das Coves, 23')

if __name__ == '__main__':
    unittest.main()
