import sqlite3

from datetime import datetime

from Doador import Doador
from Funcoes import Funcoes

class Doacao:
    def __init__(self, id_doacao: int = None, doador: Doador = None, data_doacao: str = None, qtd_moedas_doacao: int = None):
        self._id_doacao = id_doacao
        self._doador = doador
        self._data_doacao = data_doacao
        self._qtd_moedas_doacao = qtd_moedas_doacao

    @property
    def id_doacao(self) -> int:
        return self._id_doacao

    @id_doacao.setter
    def id_doacao(self, id_doacao: int):
        self._id_doacao = id_doacao

    @property
    def doador(self) -> Doador:
        return self._doador

    @doador.setter
    def doador(self, doador: Doador):
        self._doador = doador

    @property
    def data_doacao(self) -> str:
        return self._data_doacao

    @data_doacao.setter
    def data_doacao(self, data_doacao: str):
        self._data_doacao = data_doacao

    @property
    def qtd_moedas_doacao(self) -> int:
        return self._qtd_moedas_doacao

    @qtd_moedas_doacao.setter
    def qtd_moedas_doacao(self, qtd_moedas_doacao: int):
        self._qtd_moedas_doacao = qtd_moedas_doacao

    def perfilDoacao(doacao_buscada):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {doacao_buscada.id_doacao}\n"
        retornoPerfil += f"02. DOADOR: {doacao_buscada.doador.nome_usuario}\n"
        retornoPerfil += f"03. DATA: {doacao_buscada.data_doacao}\n"
        retornoPerfil += f"04. QUANTIDADE DE MOEDAS: {doacao_buscada.qtd_moedas_doacao}\n"
        retornoPerfil += "05. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarDoacao(dsn, id_doacao, listaDoacoes, listaDoadores):
        # INSTANCIANDA NOVA DOAÇÃO
        novo_doacao = Doacao()

        Funcoes.menuCabecalho

        # SETANDO O ID DA NOVA DOAÇÃO
        id_doacao = id_doacao

        # SETANDO O DOADOR DA NOVA DOAÇÃO
        try:
            Funcoes.exibirDoacoesAdmin(listaDoacoes)
            id_buscado = int(input("DIGITE O ID DO DOADOR QUE DESEJA INCLUIR À DOAÇÃO: \n"))
            doador_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaDoadores)
            doador_buscado = Funcoes.validarUsuarioBuscado(doador_buscado, listaDoadores)

            doador = Doador()
            doador.id_usuario = doador_buscado.id_usuario
            doador.cpf_usuario = doador_buscado.cpf_usuario
            doador.nome_usuario = doador_buscado.nome_usuario
            doador.email_usuario = doador_buscado.email_usuario
            doador.cel_usuario = doador_buscado.cel_usuario
            doador.senha_usuario = doador_buscado.senha_usuario
            doador.status_usuario = doador_buscado.status_usuario
            doador.nivel_doador = doador_buscado.nivel_doador
            doador.moedas_doador = doador_buscado.moedas_doador

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO DOADOR:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO DOADOR DA DOAÇÃO:")
            print(str(e))

        # SETANDO A DATA DA NOVA DOAÇÃO
        try:
            data_doacao = input(f"DIGITE A DATA DA DOAÇÃO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            data_doacao = Funcoes.validarPreenchimento(f"DIGITE A DATA DA DOAÇÃO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", data_doacao)
            data_formatada = datetime.strptime(data_doacao, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%Y-%m-%d")
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA DATA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA DATA DA DOAÇÃO:")
            print(str(e))

        # SETANDO A QUANTIDADE DE MOEDAS DA NOVA DOAÇÃO
        try:
            qtd_moedas_doacao = int(input(f"DIGITE A QUANTIDADE DE MOEDAS DA DOAÇÃO (NÚMERO INTEIRO): "))
            qtd_moedas_doacao = int(Funcoes.validarPreenchimento(f"DIGITE A QUANTIDADE DE MOEDAS DA DOAÇÃO (NÚMERO INTEIRO): ", qtd_moedas_doacao))

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA QUANTIDADE DE MOEDAS:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA QUANTIDADE DE MOEDAS DA DOAÇÃO:")
            print(str(e))
        
        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS
            cursor.execute("INSERT INTO doacao (id_doacao, doador, data_doacao, qtd_moedas_doacao) VALUES (:1, :2, :3, :4)", (id_doacao, doador, data_formatada_banco, qtd_moedas_doacao))
            cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE
            novo_doacao.id_doacao = id_doacao
            novo_doacao.doador = doador
            novo_doacao.data_doacao = data_formatada
            novo_doacao.qtd_moedas_doacao = qtd_moedas_doacao
            listaDoacoes.append(novo_doacao)

            print("DOAÇÃO CADASTRADA COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DA DOAÇÃO:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

    def editarDoacao(dsn, listaDoacoes, listaDoadores):
        perfilDoacao = True

        if (len(listaDoacoes) == 0):
            input("NENHUMA DOAÇÃO CADASTRADA. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirDoacoesAdmin(listaDoacoes)
            id_buscado = int(input("DIGITE O ID DA DOAÇÃO QUE DESEJA EDITAR: \n"))
            doacao_buscada = Funcoes.buscarDoacaoPorId(id_buscado, listaDoacoes)
            doacao_buscada = Funcoes.validarDoacaoBuscada(doacao_buscada, listaDoacoes)

            while (perfilDoacao):
                opcao = int(input(Doacao.perfilDoacao(doacao_buscada)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 5, Doacao.perfilDoacao(doacao_buscada)))

                if (opcao == 1):
                    # EDITAR O ID DA DOAÇÃO
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR O DOADOR DA DOAÇÃO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O DOADOR DA DOAÇÃO DE ID {doacao_buscada.id_doacao}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O DOADOR DA DOAÇÃO DE ID {doacao_buscada.id_doacao}")))
                    
                    if (opcao == 1):
                       # EDITAR O DOADOR DA DOAÇÃO - SIM
                       Doacao.editarDoador(dsn, doacao_buscada, listaDoadores)
                    
                    elif (opcao == 2):
                        # EDITAR O DOADOR DA DOAÇÃO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 3):
                    # EDITAR A DATA DA DOAÇÃO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DATA DA DOAÇÃO DE ID {doacao_buscada.id_doacao}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DATA DA DOAÇÃO DE ID {doacao_buscada.id_doacao}")))
                    
                    if (opcao == 1):
                       # EDITAR A DATA DA DOAÇÃO - SIM
                       Doacao.editarData(dsn, doacao_buscada)
                    
                    elif (opcao == 2):
                        # EDITAR A DATA DA DOAÇÃO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR A QUANTIDADE DE MOEDAS DA DOAÇÃO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A QUANTIDADE DE MOEDAS DA DOAÇÃO DE ID {doacao_buscada.id_doacao}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A QUANTIDADE DE MOEDAS DA DOAÇÃO DE ID {doacao_buscada.id_doacao}")))
                    
                    if (opcao == 1):
                        # EDITAR A QUANTIDADE DE MOEDAS DA DOAÇÃO - SIM
                       Doacao.editarQuantidadeMoedas(dsn, doacao_buscada)
                    
                    elif (opcao == 2):
                        # EDITAR A QUANTIDADE DE MOEDAS DA DOAÇÃO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    perfilDoacao = False

    def editarDoador(dsn, doacao_buscada, listaDoadores):
        try:
            if (len(listaDoadores) == 0):
                input("NENHUM DOADOR CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                Funcoes.exibirUsuariosAdmin(listaDoadores)
                id_buscado = int(input("DIGITE O ID DO DOADOR QUE DESEJA INCLUIR À DOAÇÃO: \n"))
                doador_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaDoadores)
                doador_buscado = Funcoes.validarUsuarioBuscado(doador_buscado, listaDoadores)

                novo_doador = Doador()
                novo_doador.id_usuario = doador_buscado.id_usuario
                novo_doador.cpf_usuario = doador_buscado.cpf_usuario
                novo_doador.nome_usuario = doador_buscado.nome_usuario
                novo_doador.email_usuario = doador_buscado.email_usuario
                novo_doador.cel_usuario = doador_buscado.cel_usuario
                novo_doador.senha_usuario = doador_buscado.senha_usuario
                novo_doador.status_usuario = doador_buscado.status_usuario
                novo_doador.nivel_doador = doador_buscado.nivel_doador
                novo_doador.moedas_doador = doador_buscado.moedas_doador
                
                # CRIANDO CONEXÃO COM O BANCO DE DADOS
                conn = Funcoes.connect(dsn)
                cursor = conn.cursor()

                try:           
                    # FAZENDO UPDATE NO BANCO DE DADOS
                    cursor.execute("UPDATE doacao SET doador = :novo_doador WHERE id_doacao = :id_doacao", {"novo_doador": novo_doador, "id_doacao": doacao_buscada.id_doacao})
                    cursor.connection.commit()

                    # FAZENDO UPDATE NO CONSOLE
                    doacao_buscada.doador = novo_doador

                    print("USUÁRIO (DOADOR) DA DOAÇÃO EDITADO COM SUCESSO!")

                except sqlite3.DatabaseError as db_error:
                    print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA DOAÇÃO:")
                    print(str(db_error))

                finally:
                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA DOAÇÃO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO USUÁRIO (DOADOR) DA DOAÇÃO:")
            print(str(e))

    def editarData(dsn, doacao_buscada):
        try:
            data_doacao = input(f"DIGITE A NOVA DATA DA DOAÇÃO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            data_doacao = Funcoes.validarPreenchimento(f"DIGITE A NOVA DATA DA DOAÇÃO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", data_doacao)
            data_formatada = datetime.strptime(data_doacao, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%Y-%m-%d")

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE doacao SET data_doacao = :data_formatada_banco WHERE id_doacao = :id_doacao", {"data_formatada_banco": data_formatada_banco, "id_doacao": doacao_buscada.id_doacao})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                doacao_buscada.data_doacao = data_formatada

                print("DATA DA DOAÇÃO EDITADA COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA DATA:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA DATA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA DATA DA DOAÇÃO:")
            print(str(e))

    def editarQuantidadeMoedas(dsn, doacao_buscada):
        try:
            nova_qtd_moedas_doacao = int(input(f"DIGITE A NOVA QUANTIDADE DE MOEDAS DA DOAÇÃO DE ID {doacao_buscada.id_doacao} (NÚMERO INTEIRO): "))
            nova_qtd_moedas_doacao = int(Funcoes.validarPreenchimento(f"DIGITE A NOVA QUANTIDADE DE MOEDAS DA DOAÇÃO DE ID {doacao_buscada.id_doacao} (NÚMERO INTEIRO): ", nova_qtd_moedas_doacao))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE doacao SET qtd_moedas_doacao = :nova_qtd_moedas_doacao WHERE id_doacao = :id_doacao", {"nova_qtd_moedas_doacao": nova_qtd_moedas_doacao, "id_doacao": doacao_buscada.id_doacao})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                doacao_buscada.qtd_moedas_doacao = nova_qtd_moedas_doacao

                print("QUANTIDADE DE MOEDAS DA DOAÇÃO EDITADA COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA QUANTIDADE DE MOEDAS:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA QUANTIDADE DE MOEDAS:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA QUANTIDADE DE MOEDAS DA DOAÇÃO:")
            print(str(e))

    def excluirDoacao(dsn, listaDoacoes):
        
        if len(listaDoacoes) == 0:
            print("NÃO EXISTEM DOAÇÕES CADASTRADAS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirDoacoesAdmin(listaDoacoes)
            try:
                id_buscado = int(input("DIGITE O ID DA DOAÇÃO QUE DESEJA EXCLUIR: \n"))
                doacao_buscada = Funcoes.buscarDoacaoPorId(id_buscado, listaDoacoes)
                doacao_buscada = Funcoes.validarDoacaoBuscada(doacao_buscada, listaDoacoes)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR A DOAÇÃO")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR A DOAÇÃO"))

                if opcao == 1:
                    for i in range(len(listaDoacoes)):
                        if listaDoacoes[i].id_doacao == id_buscado:
                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try: 
                                # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                                cursor.execute("DELETE FROM doacao WHERE id_doacao = :1", (listaDoacoes[i].id_doacao,))
                                cursor.connection.commit()

                                del listaDoacoes[i]

                                print("DOAÇÃO EXCLUÍDA COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A EXCLUSÃO DA DOAÇÃO:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DA DOAÇÃO A SER EXCLUÍDA:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DA DOAÇÃO:")
                print(str(e))
