import cx_Oracle

from Usuario import Usuario

class Voluntario(Usuario):
    def __init__(self, id_usuario: int = None, cpf_usuario: str = None, nome_usuario: str = None, email_usuario: str = None, cel_usuario: str = None, senha_usuario: str = None, status_usuario: str = None, data_registro_voluntario: str = None):
        super().__init__(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
        self._data_registro_voluntario = data_registro_voluntario

    @property
    def data_registro_voluntario(self) -> str:
        return self._data_registro_voluntario

    @data_registro_voluntario.setter
    def data_registro_voluntario(self, data_registro_voluntario: str):
        self._data_registro_voluntario = data_registro_voluntario
