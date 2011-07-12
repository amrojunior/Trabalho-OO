#coding:latin-1
import produto
class Estoque(object):
    def __init__(self):
        self.lista_produtos = []
        #self.produtos_defeituosos = []

    def cadastrar_produto(self, novo_produto):
        self.lista_produtos.append(novo_produto)

    def inserir_item_produto(self, posicao_produto, novo_numero_serie):
        self.lista_produtos[posicao_produto].numero_serie.append(novo_numero_serie)

    def buscar_produto(self, pesquisa_descricao):
        total_produtos = len(self.lista_produtos)
        numero_produto = 0
        while (numero_produto < total_produtos) and (self.lista_produtos[numero_produto].descricao != pesquisa_descricao):
            numero_produto = numero_produto + 1
        if numero_produto == total_produtos:
            return None
        else:
            return numero_produto

    def buscar_numero_serie(self, numero_serie_procurado):
        if len(self.lista_produtos[numero_serie_procurado].numero_serie) > 0:
            return self.lista_produtos[numero_serie_procurado].numero_serie.pop(0)
        else:
            return None

    def relacao_aparelhos(self):
        total_produtos = len(self.lista_produtos)
        posicao_produto = 0
        print self.lista_produtos[posicao_produto].descricao
        while posicao_produto < total_produtos:
            total_numero_serie = len(self.lista_produtos[posicao_produto].numero_serie)
            posicao_numero_serie = 0
            while posicao_numero_serie < total_numero_serie:
                if total_numero_serie != 0:
                    print self.lista_produtos[posicao_produto].numero_serie[posicao_numero_serie]
                posicao_numero_serie = posicao_numero_serie + 1
            posicao_produto = posicao_produto + 1

    def vender_produto(self, descricao_produto):
        posicao_produto = self.buscar_produto(descricao_produto)
        if len(self.lista_produtos[posicao_produto].numero_serie) > 0:
            numero_serie_retornado = self.lista_produtos[posicao_produto].numero_serie[0]
            return self.lista_produtos[posicao_produto].numero_serie.pop(0)
        else:
            return posicao_produto

    def trocar_aparelho(self, descricao_produto):
        posicao_produto = self.buscar_produto(descricao_produto)
        if len(self.lista_produtos[posicao_produto].numero_serie) > 0:
            numero_serie_retornado = self.lista_produtos[posicao_produto].numero_serie[0]
            return self.lista_produtos[posicao_produto].numero_serie.pop(0)
        else:
            return posicao_produto
