import cx_Oracle

from Usuario import Usuario

class Voluntario(Usuario):
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None, cel_usuario=None, senha_usuario=None, status_usuario=None, data_registro_voluntario=None):
        super().__init__(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
        self._data_registro_voluntario = data_registro_voluntario

    @property
    def data_registro_voluntario(self):
        return self._data_registro_voluntario

    @data_registro_voluntario.setter
    def data_registro_voluntario(self, data_registro_voluntario):
        self._data_registro_voluntario = data_registro_voluntario
