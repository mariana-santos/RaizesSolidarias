import cx_Oracle

class Colheita:
    def __init__(self, id_colheita=None, data_colheita=None, descricao_colheita=None):
        self.__id_colheita = id_colheita
        self.__data_colheita = data_colheita
        self.__descricao_colheita = descricao_colheita

    @property
    def id_colheita(self):
        return self.__id_colheita

    @id_colheita.setter
    def id_colheita(self, id_colheita):
        self.__id_colheita = id_colheita

    @property
    def data_colheita(self):
        return self.__data_colheita

    @data_colheita.setter
    def data_colheita(self, data_colheita):
        self.__data_colheita = data_colheita

    @property
    def descricao_colheita(self):
        return self.__descricao_colheita

    @descricao_colheita.setter
    def descricao_colheita(self, descricao_colheita):
        self.__descricao_colheita = descricao_colheita