#coding:latin-1
from datetime import date
import datetime
import trocas

class RelacaoTrocas(object): 
    def __init__(self):
        self.lista_relacao_trocas = []

    def cadastrar_trocas(self, nova_troca): 
        self.lista_relacao_trocas.append(nova_troca)

    def relacao_aparelhoscomdefeito(self):#Daqui sai a relação de aparelhos com defeito
        total_aparelhos = len(self.lista_relacao_trocas)
        posicao = 0
        while (posicao < total_aparelhos):
            print self.lista_relacao_trocas[posicao]
            posicao = posicao + 1
