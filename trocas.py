#coding:latin-1
import relacao_trocas
from datetime import date
import datetime

class Trocas(object):
    def __init__(self, numero_troca, descricao, numero_serie, cliente, data_troca, defeito):
        self.numero_troca = numero_troca
        self.descricao = descricao
        self.numero_serie = numero_serie
        self.cliente = cliente
        self.data_troca = date.today()
        self.defeito = defeito
        
