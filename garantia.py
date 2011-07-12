#coding:latin-1
import estoque
import termo_garantia
from datetime import date
import datetime

class Garantia(object):
       
    def __init__(self, numero_venda, data_venda, data_validade, marca, modelo, numero_serie, nome_cliente, endereco_cliente):
        self.numero_venda = numero_venda
        self.data_venda = date.today()
        self.data_validade = self.data_venda + datetime.timedelta(days=365)
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.nome_cliente = nome_cliente
        self.endereco_cliente = endereco_cliente
 
