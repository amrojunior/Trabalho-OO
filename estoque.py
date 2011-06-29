#coding:latin-1
class Estoque(object):
    def __init__(self, codigo_produto, descricao, marca, modelo, numero_serie, quantidade, preco):
        self.codigo_produto = codigo_produto
        self.descricao = descricao
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.quantidade = quantidade
        self.preco = preco
