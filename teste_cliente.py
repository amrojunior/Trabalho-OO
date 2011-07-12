#coding:latin-1
import unittest
from cliente import Cliente
from should_dsl import should

class TesteCliente(unittest.TestCase):
    def testa_cliente(self):
        cliente = Cliente('11111', 'maria sapatao', 'av. das sapatas, 33', 'com trocas')
        cliente.codigo |should| equal_to('11111')
        cliente.nome |should| equal_to('maria sapatao')
        cliente.endereco |should| equal_to('av. das sapatas, 33')
        cliente.situacao |should| equal_to('com trocas')

if __name__ == '__main__':
    unittest.main()
        
