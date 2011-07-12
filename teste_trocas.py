#coding:latin-1
import unittest
from should_dsl import should
import estoque
import garantia
import termo_garantia
from datetime import date
from trocas import Trocas
import datetime
import trocas

class TesteTrocas(unittest.TestCase):
    def teste_trocas(self):
        trocas = Trocas('000111', 'Computador', 'SN20111', 'Marcos Antônio', date.today(), 'sem parafuso')
        trocas.numero_troca |should| equal_to('000111')
        trocas.descricao |should| equal_to('Computador')
        trocas.numero_serie |should| equal_to('SN20111')
        trocas.cliente |should| equal_to('Marcos Antônio')
        trocas.data_troca |should| equal_to(date.today())
        trocas.defeito |should| equal_to('sem parafuso')
        
if __name__ == '__main__':
    unittest.main()
