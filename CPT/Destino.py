import cx_Oracle

class Destino:
    def __init__(self, id_destino=None, endereco_destino=None, responsavel_destino=None, cel_destino=None, qtd_dependentes_destino=None):
        self.__id_destino = id_destino
        self.__endereco_destino = endereco_destino
        self.__responsavel_destino = responsavel_destino
        self.__cel_destino = cel_destino
        self.__qtd_dependentes_destino = qtd_dependentes_destino

    @property
    def id_destino(self):
        return self.__id_destino

    @id_destino.setter
    def id_destino(self, id_destino):
        self.__id_destino = id_destino

    @property
    def endereco_destino(self):
        return self.__endereco_destino

    @endereco_destino.setter
    def endereco_destino(self, endereco_destino):
        self.__endereco_destino = endereco_destino

    @property
    def responsavel_destino(self):
        return self.__responsavel_destino

    @responsavel_destino.setter
    def responsavel_destino(self, responsavel_destino):
        self.__responsavel_destino = responsavel_destino

    @property
    def cel_destino(self):
        return self.__cel_destino

    @cel_destino.setter
    def cel_destino(self, cel_destino):
        self.__cel_destino = cel_destino

    @property
    def qtd_dependentes_destino(self):
        return self.__qtd_dependentes_destino

    @qtd_dependentes_destino.setter
    def qtd_dependentes_destino(self, qtd_dependentes_destino):
        self.__qtd_dependentes_destino = qtd_dependentes_destino