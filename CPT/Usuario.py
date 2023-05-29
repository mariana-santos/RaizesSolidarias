import cx_Oracle

class Usuario:
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None, cel_usuario=None, senha_usuario=None, status_usuario=None):
        self._id_usuario = id_usuario
        self._cpf_usuario = cpf_usuario
        self._nome_usuario = nome_usuario
        self._email_usuario = email_usuario
        self._cel_usuario = cel_usuario
        self._senha_usuario = senha_usuario
        self._status_usuario = status_usuario

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def cpf_usuario(self):
        return self._cpf_usuario

    @cpf_usuario.setter
    def cpf_usuario(self, cpf_usuario):
        self._cpf_usuario = cpf_usuario

    @property
    def nome_usuario(self):
        return self._nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, nome_usuario):
        self._nome_usuario = nome_usuario

    @property
    def email_usuario(self):
        return self._email_usuario

    @email_usuario.setter
    def email_usuario(self, email_usuario):
        self._email_usuario = email_usuario

    @property
    def cel_usuario(self):
        return self._cel_usuario

    @cel_usuario.setter
    def cel_usuario(self, cel_usuario):
        self._cel_usuario = cel_usuario

    @property
    def senha_usuario(self):
        return self._senha_usuario

    @senha_usuario.setter
    def senha_usuario(self, senha_usuario):
        self._senha_usuario = senha_usuario

    @property
    def status_usuario(self):
        return self._status_usuario

    @status_usuario.setter
    def status_usuario(self, status_usuario):
        self._status_usuario = status_usuario
