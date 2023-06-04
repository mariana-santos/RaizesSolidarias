import sqlite3

from Funcoes import Funcoes

class Alimento:
    def __init__(self, id_alimento: int = None, nome_alimento: str = None, tempo_colheita: int = None, qtd_irrigacao: int = None, preco_alimento: int = None, qtd_alimento: int = None):
        self._id_alimento = id_alimento
        self._nome_alimento = nome_alimento
        self._tempo_colheita = tempo_colheita
        self._qtd_irrigacao = qtd_irrigacao
        self._preco_alimento = preco_alimento
        self._qtd_alimento = qtd_alimento
    
    @property
    def id_alimento(self) -> int:
        return self._id_alimento
    
    @id_alimento.setter
    def id_alimento(self, id_alimento: int):
        self._id_alimento = id_alimento
    
    @property
    def nome_alimento(self) -> str:
        return self._nome_alimento
    
    @nome_alimento.setter
    def nome_alimento(self, nome_alimento: str):
        self._nome_alimento = nome_alimento
    
    @property
    def tempo_colheita(self) -> int:
        return self._tempo_colheita
    
    @tempo_colheita.setter
    def tempo_colheita(self, tempo_colheita: int):
        self._tempo_colheita = tempo_colheita
    
    @property
    def qtd_irrigacao(self) -> int:
        return self._qtd_irrigacao
    
    @qtd_irrigacao.setter
    def qtd_irrigacao(self, qtd_irrigacao: int):
        self._qtd_irrigacao = qtd_irrigacao
    
    @property
    def preco_alimento(self) -> int:
        return self._preco_alimento
    
    @preco_alimento.setter
    def preco_alimento(self, preco_alimento: int):
        self._preco_alimento = preco_alimento
    
    @property
    def qtd_alimento(self) -> int:
        return self._qtd_alimento
    
    @qtd_alimento.setter
    def qtd_alimento(self, qtd_alimento: int):
        self._qtd_alimento = qtd_alimento
    
    def perfilAlimento(alimento_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {alimento_buscado.id_alimento}\n"
        retornoPerfil += f"02. NOME: {alimento_buscado.nome_alimento}\n"
        retornoPerfil += f"03. TEMPO DE COLHEITA: {alimento_buscado.tempo_colheita}\n"
        retornoPerfil += f"04. QUANTIDADE DE IRRIGAÇÃO: {alimento_buscado.qtd_irrigacao}\n"
        retornoPerfil += f"05. PREÇO: {alimento_buscado.preco_alimento}\n"
        retornoPerfil += f"06. QUANTIDADE: {alimento_buscado.qtd_alimento}\n"
        retornoPerfil += "07. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarAlimento(dsn, id_alimento, listaAlimentos):
        # INSTANCIANDO NOVO ALIMENTO
        novo_alimento = Alimento()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVO ALIMENTO
        id_alimento = id_alimento

        # SETANDO O NOME DO NOVO ALIMENTO
        try:
            nome_alimento = input(f"DIGITE O NOME DO NOVO ALIMENTO: ")
            nome_alimento = Funcoes.validarPreenchimento(f"DIGITE O NOME DO NOVO ALIMENTO: ", nome_alimento)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOME:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO NOME DO ALIMENTO:")
            print(str(e))
    
       # SETANDO O TEMPO DE COLHEITA DO NOVO ALIMENTO
        try:
            tempo_colheita = int(input(f"DIGITE O TEMPO DE COLHEITA DO NOVO ALIMENTO (EM DIAS (NÚMERO INTEIRO)): "))
            tempo_colheita = int(Funcoes.validarPreenchimento(f"DIGITE O TEMPO DE COLHEITA DO NOVO ALIMENTO (EM DIAS (NÚMERO INTEIRO)): ", tempo_colheita))

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO TEMPO DE COLHEITA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO TEMPO DE COLHEITA DO ALIMENTO:")
            print(str(e))
        
        # SETANDO A QUANTIDADE DE IRRIGAÇÃO DO NOVO ALIMENTO
        try:
            qtd_irrigacao = int(input(f"DIGITE A QUANTIDADE DE IRRIGAÇÃO DO NOVO ALIMENTO (QUANTAS VEZES POR DIA (NÚMERO INTEIRO)): "))
            qtd_irrigacao = int(Funcoes.validarPreenchimento(f"DIGITE A QUANTIDADE DE IRRIGAÇÃO DO NOVO ALIMENTO (QUANTAS VEZES POR DIA (NÚMERO INTEIRO)): ", qtd_irrigacao))

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA QUANTIDADE DE IRRICAÇÃO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA QUANTIDADE DE IRRIGAÇÃO DO ALIMENTO:")
            print(str(e))

        # SETANDO O PREÇO DO NOVO ALIMENTO
        try:
            preco_alimento = int(input(f"DIGITE O PREÇO DO NOVO ALIMENTO (EM MOEDAS (NÚMERO INTEIRO)): "))
            preco_alimento = int(Funcoes.validarPreenchimento(f"DIGITE O PREÇO DO NOVO ALIMENTO (EM MOEDAS (NÚMERO INTEIRO)): ", preco_alimento))

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO PREÇO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO PREÇO DO ALIMENTO:")
            print(str(e))

        # SETANDO A QUANTIDADE DO NOVO ALIMENTO
        try:
            qtd_alimento = int(input(f"DIGITE A QUANTIDADE DO NOVO ALIMENTO (NÚMERO INTEIRO): "))
            qtd_alimento = int(Funcoes.validarPreenchimento(f"DIGITE A QUANTIDADE DO NOVO ALIMENTO (NÚMERO INTEIRO): ", qtd_alimento))

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA QUANTIDADE:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA QUANTIDADE DO ALIMENTO:")
            print(str(e))
        
        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS
            cursor.execute("INSERT INTO alimento (id_alimento, nome_alimento, tempo_colheita, qtd_irrigacao, preco_alimento, qtd_alimento) VALUES (:1, :2, :3, :4, :5, :6)", (id_alimento, nome_alimento, tempo_colheita, qtd_irrigacao, preco_alimento, qtd_alimento))
            cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE
            novo_alimento.id_alimento = id_alimento
            novo_alimento.nome_alimento = nome_alimento
            novo_alimento.tempo_colheita = tempo_colheita
            novo_alimento.qtd_irrigacao = qtd_irrigacao
            novo_alimento.preco_alimento = preco_alimento
            novo_alimento.qtd_alimento = qtd_alimento
            listaAlimentos.append(novo_alimento)

            print("ALIMENTO CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO ALIMENTO:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

    def editarAlimento(dsn, listaAlimentos):
        perfilAlimento = True

        if (len(listaAlimentos) == 0):
            input("NENHUM ALIMENTO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirAlimentosAdmin(listaAlimentos)
            id_buscado = int(input("DIGITE O ID DO ALIMENTO QUE DESEJA EDITAR: \n"))
            alimento_buscado = Funcoes.buscarAlimentoPorId(id_buscado, listaAlimentos)
            alimento_buscado = Funcoes.validarAlimentoBuscado(alimento_buscado, listaAlimentos)

            while (perfilAlimento):
                opcao = int(input(Alimento.perfilAlimento(alimento_buscado)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 7, Alimento.perfilAlimento(alimento_buscado)))

                if (opcao == 1):
                    # EDITAR O ID DO ALIMENTO
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR O NOME DO ALIMENTO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO ALIMENTO DE ID {alimento_buscado.id_alimento}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO ALIMENTO DE ID {alimento_buscado.id_alimento}")))
                    
                    if (opcao == 1):
                       # EDITAR O NOME DO ALIMENTO - SIM
                       Alimento.editarNome(dsn, alimento_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O NOME DO ALIMENTO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 3):
                    # EDITAR O TEMPO DE COLHEITA DO ALIMENTO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O TEMPO DE COLHEITA DO ALIMENTO DE ID {alimento_buscado.id_alimento}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O TEMPO DE COLHEITA DO ALIMENTO DE ID {alimento_buscado.id_alimento}")))
                    
                    if (opcao == 1):
                       # EDITAR O TEMPO DE COLHEITA DO ALIMENTO - SIM
                       Alimento.editarTempoColheita(dsn, alimento_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O TEMPO DE COLHEITA DO ALIMENTO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR A QUANTIDADE DE IRRIGAÇÃO DO ALIMENTO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A QUANTIDADE DE IRRIGAÇÃO DO ALIMENTO DE ID {alimento_buscado.id_alimento}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A QUANTIDADE DE IRRIGAÇÃO DO ALIMENTO DE ID {alimento_buscado.id_alimento}")))
                    
                    if (opcao == 1):
                        # EDITAR A QUANTIDADE DE IRRIGAÇÃO DO ALIMENTO - SIM
                       Alimento.editarQtdIrrigacao(dsn, alimento_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A QUANTIDADE DE IRRIGAÇÃO DO ALIMENTO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    # EDITAR O PREÇO DO ALIMENTO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O PREÇO DO ALIMENTO DE ID {alimento_buscado.id_alimento}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O PREÇO DO ALIMENTO DE ID {alimento_buscado.id_alimento}")))
                    
                    if (opcao == 1):
                        # EDITAR O PREÇO DO ALIMENTO - SIM
                       Alimento.editarPreco(dsn, alimento_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O PREÇO DO ALIMENTO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 6):
                    # EDITAR A QUANTIDADE DO ALIMENTO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A QUANTIDADE DO ALIMENTO DE ID {alimento_buscado.id_alimento}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A QUANTIDADE DO ALIMENTO DE ID {alimento_buscado.id_alimento}")))
                    
                    if (opcao == 1):
                        # EDITAR A QUANTIDADE DO ALIMENTO - SIM
                       Alimento.editarQuantidade(dsn, alimento_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A QUANTIDADE DO ALIMENTO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 7):
                    perfilAlimento = False

    def editarNome(dsn, alimento_buscado):
        try:
            novo_nome = input(f"DIGITE O NOVO NOME DO ALIMENTO {alimento_buscado.nome_alimento}: ")
            novo_nome = Funcoes.validarPreenchimento(f"DIGITE O NOVO NOME DO ALIMENTO {alimento_buscado.nome_alimento}: ", novo_nome)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE alimento SET nome_alimento = :novo_nome WHERE id_alimento = :id_alimento", {"novo_nome": novo_nome, "id_alimento": alimento_buscado.id_alimento})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                alimento_buscado.nome_alimento = novo_nome

                print("NOME DO ALIMENTO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO NOME:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO NOME:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO NOME DO ALIMENTO:")
            print(str(e))

    def editarTempoColheita(dsn, alimento_buscado):
        try:
            novo_tempo_colheita = int(input(f"DIGITE O NOVO TEMPO DE COLHEITA DO ALIMENTO {alimento_buscado.nome_alimento} (EM DIAS (NÚMERO INTEIRO)): "))
            novo_tempo_colheita = int(Funcoes.validarPreenchimento(f"DIGITE O NOVO TEMPO DE COLHEITA DO ALIMENTO {alimento_buscado.nome_alimento} (EM DIAS (NÚMERO INTEIRO)): ", novo_tempo_colheita))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE alimento SET tempo_colheita = :novo_tempo_colheita WHERE id_alimento = :id_alimento", {"novo_tempo_colheita": novo_tempo_colheita, "id_alimento": alimento_buscado.id_alimento})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                alimento_buscado.tempo_colheita = novo_tempo_colheita

                print("TEMPO DE COLHEITA DO ALIMENTO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO TEMPO DE COLHEITA:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO TEMPO DE COLHEITA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO TEMPO DE COLHEITA DO ALIMENTO:")
            print(str(e))

    def editarQtdIrrigacao(dsn, alimento_buscado):
        try:
            nova_qtd_irrigacao = int(input(f"DIGITE A NOVA QUANTIDADE DE IRRIGAÇÃO DO ALIMENTO {alimento_buscado.nome_alimento} (QUANTAS VEZES POR DIA (NÚMERO INTEIRO)): "))
            nova_qtd_irrigacao = int(Funcoes.validarPreenchimento(f"DIGITE A NOVA QUANTIDADE DE IRRIGAÇÃO DO ALIMENTO {alimento_buscado.nome_alimento} (QUANTAS VEZES POR DIA (NÚMERO INTEIRO)): ", nova_qtd_irrigacao))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE alimento SET qtd_irrigacao = :nova_qtd_irrigacao WHERE id_alimento = :id_alimento", {"nova_qtd_irrigacao": nova_qtd_irrigacao, "id_alimento": alimento_buscado.id_alimento})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                alimento_buscado.qtd_irrigacao = nova_qtd_irrigacao

                print("QUANTIDADE DE IRRIGAÇÃO DO ALIMENTO EDITADA COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA QUANTIDADE DE IRRIGAÇÃO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA QUANTIDADE DE IRRIGAÇÃO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA QUANTIDADE DE IRRIGAÇÃO DO ALIMENTO:")
            print(str(e))
    
    def editarPreco(dsn, alimento_buscado):
        try:
            novo_preco_alimento = int(input(f"DIGITE O NOVO PREÇO DO ALIMENTO {alimento_buscado.nome_alimento} (EM MOEDAS (NÚMERO INTEIRO)): "))
            novo_preco_alimento = int(Funcoes.validarPreenchimento(f"DIGITE O NOVO PREÇO DO ALIMENTO {alimento_buscado.nome_alimento} (EM MOEDAS (NÚMERO INTEIRO)): ", novo_preco_alimento))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE alimento SET preco_alimento = :novo_preco_alimento WHERE id_alimento = :id_alimento", {"novo_preco_alimento": novo_preco_alimento, "id_alimento": alimento_buscado.id_alimento})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                alimento_buscado.preco_alimento = novo_preco_alimento

                print("PREÇO DO ALIMENTO EDITADA COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO PREÇO DO ALIMENTO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO PREÇO DO ALIMENTO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO PREÇO DO ALIMENTO:")
            print(str(e))
    
    def editarQuantidade(dsn, alimento_buscado):
        try:
            nova_qtd_alimento = int(input(f"DIGITE A NOVA QUANTIDADE DO ALIMENTO {alimento_buscado.nome_alimento} (NÚMERO INTEIRO): "))
            nova_qtd_alimento = int(Funcoes.validarPreenchimento(f"DIGITE A NOVA QUANTIDADE DO ALIMENTO {alimento_buscado.nome_alimento} (NÚMERO INTEIRO): ", nova_qtd_alimento))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE alimento SET qtd_alimento = :nova_qtd_alimento WHERE id_alimento = :id_alimento", {"nova_qtd_alimento": nova_qtd_alimento, "id_alimento": alimento_buscado.id_alimento})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                alimento_buscado.qtd_alimento = nova_qtd_alimento

                print("QUANTIDADE DO ALIMENTO EDITADA COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA QUANTIDADE DO ALIMENTO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA QUANTIDADE DO ALIMENTO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA QUANTIDADE DO ALIMENTO:")
            print(str(e))

    def excluirAlimento(dsn, listaAlimentos):
        
        if len(listaAlimentos) == 0:
            print("NÃO EXISTEM ALIMENTOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirAlimentosAdmin(listaAlimentos)
            try:
                id_buscado = int(input("DIGITE O ID DO ALIMENTO QUE DESEJA EXCLUIR: \n"))
                alimento_buscado = Funcoes.buscarAlimentoPorId(id_buscado, listaAlimentos)
                alimento_buscado = Funcoes.validarAlimentoBuscado(alimento_buscado, listaAlimentos)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O ALIMENTO")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O ALIMENTO"))

                if opcao == 1:
                    for i in range(len(listaAlimentos)):
                        if listaAlimentos[i].id_alimento == id_buscado:
                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try: 
                                # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                                cursor.execute("DELETE FROM alimento WHERE id_alimento = :1", (listaAlimentos[i].id_alimento,))
                                cursor.connection.commit()

                                del listaAlimentos[i]

                                print("ALIMENTO EXCLUÍDO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A EXCLUSÃO DO ALIMENTO:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO ALIMENTO A SER EXCLUÍDO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO ALIMENTO:")
                print(str(e))
