import sqlite3

from datetime import datetime

from Funcoes import Funcoes
from Usuario import Usuario

class Agendamento:
    def __init__(self, id_agendamento: int = None, data_agendamento: str = None, turno_agendamento: str = None, usuario: Usuario = None):
        self.__id_agendamento = id_agendamento
        self.__data_agendamento = data_agendamento
        self.__turno_agendamento = turno_agendamento
        self.__usuario = usuario

    @property
    def id_agendamento(self) -> int:
        return self.__id_agendamento

    @id_agendamento.setter
    def id_agendamento(self, id_agendamento: int):
        self.__id_agendamento = id_agendamento

    @property
    def data_agendamento(self) -> str:
        return self.__data_agendamento

    @data_agendamento.setter
    def data_agendamento(self, data_agendamento: str):
        self.__data_agendamento = data_agendamento

    @property
    def turno_agendamento(self) -> str:
        return self.__turno_agendamento

    @turno_agendamento.setter
    def turno_agendamento(self, turno_agendamento: str):
        self.__turno_agendamento = turno_agendamento

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario: Usuario):
        self.__usuario = usuario

    def perfilAgendamento(agendamento_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {agendamento_buscado.id_agendamento}\n"
        retornoPerfil += f"02. DATA: {Funcoes.formatarData(agendamento_buscado.data_agendamento)}\n"
        retornoPerfil += f"03. TURNO: {agendamento_buscado.turno_agendamento}\n"
        retornoPerfil += f"04. USUÁRIO: ID: {agendamento_buscado.usuario.id_usuario} | CPF: {agendamento_buscado.usuario.cpf_usuario} | NOME: {agendamento_buscado.usuario.nome_usuario}\n"
        retornoPerfil += "05. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarAgendamento(dsn, id_agendamento, listaReceptores, listaVoluntarios, listaAgendamentos):
        # INSTANCIANDO NOVO AGENDAMENTO
        novo_agendamento = Agendamento()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVO AGENDAMENTO
        id_agendamento = id_agendamento

        # SETANDO A DATA DO NOVO AGENDAMENTO
        try:
            data_agendamento = input(f"DIGITE A DATA DO AGENDAMENTO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            data_agendamento = Funcoes.validarPreenchimento(f"DIGITE A DATA DO AGENDAMENTO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", data_agendamento)
            data_formatada = datetime.strptime(data_agendamento, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%Y-%m-%d")

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA DATA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA DATA DO AGENDAMENTO:")
            print(str(e))
    
       # SETANDO O TURNO DO NOVO AGENDAMENTO
        try:
            turno_opcao = (f"SELECIONE O NOVO TURNO DO AGENDAMENTO: " + "\n" +
                            "01. MANHÃ" + "\n" +
                            "02. TARDE" + "\n" + 
                            Funcoes.menuRodape())
            
            opcao = int(input(turno_opcao))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, turno_opcao))

            if (opcao == 1):
                turno_agendamento = "MANHÃ"
            
            elif (opcao == 2):
                turno_agendamento = "TARDE"

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO TURNO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO TURNO DO AGENDAMENTO:")
            print(str(e))

        # SETANDO O USUÁRIO DO NOVO AGENDAMENTO
        try:
            tipo_usuario = (f"SELECIONE O TIPO DO NOVO USUÁRIO DO AGENDAMENTO: " + "\n" +
                            "01. RECEPTOR" + "\n" +
                            "02. VOLUNTÁRIO" + "\n" + 
                            Funcoes.menuRodape())
            
            opcao = int(input(tipo_usuario))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, tipo_usuario))

            if (opcao == 1):
                if (len(listaReceptores) == 0):
                    input("NENHUM RECEPTOR CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

                else:
                    Funcoes.exibirUsuariosAdmin(listaReceptores)
                    id_buscado = int(input("DIGITE O ID DO RECEPTOR QUE DESEJA INCLUIR AO AGENDAMENTO: \n"))
                    receptor_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaReceptores)
                    receptor_buscado = Funcoes.validarUsuarioBuscado(receptor_buscado, listaReceptores)
                    
                    usuario_agendamento = Usuario()
                    usuario_agendamento.id_usuario = receptor_buscado.id_usuario
                    usuario_agendamento.cpf_usuario = receptor_buscado.cpf_usuario
                    usuario_agendamento.nome_usuario = receptor_buscado.nome_usuario
                    usuario_agendamento.email_usuario = receptor_buscado.email_usuario
                    usuario_agendamento.cel_usuario = receptor_buscado.cel_usuario
                    usuario_agendamento.senha_usuario = receptor_buscado.senha_usuario
                    usuario_agendamento.status_usuario = receptor_buscado.status_usuario

            elif (opcao == 2):
                if (len(listaVoluntarios) == 0):
                    input("NENHUM VOLUNTÁRIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

                else:
                    Funcoes.exibirUsuariosAdmin(listaVoluntarios)
                    id_buscado = int(input("DIGITE O ID DO VOLUNTÁRIO QUE DESEJA INCLUIR AO AGENDAMENTO: \n"))
                    voluntario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaVoluntarios)
                    voluntario_buscado = Funcoes.validarUsuarioBuscado(voluntario_buscado, listaVoluntarios)
                    
                    usuario_agendamento = Usuario()
                    usuario_agendamento.id_usuario = voluntario_buscado.id_usuario
                    usuario_agendamento.cpf_usuario = voluntario_buscado.cpf_usuario
                    usuario_agendamento.nome_usuario = voluntario_buscado.nome_usuario
                    usuario_agendamento.email_usuario = voluntario_buscado.email_usuario
                    usuario_agendamento.cel_usuario = voluntario_buscado.cel_usuario
                    usuario_agendamento.senha_usuario = voluntario_buscado.senha_usuario
                    usuario_agendamento.status_usuario = voluntario_buscado.status_usuario
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO USUÁRIO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO USUÁRIO DO AGENDAMENTO:")
            print(str(e))
        
        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS
            cursor.execute("INSERT INTO agendamento (id_agendamento, data_agendamento, turno_agendamento, id_usuario) VALUES (:1, :2, :3, :4)", (id_agendamento, data_formatada_banco, turno_agendamento, usuario_agendamento.id_usuario))
            cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE
            novo_agendamento.id_agendamento = id_agendamento
            novo_agendamento.data_agendamento = data_formatada
            novo_agendamento.turno_agendamento = turno_agendamento
            novo_agendamento.usuario = usuario_agendamento
            listaAgendamentos.append(novo_agendamento)
            id_agendamento = id_agendamento + 1

            print("AGENDAMENTO CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO AGENDAMENTO:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

    def editarAgendamento(dsn, listaAgendamentos):
        perfilAgendamento = True

        if (len(listaAgendamentos) == 0):
            input("NENHUM AGENDAMENTO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirAgendamentosAdmin(listaAgendamentos)
            id_buscado = int(input("DIGITE O ID DO AGENDAMENTO QUE DESEJA EDITAR: \n"))
            agendamento_buscado = Funcoes.buscarAgendamentoPorId(id_buscado, listaAgendamentos)
            agendamento_buscado = Funcoes.validarAgendamentoBuscado(agendamento_buscado, listaAgendamentos)

            while (perfilAgendamento):
                opcao = int(input(Agendamento.perfilAgendamento(agendamento_buscado)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 5, Agendamento.perfilAgendamento(agendamento_buscado)))

                if (opcao == 1):
                    # EDITAR O ID DO AGENDAMENTO
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR A DATA DO AGENDAMENTO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DATA DO AGENDAMENTO DE ID {agendamento_buscado.id_agendamento}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DATA DO AGENDAMENTO DE ID {agendamento_buscado.id_agendamento}")))
                    
                    if (opcao == 1):
                       # EDITAR A DATA DO AGENDAMENTO - SIM
                       Agendamento.editarData(dsn, agendamento_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A DATA DO AGENDAMENTO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 3):
                    # EDITAR O TURNO DO AGENDAMENTO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O TURNO DO AGENDAMENTO DE ID {agendamento_buscado.id_agendamento}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O TURNO DO AGENDAMENTO DE ID {agendamento_buscado.id_agendamento}")))
                    
                    if (opcao == 1):
                       # EDITAR O TURNO DO AGENDAMENTO - SIM
                       Agendamento.editarTurno(dsn, agendamento_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O TURNO DO AGENDAMENTO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR O USUARIO DO AGENDAMENTO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O USUÁRIO DO AGENDAMENTO DE ID {agendamento_buscado.id_agendamento}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O USUÁRIO DO AGENDAMENTO DE ID {agendamento_buscado.id_agendamento}")))
                    
                    if (opcao == 1):
                       # EDITAR O USUARIO DO AGENDAMENTO - SIM
                       Agendamento.editarUsuario(dsn, agendamento_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O USUARIO DO AGENDAMENTO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    perfilAgendamento = False

    def editarData(dsn, agendamento_buscado):
        try:
            nova_data = input(f"DIGITE A NOVA DATA DO AGENDAMENTO DE ID {agendamento_buscado.id_agendamento} (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            nova_data = Funcoes.validarPreenchimento(f"DIGITE A NOVA DATA DO AGENDAMENTO DE ID {agendamento_buscado.id_agendamento} (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", nova_data)
            data_formatada = datetime.strptime(nova_data, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%Y-%m-%d")

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE agendamento SET data_agendamento = :data_formatada_banco WHERE id_agendamento = :id_agendamento", {"data_formatada_banco": data_formatada_banco, "id_agendamento": agendamento_buscado.id_agendamento})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                agendamento_buscado.data_agendamento = data_formatada

                print("DATA DO AGENDAMENTO EDITADA COM SUCESSO!")

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
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA DATA DO AGENDAMENTO:")
            print(str(e))
    
    def editarTurno(dsn, agendamento_buscado):
        try:
            novo_turno_opcao = (f"SELECIONE O NOVO TURNO DO AGENDAMENTO: " + "\n" +
                            "01. MANHÃ" + "\n" +
                            "02. TARDE" + "\n" + 
                            Funcoes.menuRodape())
            
            opcao = int(input(novo_turno_opcao))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, novo_turno_opcao))

            if (opcao == 1):
                novo_turno = "MANHÃ"
            
            elif (opcao == 2):
                novo_turno = "TARDE"

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE agendamento SET turno_agendamento = :novo_turno WHERE id_agendamento = :id_agendamento", {"novo_turno": novo_turno, "id_agendamento": agendamento_buscado.id_agendamento})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                agendamento_buscado.turno_agendamento = novo_turno

                print("TURNO DO AGENDAMENTO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO TURNO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO TURNO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO TURNO DO AGENDAMENTO:")
            print(str(e))

    def editarUsuario(dsn, agendamento_buscado, listaReceptores, listaVoluntarios):
        try:
            novo_tipo_usuario = (f"SELECIONE O TIPO DO NOVO USUÁRIO DO AGENDAMENTO: " + "\n" +
                            "01. RECEPTOR" + "\n" +
                            "02. VOLUNTÁRIO" + "\n" + 
                            Funcoes.menuRodape())
            
            opcao = int(input(novo_tipo_usuario))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, novo_tipo_usuario))

            if (opcao == 1):
                if (len(listaReceptores) == 0):
                    input("NENHUM RECEPTOR CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

                else:
                    Funcoes.exibirUsuariosAdmin(listaReceptores)
                    id_buscado = int(input("DIGITE O ID DO RECEPTOR QUE DESEJA EDITAR: \n"))
                    receptor_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaReceptores)
                    receptor_buscado = Funcoes.validarUsuarioBuscado(receptor_buscado, listaReceptores)
                    
                    novo_usuario = Usuario()
                    novo_usuario.id_usuario = receptor_buscado.id_usuario
                    novo_usuario.cpf_usuario = receptor_buscado.cpf_usuario
                    novo_usuario.nome_usuario = receptor_buscado.nome_usuario
                    novo_usuario.email_usuario = receptor_buscado.email_usuario
                    novo_usuario.cel_usuario = receptor_buscado.cel_usuario
                    novo_usuario.senha_usuario = receptor_buscado.senha_usuario
                    novo_usuario.status_usuario = receptor_buscado.status_usuario
                    
                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = Funcoes.connect(dsn)
                    cursor = conn.cursor()

                    try:           
                        # FAZENDO UPDATE NO BANCO DE DADOS
                        cursor.execute("UPDATE agendamento SET id_usuario = :novo_usuario.id_usuario WHERE id_agendamento = :id_agendamento", {"novo_usuario.id_usuario": novo_usuario.id_usuario, "id_agendamento": agendamento_buscado.id_agendamento})
                        cursor.connection.commit()

                        # FAZENDO UPDATE NO CONSOLE
                        agendamento_buscado.usuario = novo_usuario

                        print("USUÁRIO (RECEPTOR) DO AGENDAMENTO EDITADO COM SUCESSO!")

                    except sqlite3.DatabaseError as db_error:
                        print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO AGENDAMENTO:")
                        print(str(db_error))

                    finally:
                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

            elif (opcao == 2):
                if (len(listaVoluntarios) == 0):
                    input("NENHUM VOLUNTÁRIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

                else:
                    Funcoes.exibirUsuariosAdmin(listaVoluntarios)
                    id_buscado = int(input("DIGITE O ID DO VOLUNTÁRIO QUE DESEJA EDITAR: \n"))
                    voluntario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaVoluntarios)
                    voluntario_buscado = Funcoes.validarUsuarioBuscado(voluntario_buscado, listaVoluntarios)
                    
                    novo_usuario = Usuario()
                    novo_usuario.id_usuario = voluntario_buscado.id_usuario
                    novo_usuario.cpf_usuario = voluntario_buscado.cpf_usuario
                    novo_usuario.nome_usuario = voluntario_buscado.nome_usuario
                    novo_usuario.email_usuario = voluntario_buscado.email_usuario
                    novo_usuario.cel_usuario = voluntario_buscado.cel_usuario
                    novo_usuario.senha_usuario = voluntario_buscado.senha_usuario
                    novo_usuario.status_usuario = voluntario_buscado.status_usuario
                    
                    # CRIANDO CONEXÃO COM O BANCO DE DADOS
                    conn = Funcoes.connect(dsn)
                    cursor = conn.cursor()

                    try:           
                        # FAZENDO UPDATE NO BANCO DE DADOS
                        cursor.execute("UPDATE agendamento SET id_usuario = :novo_usuario.id_usuario WHERE id_agendamento = :id_agendamento", {"novo_usuario.id_usuario": novo_usuario.id_usuario, "id_agendamento": agendamento_buscado.id_agendamento})
                        cursor.connection.commit()

                        # FAZENDO UPDATE NO CONSOLE
                        agendamento_buscado.usuario = novo_usuario

                        print("USUÁRIO (VOLUNTÁRIO) DO AGENDAMENTO EDITADO COM SUCESSO!")

                    except sqlite3.DatabaseError as db_error:
                        print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO AGENDAMENTO:")
                        print(str(db_error))

                    finally:
                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor) 
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO AGENDAMENTO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO USUÁRIO DO AGENDAMENTO:")
            print(str(e))

    def excluirAgendamento(dsn, listaAgendamentos):
        
        if len(listaAgendamentos) == 0:
            print("NÃO EXISTEM AGENDAMENTOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirAgendamentosAdmin(listaAgendamentos)
            try:
                id_buscado = int(input("DIGITE O ID DO AGENDAMENTO QUE DESEJA EXCLUIR: \n"))
                agendamento_buscado = Funcoes.buscarAgendamentoPorId(id_buscado, listaAgendamentos)
                agendamento_buscado = Funcoes.validarAgendamentoBuscado(agendamento_buscado, listaAgendamentos)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O AGENDAMENTO")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O AGENDAMENTO"))

                if opcao == 1:
                    for i in range(len(listaAgendamentos)):
                        if listaAgendamentos[i].id_agendamento == id_buscado:
                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try: 
                                # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                                cursor.execute("DELETE FROM agendamento WHERE id_agendamento = :1", (listaAgendamentos[i].id_agendamento,))
                                cursor.connection.commit()

                                del listaAgendamentos[i]

                                print("AGENDAMENTO EXCLUÍDO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A EXCLUSÃO DO AGENDAMENTO:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO AGENDAMENTO A SER EXCLUÍDO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO AGENDAMENTO:")
                print(str(e))
