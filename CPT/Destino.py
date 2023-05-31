import cx_Oracle

import sqlite3

from Funcoes import Funcoes

class Destino:
    def __init__(self, id_destino: int = None, endereco_destino: str = None, responsavel_destino: str = None, cel_destino: str = None, qtd_dependentes_destino: int = None):
        self.__id_destino = id_destino
        self.__endereco_destino = endereco_destino
        self.__responsavel_destino = responsavel_destino
        self.__cel_destino = cel_destino
        self.__qtd_dependentes_destino = qtd_dependentes_destino

    @property
    def id_destino(self) -> int:
        return self.__id_destino

    @id_destino.setter
    def id_destino(self, id_destino: int):
        self.__id_destino = id_destino

    @property
    def endereco_destino(self) -> str:
        return self.__endereco_destino

    @endereco_destino.setter
    def endereco_destino(self, endereco_destino: str):
        self.__endereco_destino = endereco_destino

    @property
    def responsavel_destino(self) -> str:
        return self.__responsavel_destino

    @responsavel_destino.setter
    def responsavel_destino(self, responsavel_destino: str):
        self.__responsavel_destino = responsavel_destino

    @property
    def cel_destino(self) -> str:
        return self.__cel_destino

    @cel_destino.setter
    def cel_destino(self, cel_destino: str):
        self.__cel_destino = cel_destino

    @property
    def qtd_dependentes_destino(self) -> int:
        return self.__qtd_dependentes_destino

    @qtd_dependentes_destino.setter
    def qtd_dependentes_destino(self, qtd_dependentes_destino: int):
        self.__qtd_dependentes_destino = qtd_dependentes_destino

    def perfilDestino(destino_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {destino_buscado.id_destino}\n"
        retornoPerfil += f"02. ENDEREÇO: {destino_buscado.endereco_destino}\n"
        retornoPerfil += f"03. RESPONSÁVEL: {destino_buscado.responsavel_destino}\n"
        retornoPerfil += f"04. CELULAR: {destino_buscado.cel_destino}\n"
        retornoPerfil += f"05. QUANTIDADE DE DEPENDENTES: {destino_buscado.qtd_dependentes_destino}\n"
        retornoPerfil += "06. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarDestino(dsn, id_destino, listaDestinos):
        # INSTANCIANDO NOVO DESTINO - OK
        novo_destino = Destino()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVO DESTINO - OK
        id_destino = id_destino

        # SETANDO O ENDEREÇO DO NOVO DESTINO - OK
        try:
            endereco_destino = input(f"DIGITE O ENDEREÇO DO NOVO DESTINO: ")
            endereco_destino = Funcoes.validarPreenchimento(f"DIGITE O ENDEREÇO DO NOVO DESTINO: ", endereco_destino)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ENDEREÇO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO ENDEREÇO DO DESTINO:")
            print(str(e))
    
       # SETANDO O RESPONSÁVEL DO NOVO DESTINO - OK
        try:
            responsavel_destino = input(f"DIGITE O ENDEREÇO DO RESPONSÁVEL DO NOVO DESTINO: ")
            responsavel_destino = Funcoes.validarPreenchimento(f"DIGITE O ENDEREÇO DO RESPONSÁVEL DO NOVO DESTINO: ", responsavel_destino)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ENDEREÇO DO RESPONSÁVEL:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO ENDEREÇO DO RESPONSÁVEL DO DESTINO:")
            print(str(e))
        
        # SETANDO O CELULAR DO NOVO DESTINO - OK
        try:
            cel_destino = input(f"DIGITE O CELULAR DO DESTINO (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
            cel_destino = Funcoes.validarPreenchimento(f"DIGITE O CELULAR DO DESTINO (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ", cel_destino)
            cel_destino = Funcoes.validarCel(cel_destino)
            cel_destino = Funcoes.formatarCel(cel_destino)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO CELULAR:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO CELULAR DO DESTINO:")
            print(str(e))

        # SETANDO O PREÇO DO NOVO DESTINO - OK
        try:
            qtd_dependentes_destino = int(input(f"DIGITE A QUANTIDADE DE DEPENDENTES DO DESTINO (NÚMERO INTEIRO): "))
            qtd_dependentes_destino = int(Funcoes.validarPreenchimento(f"DIGITE A QUANTIDADE DE DEPENDENTES DO DESTINO (NÚMERO INTEIRO): ", qtd_dependentes_destino))

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA QUANTIDADE DE DEPENDENTES:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA QUANTIDADE DE DEPENDENTES DO DESTINO:")
            print(str(e))
        
        # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS - OK
            cursor.execute("INSERT INTO destino (id_destino, endereco_destino, responsavel_destino, cel_destino, qtd_dependentes_destino) VALUES (:1, :2, :3, :4, :5)", (id_destino, endereco_destino, responsavel_destino, cel_destino, qtd_dependentes_destino))
            cursor.connection.commit()

            # FAZENDO UPDATE NO CONSOLE - OK
            novo_destino.id_destino = id_destino
            novo_destino.endereco_destino = endereco_destino
            novo_destino.responsavel_destino = responsavel_destino
            novo_destino.cel_destino = cel_destino
            novo_destino.qtd_dependentes_destino = qtd_dependentes_destino
            listaDestinos.append(novo_destino)
            id_destino = id_destino + 1

            print("DESTINO CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO DESTINO:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
            Funcoes.disconnect(conn, cursor)

    def editarDestino(dsn, listaDestinos):
        perfilDestino = True

        if (len(listaDestinos) == 0):
            input("NENHUM DESTINO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirDestinosAdmin(listaDestinos)
            id_buscado = int(input("DIGITE O ID DO DESTINO QUE DESEJA EDITAR: \n"))
            destino_buscado = Funcoes.buscarDestinoPorId(id_buscado, listaDestinos)
            destino_buscado = Funcoes.validarDestinoBuscado(destino_buscado, listaDestinos)

            while (perfilDestino):
                opcao = int(input(Destino.perfilDestino(destino_buscado)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 6, Destino.perfilDestino(destino_buscado)))

                if (opcao == 1):
                    # EDITAR O ID DO DESTINO - OK
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR O ENDEREÇO DO DESTINO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O ENDEREÇO DO DESTINO DE ID {destino_buscado.id_destino}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O ENDEREÇO DO DESTINO DE ID {destino_buscado.id_destino}")))
                    
                    if (opcao == 1):
                       # EDITAR O ENDEREÇO DO DESTINO - SIM - OK
                       Destino.editarEndereco(dsn, destino_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O ENDEREÇO DO DESTINO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 3):
                    # EDITAR O RESPONSÁVEL DO DESTINO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O RESPONSÁVEL DO DESTINO DE ID {destino_buscado.id_destino}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O RESPONSÁVEL DO DESTINO DE ID {destino_buscado.id_destino}")))
                    
                    if (opcao == 1):
                       # EDITAR O RESPONSÁVEL DO DESTINO - SIM - OK
                       Destino.editarResponsavel(dsn, destino_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O RESPONSÁVEL DO DESTINO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR O CELULAR DO DESTINO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CELULAR DO DESTINO DE ID {destino_buscado.id_destino}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CELULAR DO DESTINO DE ID {destino_buscado.id_destino}")))
                    
                    if (opcao == 1):
                        # EDITAR O CELULAR DO DESTINO - SIM - OK
                       Destino.editarCel(dsn, destino_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O CELULAR DO DESTINO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    # EDITAR A QUANTIDADE DE DEPENDENTES DO DESTINO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A QUANTIDADE DE DEPENDENTES DO DESTINO DE ID {destino_buscado.id_destino}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A QUANTIDADE DE DEPENDENTES DO DESTINO DE ID {destino_buscado.id_destino}")))
                    
                    if (opcao == 1):
                        # EDITAR A QUANTIDADE DE DEPENDENTES DO DESTINO - SIM - OK
                       Destino.editarQuantidadeDependentes(dsn, destino_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A QUANTIDADE DE DEPENDENTES DO DESTINO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 6):
                    perfilDestino = False

    def editarEndereco(dsn, destino_buscado):
        try:
            novo_endereco = input(f"DIGITE O NOVO ENDEREÇO DO DESTINO DE ID {destino_buscado.id_destino}: ")
            novo_endereco = Funcoes.validarPreenchimento(f"DIGITE O NOVO ENDEREÇO DO DESTINO DE ID {destino_buscado.id_destino}: ", novo_endereco)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE destino SET endereco_destino = :novo_endereco WHERE id_destino = :id_destino", {"novo_endereco": novo_endereco, "id_destino": destino_buscado.id_destino})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                destino_buscado.endereco_destino = novo_endereco

                print("ENDEREÇO DO DESTINO EDITADO COM SUCESSO!")

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
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO ENDEREÇO DO DESTINO:")
            print(str(e))

    def editarResponsavel(dsn, destino_buscado):
        try:
            novo_responsavel = input(f"DIGITE O NOME DO NOVO RESPONSÁVEL DO DESTINO DE ID {destino_buscado.id_destino}: ")
            novo_responsavel = Funcoes.validarPreenchimento(f"DIGITE O NOME DO NOVO RESPONSÁVEL DO DESTINO DE ID {destino_buscado.id_destino}: ", novo_responsavel)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE destino SET responsavel_destino = :novo_responsavel WHERE id_destino = :id_destino", {"novo_responsavel": novo_responsavel, "id_destino": destino_buscado.id_destino})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                destino_buscado.responsavel_destino = novo_responsavel

                print("RESPONSÁVEL DO DESTINO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO RESPONSÁVEL:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO RESPONSÁVEL:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO RESPONSÁVEL DO DESTINO:")
            print(str(e))

    def editarCel(dsn, destino_buscado):
        try:
            novo_cel = input(f"DIGITE O NOVO CELULAR DO DESTINO DE ID {destino_buscado.id_destino} (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
            novo_cel = Funcoes.validarPreenchimento(f"DIGITE O NOVO CELULAR DO DESTINO DE ID {destino_buscado.id_destino} (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ", novo_cel)
            novo_cel = Funcoes.validarCel(novo_cel)
            novo_cel = Funcoes.formatarCel(novo_cel)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()
            
            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE destino SET cel_destino = :novo_cel WHERE id_destino = :id_destino", {"novo_cel": novo_cel, "id_destino": destino_buscado.id_destino})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                destino_buscado.cel_destino = novo_cel

                print("CELULAR DO DESTINO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO CELULAR:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO CELULAR:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO CELULAR DO DESTINO:")
            print(str(e))

    def editarQuantidadeDependentes(dsn, destino_buscado):
        try:
            nova_qtd_dependentes_destino = int(input(f"DIGITE A NOVA QUANTIDADE DE DEPENDENTES DO DESTINO DE ID {destino_buscado.id_destino} (NÚMERO INTEIRO): "))
            nova_qtd_dependentes_destino = int(Funcoes.validarPreenchimento(f"DIGITE A NOVA QUANTIDADE DE DEPENDENTES DO DESTINO DE ID {destino_buscado.id_destino} (NÚMERO INTEIRO): ", nova_qtd_dependentes_destino))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE destino SET qtd_dependentes_destino = :nova_qtd_dependentes_destino WHERE id_destino = :id_destino", {"nova_qtd_dependentes_destino": nova_qtd_dependentes_destino, "id_destino": destino_buscado.id_destino})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                destino_buscado.qtd_dependentes_destino = nova_qtd_dependentes_destino

                print("QUANTIDADE DE DEPENDENTES DO DESTINO EDITADA COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA QUANTIDADE DE DEPENDENTES DO DESTINO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA QUANTIDADE DE DEPENDENTES DO DESTINO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA QUANTIDADE DE DEPENDENTES DO DESTINO:")
            print(str(e))

    def excluirDestino(dsn, listaDestinos):
        
        if len(listaDestinos) == 0:
            print("NÃO EXISTEM DESTINOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirDestinosAdmin(listaDestinos)
            try:
                id_buscado = int(input("DIGITE O ID DO DESTINO QUE DESEJA EXCLUIR: \n"))
                destino_buscado = Funcoes.buscarDestinoPorId(id_buscado, listaDestinos)
                destino_buscado = Funcoes.validarDestinoBuscado(destino_buscado, listaDestinos)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O DESTINO")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O DESTINO"))

                if opcao == 1:
                    for i in range(len(listaDestinos)):
                        if listaDestinos[i].id_destino == id_buscado:
                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try: 
                                # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                                cursor.execute("DELETE FROM destino WHERE id_destino = :1", (listaDestinos[i].id_destino,))
                                cursor.connection.commit()

                                del listaDestinos[i]

                                print("DESTINO EXCLUÍDO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A EXCLUSÃO DO DESTINO:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO DESTINO A SER EXCLUÍDO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO DESTINO:")
                print(str(e))
