#coding:latin-1
import estoque
class Produto(object):
    def __init__(self, descricao, marca, modelo, preco):
        self.descricao = descricao
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = []
        self.preco = preco     
