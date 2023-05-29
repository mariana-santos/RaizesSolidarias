import cx_Oracle

class Doacao:
    def __init__(self, id_doacao=None, doador=None, data_doacao=None, qtd_moedas_doacao=None):
        self.__id_doacao = id_doacao
        self.__doador = doador
        self.__data_doacao = data_doacao
        self.__qtd_moedas_doacao = qtd_moedas_doacao

    @property
    def id_doacao(self):
        return self.__id_doacao

    @id_doacao.setter
    def id_doacao(self, id_doacao):
        self.__id_doacao = id_doacao

    @property
    def doador(self):
        return self.__doador

    @doador.setter
    def doador(self, doador):
        self.__doador = doador

    @property
    def data_doacao(self):
        return self.__data_doacao

    @data_doacao.setter
    def data_doacao(self, data_doacao):
        self.__data_doacao = data_doacao

    @property
    def qtd_moedas_doacao(self):
        return self.__qtd_moedas_doacao

    @qtd_moedas_doacao.setter
    def qtd_moedas_doacao(self, qtd_moedas_doacao):
        self.__qtd_moedas_doacao = qtd_moedas_doacao