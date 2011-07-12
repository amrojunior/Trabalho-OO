#coding:latin-1

class Cliente(object):
    def __init__(self, codigo, nome, endereco, situacao):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.situacao = situacao
