#coding:latin-1

from datetime import date

class Vendas(object):
    def __init__(self, numero_venda, codigo_produto, descricao, marca, modelo, preco_venda, quantidade_vendida, numero_serie, cliente, endereco_cliente):
        self.numero_venda = numero_venda
        self.codigo_produto = codigo_produto
        self.descricao = descricao
        self.data_venda = date.today()
        self.marca = marca
        self.modelo = modelo
        self.preco_venda = preco_venda
        self.quantidade_vendida = quantidade_vendida
        self.numero_serie = numero_serie
        self.cliente = cliente
        self.endereco_cliente = endereco_cliente
