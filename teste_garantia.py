#coding:latin-1
import unittest
from should_dsl import should
from estoque import Estoque
from datetime import date
from garantia import Garantia
import datetime

class TesteGarantia(unittest.TestCase):
    
    def teste_garantia(self):
        garantia = Garantia('000111', date.today(), date.today() + datetime.timedelta(days=365), 'Dell', 'MO2011', 'SN20111', 'Marcos Antônio', 'Av. das Coves, 23')
        garantia.numero_venda |should| equal_to('000111')
        garantia.data_venda |should| equal_to(date.today())
        garantia.data_validade |should| equal_to(datetime.date(2012, 7, 10))
        garantia.marca |should| equal_to('Dell')
        garantia.modelo |should| equal_to('MO2011')
        garantia.numero_serie |should| equal_to('SN20111')
        garantia.nome_cliente |should| equal_to('Marcos Antônio')
        garantia.endereco_cliente |should| equal_to('Av. das Coves, 23')

if __name__ == '__main__':
    unittest.main()
