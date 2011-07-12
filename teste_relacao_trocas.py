#coding:latin-1
import unittest
from should_dsl import should
from datetime import date
import datetime
from trocas import Trocas
from relacao_trocas import RelacaoTrocas

class TesteRelacaoTrocas(unittest.TestCase):
    def teste_relacao_trocas(self):
        relacao_trocas = RelacaoTrocas()
        relacao_trocas.lista_relacao_trocas |should| equal_to([])

    def teste_cadastrar_trocas(self):
        relacao_trocas = RelacaoTrocas()
        trocas = Trocas('000111', 'Computador', 'SN20111', 'Marcos Antônio', date.today(), 'sem parafuso')
        relacao_trocas.cadastrar_trocas(trocas)
        relacao_trocas.lista_relacao_trocas[0].numero_troca |should| equal_to('000111')
        relacao_trocas.lista_relacao_trocas[0].cliente |should| equal_to('Marcos Antônio')
        relacao_trocas.lista_relacao_trocas |should| have(1).itens

    def teste_relacao_aparelhoscomdefeito(self):
        relacao_trocas = RelacaoTrocas()
        trocas1 = Trocas('000111', 'Computador', 'SN20111', 'Marcos Antônio', date.today(), 'sem parafuso')
        relacao_trocas.cadastrar_trocas(trocas1)
        trocas2 = Trocas('000333', 'Mouse', 'SN33000', 'José', date.today(), 'fio quebrado')
        relacao_trocas.cadastrar_trocas(trocas2)
        relacao_trocas.lista_relacao_trocas |should| have(2).itens
        relacao_trocas.relacao_aparelhoscomdefeito()
        

if __name__ == '__main__':
    unittest.main()
