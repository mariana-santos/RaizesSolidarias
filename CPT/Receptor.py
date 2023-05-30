import cx_Oracle
import sqlite3

from Funcoes import Funcoes
from Usuario import Usuario

class Receptor(Usuario):
    def __init__(self, id_usuario: int = None, cpf_usuario: str = None, nome_usuario: str = None, email_usuario: str = None, cel_usuario: str = None, senha_usuario: str = None, status_usuario: str = None, carga_receptor: int = None, endereco_receptor: str = None):
        super().__init__(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
        self._carga_receptor = carga_receptor
        self._endereco_receptor = endereco_receptor

    @property
    def carga_receptor(self) -> int:
        return self._carga_receptor

    @carga_receptor.setter
    def carga_receptor(self, carga_receptor: int):
        self._carga_receptor = carga_receptor

    @property
    def endereco_receptor(self) -> str:
        return self._endereco_receptor

    @endereco_receptor.setter
    def endereco_receptor(self, endereco_receptor: str):
        self._endereco_receptor = endereco_receptor

    def editarCarga(dsn, usuario_buscado):
        try:
            nova_carga = int(input(f"DIGITE A NOVA CARGA SUPORTADA DO RECEPTOR {usuario_buscado.nome_usuario}: "))
            nova_carga = int(Funcoes.validarPreenchimento(f"DIGITE A NOVA CARGA SUPORTADA DO RECEPTOR {usuario_buscado.nome_usuario}: ", nova_carga))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE receptor SET carga_receptor = :nova_carga WHERE id_usuario = :id_usuario", {"nova_carga": nova_carga, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                usuario_buscado.carga_receptor = nova_carga

                print("CARGA DO RECEPTOR EDITADA COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA CARGA:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVA CARGA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA CARGA DO RECEPTOR:")
            print(str(e))

    def editarEndereco(dsn, usuario_buscado):
        try:
            novo_endereco = input(f"DIGITE O NOVO ENDEREÇO DO RECEPTOR {usuario_buscado.nome_usuario}: ")
            novo_endereco = Funcoes.validarPreenchimento(f"DIGITE O NOVO ENDEREÇO DO RECEPTOR {usuario_buscado.nome_usuario}: ", novo_endereco)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE receptor SET endereco_receptor = :novo_endereco WHERE id_usuario = :id_usuario", {"novo_endereco": novo_endereco, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                usuario_buscado.endereco_receptor = novo_endereco

                print("ENDEREÇO DO RECEPTOR EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO ENDEREÇO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO ENDEREÇO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO ENDEREÇO DO RECEPTOR:")
            print(str(e))
