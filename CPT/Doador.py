import cx_Oracle

from Usuario import Usuario

class Doador(Usuario):
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None, cel_usuario=None, senha_usuario=None, status_usuario=None, nivel_doador=None, moedas_doador=None):
        super().__init__(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
        self._nivel_doador = nivel_doador
        self._moedas_doador = moedas_doador

    @property
    def nivel_doador(self):
        return self._nivel_doador

    @nivel_doador.setter
    def nivel_doador(self, nivel_doador):
        self._nivel_doador = nivel_doador

    @property
    def moedas_doador(self):
        return self._moedas_doador

    @moedas_doador.setter
    def moedas_doador(self, moedas_doador):
        self._moedas_doador = moedas_doador