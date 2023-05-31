import cx_Oracle
import sqlite3

from datetime import datetime

from Funcoes import Funcoes
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

    def perfilVoluntario(voluntario_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {voluntario_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {voluntario_buscado.cpf_usuario}\n"
        retornoPerfil += f"03. NOME: {voluntario_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {voluntario_buscado.email_usuario}\n"
        retornoPerfil += f"05. CELULAR: {voluntario_buscado.cel_usuario}\n"
        retornoPerfil += f"06. SENHA: {voluntario_buscado.senha_usuario}\n"
        retornoPerfil += f"07. STATUS: {voluntario_buscado.status_usuario}\n"
        retornoPerfil += f"08. DATA DE REGISTRO: {voluntario_buscado.data_registro_voluntario}\n"
        retornoPerfil += "09. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarVoluntario(dsn, id_usuario, listaUsuarios, listaVoluntarios):
        Voluntario.cadastrarUsuario(dsn, id_usuario, listaUsuarios)
        usuario_buscado = Funcoes.buscarUsuarioPorId(id_usuario, listaUsuarios)

        # INSTANCIANDO NOVO VOLUNTARIO - OK
        novo_voluntario = Voluntario()

        # SETANDO OS ATRIBUTOS DO NOVO USUARIO PARA O NOVO VOLUNTARIO - OK
        id_usuario = usuario_buscado.id_usuario
        cpf_usuario = usuario_buscado.cpf_usuario
        nome_usuario = usuario_buscado.nome_usuario
        email_usuario = usuario_buscado.email_usuario
        cel_usuario = usuario_buscado.cel_usuario
        senha_usuario = usuario_buscado.senha_usuario
        status_usuario = usuario_buscado.status_usuario

        # SETANDO A DATA DE REGISTRO DO NOVO USUARIO - OK
        data_registro_voluntario = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%d/%m/%Y')

        # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS - OK
            cursor.execute("INSERT INTO voluntario (id_usuario, data_registro_voluntario) VALUES (:1, :2)", (id_usuario, data_registro_voluntario))
            cursor.connection.commit()

            # FAZENDO UPDATE NO CONSOLE - OK
            novo_voluntario.id_usuario = id_usuario
            novo_voluntario.cpf_usuario = cpf_usuario
            novo_voluntario.nome_usuario = nome_usuario
            novo_voluntario.email_usuario = email_usuario
            novo_voluntario.cel_usuario = cel_usuario
            novo_voluntario.senha_usuario = senha_usuario
            novo_voluntario.status_usuario = status_usuario
            listaVoluntarios.append(novo_voluntario)
            id_usuario = id_usuario + 1

            print("VOLUNTARIO CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO VOLUNTARIO:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
            Funcoes.disconnect(conn, cursor)
