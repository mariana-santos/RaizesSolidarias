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

    def perfilReceptor(receptor_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {receptor_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {receptor_buscado.cpf_usuario}\n"
        retornoPerfil += f"03. NOME: {receptor_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {receptor_buscado.email_usuario}\n"
        retornoPerfil += f"05. CELULAR: {receptor_buscado.cel_usuario}\n"
        retornoPerfil += f"06. SENHA: {receptor_buscado.senha_usuario}\n"
        retornoPerfil += f"07. STATUS: {receptor_buscado.status_usuario}\n"
        retornoPerfil += f"08. CARGA MÁXIMA TRANSPORTADA: {receptor_buscado.carga_receptor}\n"
        retornoPerfil += f"09. ENDEREÇO: {receptor_buscado.endereco_receptor}\n"
        retornoPerfil += "10. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarReceptor(dsn, id_usuario, listaUsuarios, listaReceptores):
        Receptor.cadastrarUsuario(dsn, id_usuario, listaUsuarios)
        receptor_buscado = Funcoes.buscarUsuarioPorId(id_usuario, listaReceptores)

        # INSTANCIANDO NOVO RECEPTOR - OK
        novo_receptor = Receptor()

        # SETANDO OS ATRIBUTOS DO NOVO RECEPTOR PARA O NOVO RECEPTOR - OK
        id_usuario = receptor_buscado.id_usuario
        cpf_usuario = receptor_buscado.cpf_usuario
        nome_usuario = receptor_buscado.nome_usuario
        email_usuario = receptor_buscado.email_usuario
        cel_usuario = receptor_buscado.cel_usuario
        senha_usuario = receptor_buscado.senha_usuario
        status_usuario = receptor_buscado.status_usuario

        # SETANDO A CARGA DO NOVO RECEPTOR - OK
        try:
            carga_receptor = int(input(f"DIGITE A CAPACIDADE MÁXIMA DA CARGA DO NOVO RECEPTOR (EM KGS, NÚMERO INTEIRO): "))
            carga_receptor = int(Funcoes.validarPreenchimento(f"DIGITE A CAPACIDADE MÁXIMA DA CARGA DO NOVO RECEPTOR (EM KGS, NÚMERO INTEIRO): ", carga_receptor))

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA CARGA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA CARGA DO RECEPTOR:")
            print(str(e))
        
        # SETANDO O ENDEREÇO DO NOVO RECEPTOR - OK
        try:
            endereco_receptor = input(f"DIGITE O ENDEREÇO DO NOVO RECEPTOR: ")
            endereco_receptor = Funcoes.validarPreenchimento(f"DIGITE O ENDEREÇO DO NOVO RECEPTOR: ", endereco_receptor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ENDEREÇO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO ENDEREÇO DO RECEPTOR:")
            print(str(e))
    
        # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS - OK
            cursor.execute("INSERT INTO receptor (id_usuario, carga_receptor, endereco_receptor) VALUES (:1, :2, :3)", (id_usuario, carga_receptor, endereco_receptor))
            cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE - OK
            novo_receptor.id_usuario = id_usuario
            novo_receptor.cpf_usuario = cpf_usuario
            novo_receptor.nome_usuario = nome_usuario
            novo_receptor.email_usuario = email_usuario
            novo_receptor.cel_usuario = cel_usuario
            novo_receptor.senha_usuario = senha_usuario
            novo_receptor.status_usuario = status_usuario
            novo_receptor.carga_receptor = carga_receptor
            novo_receptor.endereco_receptor = endereco_receptor
            listaReceptores.append(novo_receptor)
            id_usuario = id_usuario + 1

            print("RECEPTOR CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO RECEPTOR:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
            Funcoes.disconnect(conn, cursor)

    def editarReceptor(dsn, listaReceptores):
        perfilReceptor = True

        if (len(listaReceptores) == 0):
            input("NENHUM RECEPTOR CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirUsuariosAdmin(listaReceptores)
            id_buscado = int(input("DIGITE O ID DO RECEPTOR QUE DESEJA EDITAR: \n"))
            receptor_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaReceptores)
            receptor_buscado = Funcoes.validarUsuarioBuscado(receptor_buscado, listaReceptores)

            while (perfilReceptor):
                opcao = int(input(Receptor.perfilReceptor(receptor_buscado)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 9, Receptor.perfilReceptor(receptor_buscado)))

                if (opcao == 1):
                    # EDITAR O ID DO RECEPTOR - OK
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR O CPF DO RECEPTOR - OK
                    input(Funcoes.editarNegativo())

                elif (opcao == 3):
                    # EDITAR O NOME DO RECEPTOR - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O NOME DO RECEPTOR - SIM - OK
                       Receptor.editarNome(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O NOME DO RECEPTOR - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR O EMAIL DO RECEPTOR - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O EMAIL DO RECEPTOR - SIM - OK
                       Receptor.editarEmail(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O EMAIL DO RECEPTOR - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    # EDITAR O CELULAR DO RECEPTOR - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CELULAR DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CELULAR DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O CELULAR DO RECEPTOR - SIM - OK
                       Receptor.editarCel(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O CELULAR DO RECEPTOR - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 6):
                    # EDITAR A SENHA DO RECEPTOR - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A SENHA DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A SENHA DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR A SENHA DO RECEPTOR - SIM - OK
                       Receptor.editarSenha(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A SENHA DO RECEPTOR - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 7):
                    # EDITAR O STATUS DO RECEPTOR - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O STATUS DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O STATUS DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O STATUS DO RECEPTOR - SIM - OK
                       Receptor.editarStatus(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O STATUS DO RECEPTOR - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 8):
                    # EDITAR O ENDEREÇO DO RECEPTOR - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O ENDEREÇO DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O ENDEREÇO DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O ENDEREÇO DO RECEPTOR - SIM - OK
                       Receptor.editarEndereco(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O ENDEREÇO DO RECEPTOR - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 9):
                    # EDITAR A CARGA DO RECEPTOR - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A CARGA DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A CARGA DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR A CARGA DO RECEPTOR - SIM - OK
                       Receptor.editarCarga(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A CARGA DO RECEPTOR - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 10):
                    perfilReceptor = False

    def editarCarga(dsn, receptor_buscado):
        try:
            nova_carga = int(input(f"DIGITE A NOVA CARGA SUPORTADA DO RECEPTOR {receptor_buscado.nome_usuario}: "))
            nova_carga = int(Funcoes.validarPreenchimento(f"DIGITE A NOVA CARGA SUPORTADA DO RECEPTOR {receptor_buscado.nome_usuario}: ", nova_carga))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE receptor SET carga_receptor = :nova_carga WHERE id_usuario = :id_usuario", {"nova_carga": nova_carga, "id_usuario": receptor_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                receptor_buscado.carga_receptor = nova_carga

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

    def editarEndereco(dsn, receptor_buscado):
        try:
            novo_endereco = input(f"DIGITE O NOVO ENDEREÇO DO RECEPTOR {receptor_buscado.nome_usuario}: ")
            novo_endereco = Funcoes.validarPreenchimento(f"DIGITE O NOVO ENDEREÇO DO RECEPTOR {receptor_buscado.nome_usuario}: ", novo_endereco)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                cursor.execute("UPDATE receptor SET endereco_receptor = :novo_endereco WHERE id_usuario = :id_usuario", {"novo_endereco": novo_endereco, "id_usuario": receptor_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE - OK
                receptor_buscado.endereco_receptor = novo_endereco

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

    def excluirReceptor(dsn, listaReceptores):
        
        if len(listaReceptores) == 0:
            print("NÃO EXISTEM RECEPTORES CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirUsuariosAdmin(listaReceptores)
            try:
                id_buscado = int(input("DIGITE O ID DO RECEPTOR QUE DESEJA EXCLUIR: \n"))
                receptor_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaReceptores)
                receptor_buscado = Funcoes.validarUsuarioBuscado(receptor_buscado, listaReceptores)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O RECEPTOR")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O RECEPTOR"))

                if opcao == 1:
                    for i in range(len(listaReceptores)):
                        if listaReceptores[i].id_usuario == id_buscado:
                            novo_status_usuario = "INATIVO"

                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try:
                                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                                cursor.execute("UPDATE usuario SET status_usuario = :novo_status_usuario WHERE id_usuario = :id_usuario", {"novo_status_usuario": novo_status_usuario, "id_usuario": receptor_buscado.id_usuario})
                                cursor.connection.commit()

                                # FAZENDO UPDATE NO CONSOLE - OK
                                receptor_buscado.status_usuario = novo_status_usuario

                                print("STATUS DO RECEPTOR ALTERADO PARA INATIVO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A ALTERAÇÃO DO STATUS DO RECEPTOR:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO RECEPTOR A SER EXCLUÍDO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO RECEPTOR:")
                print(str(e))