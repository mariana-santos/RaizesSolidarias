import cx_Oracle
import sqlite3

from Funcoes import Funcoes
from Usuario import Usuario

class Doador(Usuario):
    def __init__(self, id_usuario: int = None, cpf_usuario: str = None, nome_usuario: str = None, email_usuario: str = None, cel_usuario: str = None, senha_usuario: str = None, status_usuario: str = None, nivel_doador: int = None, moedas_doador: int = None):
        super().__init__(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
        self._nivel_doador = nivel_doador
        self._moedas_doador = moedas_doador

    @property
    def nivel_doador(self) -> int:
        return self._nivel_doador

    @nivel_doador.setter
    def nivel_doador(self, nivel_doador: int):
        self._nivel_doador = nivel_doador

    @property
    def moedas_doador(self) -> int:
        return self._moedas_doador

    @moedas_doador.setter
    def moedas_doador(self, moedas_doador: int):
        self._moedas_doador = moedas_doador

    def editarNivel(dsn, usuario_buscado):
        try:
            novo_nivel = int(input(f"DIGITE O NOVO NÍVEL DO DOADOR {usuario_buscado.nome_usuario}: "))
            novo_nivel = int(Funcoes.validarPreenchimento(f"DIGITE O NOVO NÍVEL DO DOADOR {usuario_buscado.nome_usuario}: ", novo_nivel))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE doador SET nivel_doador = :novo_nivel WHERE id_usuario = :id_usuario", {"novo_nivel": novo_nivel, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                usuario_buscado.nivel_doador = novo_nivel

                print("NÍVEL DO DOADOR EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO NÍVEL:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO NÍVEL:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO NÍVEL DO DOADOR:")
            print(str(e))

    def editarMoedas(dsn, usuario_buscado):
        try:
            moedas_adicionar = int(input(f"QUANTAS MOEDAS DESEJA ADICIONAR/SUBTRAIR DO DOADOR {usuario_buscado.nome_usuario}? "))
            moedas_adicionar = int(Funcoes.validarPreenchimento(f"QUANTAS MOEDAS DESEJA ADICIONAR/SUBTRAIR DO DOADOR {usuario_buscado.nome_usuario}? ", str(moedas_adicionar)))
            novas_moedas = moedas_adicionar + usuario_buscado.moedas_doador

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE doador SET moedas_doador = :novas_moedas WHERE id_usuario = :id_usuario", {"novas_moedas": novas_moedas, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                usuario_buscado.moedas_doador = novas_moedas

                print("MOEDAS DO DOADOR EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DAS MOEDAS:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DAS NOVAS MOEDAS:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DAS MOEDAS DO DOADOR:")
            print(str(e))
