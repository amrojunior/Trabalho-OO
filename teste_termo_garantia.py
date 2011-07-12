#coding:latin-1
import unittest
from should_dsl import should
from estoque import Estoque
from datetime import date
from garantia import Garantia
from termo_garantia import TermoGarantia
import datetime

class TesteTermoGarantia(unittest.TestCase):

    def teste_termo_de_garantia(self):
        termo_garantia = TermoGarantia()
        termo_garantia.lista_garantias |should| equal_to([])
    
    def teste_cadastrar_garantia(self):
        termo_garantia = TermoGarantia()
        garantia = Garantia('000111', date.today(), date.today() + datetime.timedelta(days=365), 'Dell', 'MO2011', 'SN20111', 'Marcos Antônio', 'Av. das Coves, 23')
        termo_garantia.cadastrar_garantia(garantia)
        termo_garantia.lista_garantias[0].numero_venda |should| equal_to('000111')
        termo_garantia.lista_garantias[0].data_venda |should| equal_to(date.today())
        termo_garantia.lista_garantias[0].data_validade |should| equal_to(datetime.date(2012, 7, 10))
        termo_garantia.lista_garantias[0].modelo |should| equal_to('MO2011')
        termo_garantia.lista_garantias[0].numero_serie |should| equal_to('SN20111')
        termo_garantia.lista_garantias[0].nome_cliente |should| equal_to('Marcos Antônio')
        termo_garantia.lista_garantias[0].endereco_cliente |should| equal_to('Av. das Coves, 23')
        termo_garantia.lista_garantias |should| have(1).itens

    def teste_verificar_numero_venda(self):
        termo_garantia = TermoGarantia()
        garantia = Garantia('000111', date.today(), date.today() + datetime.timedelta(days=365), 'Dell', 'MO2011', 'SN20111', 'Marcos Antônio', 'Av. das Coves, 23')
        termo_garantia.cadastrar_garantia(garantia)
        termo_garantia.verificar_numero_venda('000111') |should| equal_to(0)

    def teste_verificar_prazo_validade(self):
        termo_garantia = TermoGarantia()
        garantia = Garantia('000111', datetime.date(2010, 07, 30), date.today(), 'Dell', 'MO2011', 'SN20111', 'Marcos Antônio', 'Av. das Coves, 23')
        termo_garantia.cadastrar_garantia(garantia)
        date.today() - datetime.date(2010, 07, 30) |should| be_less_than_or_equal_to(datetime.timedelta(365))
        date.today() - datetime.date(2010, 04, 30) |should| be_greater_than(datetime.timedelta(365))
               
   
if __name__ == '__main__':
    unittest.main()
