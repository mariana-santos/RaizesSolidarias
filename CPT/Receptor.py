import cx_Oracle

from Usuario import Usuario

class Receptor(Usuario):
    def __init__(self, id_usuario=None, cpf_usuario=None, nome_usuario=None, email_usuario=None, cel_usuario=None, senha_usuario=None, status_usuario=None, carga_receptor=None, endereco_receptor=None):
        super().__init__(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
        self._carga_receptor = carga_receptor
        self._endereco_receptor = endereco_receptor

    @property
    def carga_receptor(self):
        return self._carga_receptor

    @carga_receptor.setter
    def carga_receptor(self, carga_receptor):
        self._carga_receptor = carga_receptor

    @property
    def endereco_receptor(self):
        return self._endereco_receptor

    @endereco_receptor.setter
    def endereco_receptor(self, endereco_receptor):
        self._endereco_receptor = endereco_receptor