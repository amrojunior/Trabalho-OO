#coding:latin-1
import garantia
import estoque
from datetime import date
import datetime
class TermoGarantia(object):
  
    def __init__(self):
        self.lista_garantias = []        
  
    def cadastrar_garantia(self, nova_garantia):
        self.lista_garantias.append(nova_garantia)

    def verificar_numero_venda(self, numero_venda_pesquisado):
        total_termos_garantia = len(self.lista_garantias)
        numero_venda_verificado = 0
        while (numero_venda_verificado < total_termos_garantia) and (self.lista_garantias[numero_venda_verificado].numero_venda != numero_venda_pesquisado):
            numero_venda_veriicado = numero_venda_veriicado + 1
        if numero_venda_pesquisado == total_termos_garantia:
            return None
        else:
            return numero_venda_verificado

    def verificar_prazo_validade(self, ano, mes, dia):
        hoje = date.today()
        data_venda_verificar = date(ano, mes, dia)
        hoje = hoje - data_venda_verificar
        if hoje <= 365:
            return True, hoje
        else:
            return False, hoje
