import sqlite3

from Funcoes import Funcoes

class Usuario:
    def __init__(self, id_usuario: int = None, cpf_usuario: str = None, nome_usuario: str = None, email_usuario: str = None, cel_usuario: str = None, senha_usuario: str = None, status_usuario: str = None):
        self._id_usuario = id_usuario
        self._cpf_usuario = cpf_usuario
        self._nome_usuario = nome_usuario
        self._email_usuario = email_usuario
        self._cel_usuario = cel_usuario
        self._senha_usuario = senha_usuario
        self._status_usuario = status_usuario

    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario: int):
        self._id_usuario = id_usuario

    @property
    def cpf_usuario(self) -> str:
        return self._cpf_usuario

    @cpf_usuario.setter
    def cpf_usuario(self, cpf_usuario: str):
        self._cpf_usuario = cpf_usuario

    @property
    def nome_usuario(self) -> str:
        return self._nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, nome_usuario: str):
        self._nome_usuario = nome_usuario

    @property
    def email_usuario(self) -> str:
        return self._email_usuario

    @email_usuario.setter
    def email_usuario(self, email_usuario: str):
        self._email_usuario = email_usuario

    @property
    def cel_usuario(self) -> str:
        return self._cel_usuario

    @cel_usuario.setter
    def cel_usuario(self, cel_usuario: str):
        self._cel_usuario = cel_usuario

    @property
    def senha_usuario(self) -> str:
        return self._senha_usuario

    @senha_usuario.setter
    def senha_usuario(self, senha_usuario: str):
        self._senha_usuario = senha_usuario

    @property
    def status_usuario(self) -> str:
        return self._status_usuario

    @status_usuario.setter
    def status_usuario(self, status_usuario: str):
        self._status_usuario = status_usuario

    def perfilUsuario(usuario_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {usuario_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {usuario_buscado.cpf_usuario}\n"
        retornoPerfil += f"03. NOME: {usuario_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {usuario_buscado.email_usuario}\n"
        retornoPerfil += f"05. CELULAR: {usuario_buscado.cel_usuario}\n"
        retornoPerfil += f"06. SENHA: {usuario_buscado.senha_usuario}\n"
        retornoPerfil += f"07. STATUS: {usuario_buscado.status_usuario}\n"
        retornoPerfil += "08. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarUsuario(dsn, id_usuario, listaUsuarios):
        # INSTANCIANDO NOVO USUARIO
        novo_usuario = Usuario()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVO USUARIO
        id_usuario = id_usuario

        # SETANDO O CPF DO NOVO USUARIO
        try:
            cpf_usuario = input(f"DIGITE O CPF DO USUÁRIO (SEM PONTOS OU TRAÇOS, EXEMPLO: 74253599010): ")
            cpf_usuario = Funcoes.validarPreenchimento(f"DIGITE O CPF DO USUÁRIO (SEM PONTOS OU TRAÇOS, EXEMPLO: 74253599010): ", cpf_usuario)
            cpf_usuario = Funcoes.verificarCPF(cpf_usuario)
            cpf_usuario = Funcoes.formatarCpf(cpf_usuario)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO CPF:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO CPF DO USUÁRIO:")
            print(str(e))
    
       # SETANDO O NOME DO NOVO USUÁRIO
        try:
            nome_usuario = input(f"DIGITE O NOME DO NOVO USUÁRIO: ")
            nome_usuario = Funcoes.validarPreenchimento(f"DIGITE O NOME DO NOVO USUÁRIO: ", nome_usuario)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOME:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO NOME DO USUÁRIO:")
            print(str(e))
    
        # SETANDO O EMAIL DO NOVO USUÁRIO
        try:
            email_usuario = input(f"DIGITE O EMAIL DO NOVO USUÁRIO: ")
            email_usuario = Funcoes.validarPreenchimento(f"DIGITE O EMAIL DO NOVO USUÁRIO: ", email_usuario)
            email_usuario = Funcoes.verificarEmail(email_usuario)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO EMAIL:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO EMAIL DO USUÁRIO:")
            print(str(e))
        
        # SETANDO O CELULAR DO NOVO USUÁRIO
        try:
            cel_usuario = input(f"DIGITE O CELULAR DO USUÁRIO (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
            cel_usuario = Funcoes.validarPreenchimento(f"DIGITE O CELULAR DO USUÁRIO (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ", cel_usuario)
            cel_usuario = Funcoes.validarCel(cel_usuario)
            cel_usuario = Funcoes.verificarCel(cel_usuario)
            cel_usuario = Funcoes.formatarCel(cel_usuario)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO CELULAR:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO CELULAR DO USUÁRIO:")
            print(str(e))

        # SETANDO A SENHA DO NOVO USUÁRIO
        try:
            senha_usuario = input("DIGITE A SENHA DO USUÁRIO: ")
            senha_usuario = Funcoes.validarPreenchimento("DIGITE A SENHA DO USUÁRIO: ", senha_usuario)
            conf_senha = input("CONFIRME A SENHA DO USUÁRIO: ")
            conf_senha = Funcoes.validarPreenchimento("CONFIRME A SENHA DO USUÁRIO: ", conf_senha)
            senha_usuario = Funcoes.validarSenha(senha_usuario, conf_senha)
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA SENHA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA SENHA DO USUÁRIO:")
            print(str(e))

        # SETANDO O STATUS DO NOVO USUÁRIO
        status_usuario = "ATIVO"

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS
            cursor.execute("INSERT INTO usuario (id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario) VALUES (:1, :2, :3, :4, :5, :6, :7)", (id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario))
            cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE
            novo_usuario.id_usuario = id_usuario
            novo_usuario.cpf_usuario = cpf_usuario
            novo_usuario.nome_usuario = nome_usuario
            novo_usuario.email_usuario = email_usuario
            novo_usuario.cel_usuario = cel_usuario
            novo_usuario.senha_usuario = senha_usuario
            novo_usuario.status_usuario = status_usuario
            listaUsuarios.append(novo_usuario)
            id_usuario = id_usuario + 1

            print("USUARIO CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO USUARIO:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

    def editarUsuario(dsn, listaUsuarios):
        perfilUsuario = True

        if (len(listaUsuarios) == 0):
            input("NENHUM USUARIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirUsuariosAdmin(listaUsuarios)
            id_buscado = int(input("DIGITE O ID DO USUARIO QUE DESEJA EDITAR: \n"))
            usuario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaUsuarios)
            usuario_buscado = Funcoes.validarUsuarioBuscado(usuario_buscado, listaUsuarios)

            while (perfilUsuario):
                opcao = int(input(Usuario.perfilUsuario(usuario_buscado)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 8, Usuario.perfilUsuario(usuario_buscado)))

                if (opcao == 1):
                    # EDITAR O ID DO USUARIO
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR O CPF DO USUARIO
                    input(Funcoes.editarNegativo())

                elif (opcao == 3):
                    # EDITAR O NOME DO USUARIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO USUARIO DE ID {usuario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO USUARIO DE ID {usuario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O NOME DO USUARIO - SIM
                       Usuario.editarNome(dsn, usuario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O NOME DO USUARIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR O EMAIL DO USUARIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO USUARIO DE ID {usuario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO USUARIO DE ID {usuario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O EMAIL DO USUARIO - SIM
                       Usuario.editarEmail(dsn, usuario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O EMAIL DO USUARIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    # EDITAR O CELULAR DO USUARIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CELULAR DO USUARIO DE ID {usuario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CELULAR DO USUARIO DE ID {usuario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O CELULAR DO USUARIO - SIM
                       Usuario.editarCel(dsn, usuario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O CELULAR DO USUARIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 6):
                    # EDITAR A SENHA DO USUARIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A SENHA DO USUARIO DE ID {usuario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A SENHA DO USUARIO DE ID {usuario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR A SENHA DO USUARIO - SIM
                       Usuario.editarSenha(dsn, usuario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A SENHA DO USUARIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 7):
                    # EDITAR O STATUS DO USUARIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O STATUS DO USUARIO DE ID {usuario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O STATUS DO USUARIO DE ID {usuario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O STATUS DO USUARIO - SIM
                       Usuario.editarStatus(dsn, usuario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O STATUS DO USUARIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 8):
                    perfilUsuario = False

    def editarNome(dsn, usuario_buscado):
        try:
            novo_nome = input(f"DIGITE O NOVO NOME DO USUÁRIO {usuario_buscado.nome_usuario}: ")
            novo_nome = Funcoes.validarPreenchimento(f"DIGITE O NOVO NOME DO USUÁRIO {usuario_buscado.nome_usuario}: ", novo_nome)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE usuario SET nome_usuario = :novo_nome WHERE id_usuario = :id_usuario", {"novo_nome": novo_nome, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                usuario_buscado.nome_usuario = novo_nome

                print("NOME DO USUÁRIO EDITADO COM SUCESSO!")

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
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO NOME DO USUÁRIO:")
            print(str(e))

    def editarEmail(dsn, usuario_buscado, emails_cadastrados):
        try:
            novo_email = input(f"DIGITE O NOVO EMAIL DO USUÁRIO {usuario_buscado.nome_usuario}: ")
            novo_email = Funcoes.validarPreenchimento(f"DIGITE O NOVO EMAIL DO USUÁRIO {usuario_buscado.nome_usuario}: ", novo_email)
            novo_email = Funcoes.verificarEmail(novo_email, emails_cadastrados)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()
            
            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE usuario SET email_usuario = :novo_email WHERE id_usuario = :id_usuario", {"novo_email": novo_email, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # ATUALIZANDO LISTA DE EMAILS CADASTRADOS
                emails_cadastrados.remove(usuario_buscado.email_usuario)
                emails_cadastrados.add(novo_email) 

                # FAZENDO UPDATE NO CONSOLE
                usuario_buscado.email_usuario = novo_email

                print("EMAIL DO USUÁRIO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO EMAIL:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO EMAIL:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO EMAIL DO USUÁRIO:")
            print(str(e))

    def editarCel(dsn, usuario_buscado, cel_cadastrados):
        try:
            novo_cel = input(f"DIGITE O NOVO CELULAR DO USUÁRIO {usuario_buscado.nome_usuario} (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
            novo_cel = Funcoes.validarPreenchimento(f"DIGITE O NOVO CELULAR DO USUÁRIO {usuario_buscado.nome_usuario} (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ", novo_cel)
            novo_cel = Funcoes.validarCel(novo_cel)
            novo_cel = Funcoes.verificarCel(novo_cel, cel_cadastrados)
            novo_cel = Funcoes.formatarCel(novo_cel)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()
            
            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE usuario SET cel_usuario = :novo_cel WHERE id_usuario = :id_usuario", {"novo_cel": novo_cel, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # ATUALIZANDO LISTA DE CELS CADASTRADOS
                cel_cadastrados.remove(usuario_buscado.cel_usuario)
                cel_cadastrados.add(novo_cel) 

                # FAZENDO UPDATE NO CONSOLE
                usuario_buscado.cel_usuario = novo_cel

                print("CELULAR DO USUÁRIO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO CELULAR:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO CELULAR:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO CELULAR DO USUÁRIO:")
            print(str(e))

    def editarSenha(dsn, usuario_buscado):
        try:
            nova_senha_usuario = input(f"DIGITE A NOVA SENHA DO USUÁRIO {usuario_buscado.nome_usuario}: ")
            conf_senha = input(f"CONFIRME A NOVA SENHA DO USUÁRIO {usuario_buscado.nome_usuario}: ")
            nova_senha_usuario = Funcoes.validarSenha(nova_senha_usuario, conf_senha)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE usuario SET senha_usuario = :nova_senha_usuario WHERE id_usuario = :id_usuario", {"nova_senha_usuario": nova_senha_usuario, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                usuario_buscado.senha_usuario = nova_senha_usuario

                print("SENHA DO USUÁRIO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA SENHA:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA SENHA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA SENHA DO USUÁRIO:")
            print(str(e))

    def editarStatus(dsn, usuario_buscado):
        try:
            novo_status = (f"SELECIONE O NOVO STATUS DO USUÁRIO {usuario_buscado.nome_usuario}: " + "\n" +
                            "01. ATIVO" + "\n" +
                            "02. INATIVO" + "\n" + 
                            Funcoes.menuRodape())
            
            opcao = int(input(novo_status))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, novo_status))

            if (opcao == 1):
                novo_status_usuario = "ATIVO"

            elif (opcao == 2):
                novo_status_usuario = "INATIVO"

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:           
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE usuario SET status_usuario = :novo_status_usuario WHERE id_usuario = :id_usuario", {"novo_status_usuario": novo_status_usuario, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                usuario_buscado.status_usuario = novo_status_usuario

                print("STATUS DO USUÁRIO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO STATUS:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO STATUS:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO STATUS DO USUÁRIO:")
            print(str(e))

    def excluirUsuario(dsn, listaUsuarios):
        
        if len(listaUsuarios) == 0:
            print("NÃO EXISTEM USUARIOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirUsuariosAdmin(listaUsuarios)
            try:
                id_buscado = int(input("DIGITE O ID DO USUARIO QUE DESEJA EXCLUIR: \n"))
                usuario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaUsuarios)
                usuario_buscado = Funcoes.validarUsuarioBuscado(usuario_buscado, listaUsuarios)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O USUARIO")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O USUARIO"))

                if opcao == 1:
                    for i in range(len(listaUsuarios)):
                        if listaUsuarios[i].id_usuario == id_buscado:
                            novo_status_usuario = "INATIVO"

                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try:
                                # FAZENDO UPDATE NO BANCO DE DADOS
                                cursor.execute("UPDATE usuario SET status_usuario = :novo_status_usuario WHERE id_usuario = :id_usuario", {"novo_status_usuario": novo_status_usuario, "id_usuario": usuario_buscado.id_usuario})
                                cursor.connection.commit()

                                # FAZENDO UPDATE NO CONSOLE
                                usuario_buscado.status_usuario = novo_status_usuario

                                print("STATUS DO USUARIO ALTERADO PARA INATIVO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A ALTERAÇÃO DO STATUS DO USUARIO:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO USUARIO A SER EXCLUÍDO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO USUARIO:")
                print(str(e))
