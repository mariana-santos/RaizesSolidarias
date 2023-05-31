import cx_Oracle

from datetime import datetime
import sqlite3

from Funcoes import Funcoes

class Colheita:
    def __init__(self, id_colheita: int = None, data_colheita: str = None, descricao_colheita: str = None):
        self.__id_colheita = id_colheita
        self.__data_colheita = data_colheita
        self.__descricao_colheita = descricao_colheita

    @property
    def id_colheita(self) -> int:
        return self.__id_colheita

    @id_colheita.setter
    def id_colheita(self, id_colheita: int):
        self.__id_colheita = id_colheita

    @property
    def data_colheita(self) -> str:
        return self.__data_colheita

    @data_colheita.setter
    def data_colheita(self, data_colheita: str):
        self.__data_colheita = data_colheita

    @property
    def descricao_colheita(self) -> str:
        return self.__descricao_colheita

    @descricao_colheita.setter
    def descricao_colheita(self, descricao_colheita: str):
        self.__descricao_colheita = descricao_colheita

    def perfilColheita(colheita_buscada):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {colheita_buscada.id_colheita}\n"
        retornoPerfil += f"02. DATA: {colheita_buscada.nome_colheita}\n"
        retornoPerfil += f"03. DESCRIÇÃO: {colheita_buscada.tempo_colheita}\n"
        retornoPerfil += "04. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarColheita(dsn, id_colheita, listaColheitas):
        # INSTANCIANDO NOVA COLHEITA - OK
        nova_colheita = Colheita()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVA COLHEITA - OK
        id_colheita = id_colheita

        # SETANDO A DATA DA NOVA COLHEITA - OK
        try:
            data_colheita = input(f"DIGITE A DATA DA COLHEITA (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            data_colheita = Funcoes.validarPreenchimento(f"DIGITE A DATA DA COLHEITA (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", data_colheita)
            data_formatada = datetime.strptime(data_colheita, "%d/%m/%Y").date()
            data_formatada = datetime.strptime(data_colheita, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%Y-%m-%d")

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA DATA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA DATA DA COLHEITA:")
            print(str(e))
    
        # SETANDO A DESCRIÇÃO DA NOVA COLHEITA - OK
        try:
            descricao_colheita = input(f"DIGITE A DESCRIÇÃO DA COLHEITA: ")
            descricao_colheita = Funcoes.validarPreenchimento(f"DIGITE A DESCRIÇÃO DA COLHEITA: ", descricao_colheita)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA DESCRIÇÃO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA DESCRIÇÃO DA COLHEITA:")
            print(str(e))

        # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS - OK
            cursor.execute("INSERT INTO colheita (id_colheita, data_colheita, descricao_colheita) VALUES (:1, :2, :3)", (id_colheita, data_formatada_banco, descricao_colheita))
            cursor.connection.commit()

            # FAZENDO UPDATE NO CONSOLE - OK
            nova_colheita.id_colheita = id_colheita
            nova_colheita.data_colheita = data_formatada
            nova_colheita.descricao_colheita = descricao_colheita
            listaColheitas.append(nova_colheita)
            id_colheita = id_colheita + 1

            print("COLHEITA CADASTRADA COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DA COLHEITA:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
            Funcoes.disconnect(conn, cursor)

    def editarColheita(dsn, listaColheitas):
        perfilColheita = True

        if (len(listaColheitas) == 0):
            input("NENHUMA COLHEITA CADASTRADA. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirColheitasAdmin(listaColheitas)
            id_buscado = int(input("DIGITE O ID DA COLHEITA QUE DESEJA EDITAR: \n"))
            colheita_buscada = Funcoes.buscarColheitaPorId(id_buscado, listaColheitas)
            colheita_buscada = Funcoes.validarColheitaBuscado(colheita_buscada, listaColheitas)

            while (perfilColheita):
                opcao = int(input(Colheita.perfilColheita(colheita_buscada)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 4, Colheita.perfilColheita(colheita_buscada)))

                if (opcao == 1):
                    # EDITAR O ID DA COLHEITA - OK
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR A DATA DA COLHEITA - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DATA DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DATA DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    
                    if (opcao == 1):
                       # EDITAR A DATA DA COLHEITA - SIM - OK
                       Colheita.editarData(dsn, colheita_buscada)
                    
                    elif (opcao == 2):
                        # EDITAR A DATA DA COLHEITA - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 3):
                    # EDITAR A DESCRIÇÃO DA COLHEITA - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DESCRIÇÃO DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DESCRIÇÃO DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    
                    if (opcao == 1):
                       # EDITAR A DESCRIÇÃO DA COLHEITA - SIM - OK
                       Colheita.editarDescricao(dsn, colheita_buscada)
                    
                    elif (opcao == 2):
                        # EDITAR A DESCRIÇÃO DA COLHEITA - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    perfilColheita = False

    def editarData(dsn, colheita_buscada):
        try:
            nova_data = input(f"DIGITE A NOVA DATA DA COLHEITA DE ID {colheita_buscada.id_colheita} (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            nova_data = Funcoes.validarPreenchimento(f"DIGITE A NOVA DATA DA COLHEITA DE ID {colheita_buscada.id_colheita} (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", nova_data)
            data_formatada = datetime.strptime(nova_data, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%Y-%m-%d")

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE colheita SET data_colheita = :data_formatada_banco WHERE id_colheita = :id_colheita", {"data_formatada_banco": data_formatada_banco, "id_colheita": colheita_buscada.id_colheita})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                colheita_buscada.data_colheita = data_formatada

                print("DATA DA COLHEITA EDITADA COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA DATA:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA DATA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA DATA DA COLHEITA:")
            print(str(e))
    
    def editarDescricao(dsn, colheita_buscada):
        try:
            nova_descricao = input(f"DIGITE A NOVA DESCRIÇÃO DA COLHEITA DE ID {colheita_buscada.id_colheita}: ")
            nova_descricao = Funcoes.validarPreenchimento(f"DIGITE A NOVA DESCRIÇÃO DA COLHEITA DE ID {colheita_buscada.id_colheita}: ", nova_descricao)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE colheita SET descricao_colheita = :nova_descricao WHERE id_colheita = :id_colheita", {"nova_descricao": nova_descricao, "id_colheita": colheita_buscada.id_colheita})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                colheita_buscada.descricao_colheita = nova_descricao

                print("DESCRIÇÃO DA COLHEITA EDITADA COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA DESCRIÇÃO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA DESCRIÇÃO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA DESCRIÇÃO DA COLHEITA:")
            print(str(e))

    def excluirColheita(dsn, listaColheitas):
        
        if len(listaColheitas) == 0:
            print("NÃO EXISTEM COLHEITAS CADASTRADAS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirColheitasAdmin(listaColheitas)
            try:
                id_buscado = int(input("DIGITE O ID DA COLHEITA QUE DESEJA EXCLUIR: \n"))
                colheita_buscada = Funcoes.buscarColheitaPorId(id_buscado, listaColheitas)
                colheita_buscada = Funcoes.validarColheitaBuscado(colheita_buscada, listaColheitas)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR A COLHEITA")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR A COLHEITA"))

                if opcao == 1:
                    for i in range(len(listaColheitas)):
                        if listaColheitas[i].id_colheita == id_buscado:
                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try: 
                                # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                                cursor.execute("DELETE FROM colheita WHERE id_colheita = :1", (listaColheitas[i].id_colheita,))
                                cursor.connection.commit()

                                del listaColheitas[i]

                                print("COLHEITA EXCLUÍDA COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A EXCLUSÃO DA COLHEITA:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DA COLHEITA A SER EXCLUÍDA:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DA COLHEITA:")
                print(str(e))
