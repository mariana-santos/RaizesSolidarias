import sqlite3

from datetime import datetime

from Alimento import Alimento
from Funcoes import Funcoes

class Plantio:
    def __init__(self, id_plantio: int = None, data_plantio: str = None, espaco_plantio: int = None, alimento: Alimento = None):
        self.__id_plantio = id_plantio
        self.__data_plantio = data_plantio
        self.__espaco_plantio = espaco_plantio
        self.__alimento = alimento

    @property
    def id_plantio(self) -> int:
        return self.__id_plantio

    @id_plantio.setter
    def id_plantio(self, id_plantio: int):
        self.__id_plantio = id_plantio

    @property
    def data_plantio(self) -> str:
        return self.__data_plantio

    @data_plantio.setter
    def data_plantio(self, data_plantio: str):
        self.__data_plantio = data_plantio

    @property
    def espaco_plantio(self) -> int:
        return self.__espaco_plantio

    @espaco_plantio.setter
    def espaco_plantio(self, espaco_plantio: int):
        self.__espaco_plantio = espaco_plantio

    @property
    def alimento(self) -> Alimento:
        return self.__alimento

    @alimento.setter
    def alimento(self, alimento: Alimento):
        self.__alimento = alimento

    def perfilPlantio(plantio_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {plantio_buscado.id_plantio}\n"
        retornoPerfil += f"02. DATA: {plantio_buscado.data_plantio}\n"
        retornoPerfil += f"03. ESPAÇO: {plantio_buscado.espaco_plantio}\n"
        retornoPerfil += f"04. ALIMENTO: {plantio_buscado.alimento}"
        retornoPerfil += "05. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarPlantio(dsn, id_plantio, listaPlantios, listaAlimentos):
        # INSTANCIANDO NOVO PLANTIO - OK
        novo_plantio = Plantio()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVO PLANTIO - OK
        id_plantio = id_plantio

        # SETANDO A DATA DO NOVO PLANTIO - OK
        try:
            data_plantio = input(f"DIGITE A DATA DO PLANTIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            data_plantio = Funcoes.validarPreenchimento(f"DIGITE A DATA DO PLANTIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", data_plantio)
            data_formatada = datetime.strptime(data_plantio, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%Y-%m-%d")

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA DATA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA DATA DO PLANTIO:")
            print(str(e))
    
        # SETANDO O ESPAÇO DO NOVO PLANTIO - OK
        try:
            espaco_plantio = int(input(f"DIGITE O ESPAÇO DO PLANTIO: "))
            espaco_plantio = int(Funcoes.validarPreenchimento(f"DIGITE O ESPAÇO DO PLANTIO: ", espaco_plantio))

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ESPAÇO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO ESPAÇO DO PLANTIO:")
            print(str(e))

        # SETANDO O ALIMENTO DO NOVO PLANTIO - OK
        try:
            if (len(listaAlimentos) == 0):
                input("NENHUM ALIMENTO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                Funcoes.exibirAlimentosAdmin(listaAlimentos)
                id_buscado = int(input("DIGITE O ID DO ALIMENTO QUE DESEJA INCLUIR AO PLANTIO: \n"))
                alimento_buscado = Funcoes.buscarAlimentoPorId(id_buscado, listaAlimentos)
                alimento_buscado = Funcoes.validarAlimentoBuscado(alimento_buscado, listaAlimentos)
                
                alimento_plantio = Alimento()
                alimento_plantio.id_alimento = alimento_buscado.id_alimento
                alimento_plantio.nome_alimento = alimento_buscado.nome_alimento
                alimento_plantio.tempo_colheita = alimento_buscado.tempo_colheita
                alimento_plantio.qtd_irrigacao = alimento_buscado.qtd_irrigacao
                alimento_plantio.preco_alimento = alimento_buscado.preco_alimento
                alimento_plantio.qtd_alimento = alimento_buscado.qtd_alimento
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO ALIMENTO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO ALIMENTO DO PLANTIO:")
            print(str(e))
        
        # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS - OK
            cursor.execute("INSERT INTO plantio (id_plantio, data_plantio, espaco_plantio, id_alimento) VALUES (:1, :2, :3, :4)", (id_plantio, data_formatada_banco, espaco_plantio, alimento_plantio.id_alimento))
            cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE - OK
            novo_plantio.id_plantio = id_plantio
            novo_plantio.data_plantio = data_formatada
            novo_plantio.espaco_plantio = espaco_plantio
            novo_plantio.alimento = alimento_plantio
            listaPlantios.append(novo_plantio)
            id_plantio = id_plantio + 1

            print("PLANTIO CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO PLANTIO:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
            Funcoes.disconnect(conn, cursor)

    def editarPlantio(dsn, listaPlantios):
        perfilPlantio = True

        if (len(listaPlantios) == 0):
            input("NENHUM PLANTIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirPlantiosAdmin(listaPlantios)
            id_buscado = int(input("DIGITE O ID DO PLANTIO QUE DESEJA EDITAR: \n"))
            plantio_buscado = Funcoes.buscarPlantioPorId(id_buscado, listaPlantios)
            plantio_buscado = Funcoes.validarPlantioBuscado(plantio_buscado, listaPlantios)

            while (perfilPlantio):
                opcao = int(input(Plantio.perfilPlantio(plantio_buscado)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 5, Plantio.perfilPlantio(plantio_buscado)))

                if (opcao == 1):
                    # EDITAR O ID DO PLANTIO - OK
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR A DATA DO PLANTIO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DATA DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DATA DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    
                    if (opcao == 1):
                       # EDITAR A DATA DO PLANTIO - SIM - OK
                       Plantio.editarData(dsn, plantio_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A DATA DO PLANTIO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 3):
                    # EDITAR O ESPAÇO DO PLANTIO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O ESPAÇO DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O ESPAÇO DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    
                    if (opcao == 1):
                       # EDITAR O ESPAÇO DO PLANTIO - SIM - OK
                       Plantio.editarEspaco(dsn, plantio_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O ESPAÇO DO PLANTIO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 4):
                    # EDITAR O ALIMENTO DO PLANTIO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O ALIMENTO DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O ALIMENTO DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    
                    if (opcao == 1):
                       # EDITAR O ALIMENTO DO PLANTIO - SIM - OK
                       Plantio.editarAlimento(dsn, plantio_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O ALIMENTO DO PLANTIO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 5):
                    perfilPlantio = False

    def editarData(dsn, plantio_buscado):
        try:
            nova_data = input(f"DIGITE A NOVA DATA DO PLANTIO DE ID {plantio_buscado.id_plantio} (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            nova_data = Funcoes.validarPreenchimento(f"DIGITE A NOVA DATA DO PLANTIO DE ID {plantio_buscado.id_plantio} (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", nova_data)
            data_formatada = datetime.strptime(nova_data, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%Y-%m-%d")

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE plantio SET data_plantio = :data_formatada_banco WHERE id_plantio = :id_plantio", {"data_formatada_banco": data_formatada_banco, "id_plantio": plantio_buscado.id_plantio})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                plantio_buscado.data_plantio = data_formatada

                print("DATA DO PLANTIO EDITADA COM SUCESSO!")

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
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA DATA DO PLANTIO:")
            print(str(e))
    
    def editarEspaco(dsn, plantio_buscado):
        try:
            novo_espaco = int(input(f"DIGITE O NOVO ESPAÇO DO PLANTIO DE ID {plantio_buscado.id_plantio}: "))
            novo_espaco = int(Funcoes.validarPreenchimento(f"DIGITE O NOVO ESPAÇO DO PLANTIO DE ID {plantio_buscado.id_plantio}: ", novo_espaco))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE plantio SET espaco_plantio = :novo_espaco WHERE id_plantio = :id_plantio", {"novo_espaco": novo_espaco, "id_plantio": plantio_buscado.id_plantio})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                plantio_buscado.espaco_plantio = novo_espaco

                print("ESPAÇO DO PLANTIO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO ESPAÇO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO ESPAÇO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO ESPAÇO DO PLANTIO:")
            print(str(e))

    def editarAlimento(dsn, plantio_buscado, listaAlimentos):
        try:
            if (len(listaAlimentos) == 0):
                input("NENHUM ALIMENTO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                Funcoes.exibirAlimentosAdmin(listaAlimentos)
                id_buscado = int(input("DIGITE O ID DO ALIMENTO QUE DESEJA INCLUIR AO PLANTIO: \n"))
                alimento_buscado = Funcoes.buscarAlimentoPorId(id_buscado, listaAlimentos)
                alimento_buscado = Funcoes.validarAlimentoBuscado(alimento_buscado, listaAlimentos)
                
                novo_alimento = Alimento()
                novo_alimento.id_alimento = alimento_buscado.id_alimento
                novo_alimento.nome_alimento = alimento_buscado.nome_alimento
                novo_alimento.tempo_colheita = alimento_buscado.tempo_colheita
                novo_alimento.qtd_irrigacao = alimento_buscado.qtd_irrigacao
                novo_alimento.preco_alimento = alimento_buscado.preco_alimento
                novo_alimento.qtd_alimento = alimento_buscado.qtd_alimento

                # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
                conn = Funcoes.connect(dsn)
                cursor = conn.cursor()

                try:           
                    # FAZENDO UPDATE NO BANCO DE DADOS - OK
                    cursor.execute("UPDATE plantio SET id_alimento = :novo_alimento.id_alimento WHERE id_plantio = :id_plantio", {"novo_alimento.id_alimento": novo_alimento.id_alimento, "id_plantio": plantio_buscado.id_plantio})
                    cursor.connection.commit()

                    # FAZENDO UPDATE NO CONSOLE - OK
                    plantio_buscado.alimento = novo_alimento

                    print("ALIMENTO DO PLANTIO EDITADO COM SUCESSO!")

                except sqlite3.DatabaseError as db_error:
                    print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO ALIMENTO:")
                    print(str(db_error))

                finally:
                    # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                    Funcoes.disconnect(conn, cursor)
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO ALIMENTO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO ALIMENTO DO PLANTIO:")
            print(str(e))

    def excluirPlantio(dsn, listaPlantios):
        
        if len(listaPlantios) == 0:
            print("NÃO EXISTEM PLANTIOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirPlantiosAdmin(listaPlantios)
            try:
                id_buscado = int(input("DIGITE O ID DO PLANTIO QUE DESEJA EXCLUIR: \n"))
                plantio_buscado = Funcoes.buscarPlantioPorId(id_buscado, listaPlantios)
                plantio_buscado = Funcoes.validarPlantioBuscado(plantio_buscado, listaPlantios)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O PLANTIO")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O PLANTIO"))

                if opcao == 1:
                    for i in range(len(listaPlantios)):
                        if listaPlantios[i].id_plantio == id_buscado:
                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try: 
                                # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                                cursor.execute("DELETE FROM plantio WHERE id_plantio = :1", (listaPlantios[i].id_plantio,))
                                cursor.connection.commit()

                                del listaPlantios[i]

                                print("PLANTIO EXCLUÍDO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A EXCLUSÃO DO PLANTIO:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO PLANTIO A SER EXCLUÍDO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO PLANTIO:")
                print(str(e))
