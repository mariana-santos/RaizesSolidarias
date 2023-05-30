import cx_Oracle

from Alimento import Alimento

class Plantio:
    def __init__(self, id_plantio: int = None, data_plantio: str = None, espaco_plantio: int = None, alimento: Alimento = None):
        self.__id_plantio = id_plantio
        self.__data_plantio = data_plantio
        self.__espaco_plantio = espaco_plantio
        self.__alimento = alimento

    @property
    def id_plantio(self) -> int:
        return self.__id_plantio

    @id_plantio.setter
    def id_plantio(self, id_plantio: int):
        self.__id_plantio = id_plantio

    @property
    def data_plantio(self) -> str:
        return self.__data_plantio

    @data_plantio.setter
    def data_plantio(self, data_plantio: str):
        self.__data_plantio = data_plantio

    @property
    def espaco_plantio(self) -> int:
        return self.__espaco_plantio

    @espaco_plantio.setter
    def espaco_plantio(self, espaco_plantio: int):
        self.__espaco_plantio = espaco_plantio

    @property
    def alimento(self) -> Alimento:
        return self.__alimento

    @alimento.setter
    def alimento(self, alimento: Alimento):
        self.__alimento = alimento