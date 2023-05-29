import cx_Oracle

class Agendamento:
    def __init__(self, id_agendamento=None, data_agendamento=None, turno_agendamento=None, usuario=None):
        self.__id_agendamento = id_agendamento
        self.__data_agendamento = data_agendamento
        self.__turno_agendamento = turno_agendamento
        self.__usuario = usuario

    @property
    def id_agendamento(self):
        return self.__id_agendamento

    @id_agendamento.setter
    def id_agendamento(self, id_agendamento):
        self.__id_agendamento = id_agendamento

    @property
    def data_agendamento(self):
        return self.__data_agendamento

    @data_agendamento.setter
    def data_agendamento(self, data_agendamento):
        self.__data_agendamento = data_agendamento

    @property
    def turno_agendamento(self):
        return self.__turno_agendamento

    @turno_agendamento.setter
    def turno_agendamento(self, turno_agendamento):
        self.__turno_agendamento = turno_agendamento

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario