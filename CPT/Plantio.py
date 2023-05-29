import cx_Oracle

class Plantio:
    def __init__(self, id_plantio=None, data_plantio=None, espaco_plantio=None, alimento=None):
        self.__id_plantio = id_plantio
        self.__data_plantio = data_plantio
        self.__espaco_plantio = espaco_plantio
        self.__alimento = alimento

    @property
    def id_plantio(self):
        return self.__id_plantio

    @id_plantio.setter
    def id_plantio(self, id_plantio):
        self.__id_plantio = id_plantio

    @property
    def data_plantio(self):
        return self.__data_plantio

    @data_plantio.setter
    def data_plantio(self, data_plantio):
        self.__data_plantio = data_plantio

    @property
    def espaco_plantio(self):
        return self.__espaco_plantio

    @espaco_plantio.setter
    def espaco_plantio(self, espaco_plantio):
        self.__espaco_plantio = espaco_plantio

    @property
    def alimento(self):
        return self.__alimento

    @alimento.setter
    def alimento(self, alimento):
        self.__alimento = alimento