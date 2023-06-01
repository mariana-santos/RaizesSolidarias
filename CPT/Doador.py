import sqlite3

from Funcoes import Funcoes
from Usuario import Usuario

class Doador(Usuario):
    def __init__(self, id_usuario: int = None, cpf_usuario: str = None, nome_usuario: str = None, email_usuario: str = None, cel_usuario: str = None, senha_usuario: str = None, status_usuario: str = None, nivel_doador: int = None, moedas_doador: int = None):
        super()._init_(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
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

    def perfilDoador(doador_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {doador_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {doador_buscado.cpf_usuario}\n"
        retornoPerfil += f"03. NOME: {doador_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {doador_buscado.email_usuario}\n"
        retornoPerfil += f"05. CELULAR: {doador_buscado.cel_usuario}\n"
        retornoPerfil += f"06. SENHA: {doador_buscado.senha_usuario}\n"
        retornoPerfil += f"07. STATUS: {doador_buscado.status_usuario}\n"
        retornoPerfil += f"08. NÍVEL: {doador_buscado.nivel_doador}\n"
        retornoPerfil += f"09. MOEDAS: {doador_buscado.moedas_doador}\n"
        retornoPerfil += "10. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarDoador(dsn, id_usuario, listaUsuarios, listaDoadores):
        Doador.cadastrarUsuario(dsn, id_usuario, listaUsuarios)
        doador_buscado = Funcoes.buscarUsuarioPorId(id_usuario, listaDoadores)

        # INSTANCIANDO NOVO DOADOR
        novo_doador = Doador()

        # SETANDO OS ATRIBUTOS DO NOVO DOADOR PARA O NOVO DOADOR
        id_usuario = doador_buscado.id_usuario
        cpf_usuario = doador_buscado.cpf_usuario
        nome_usuario = doador_buscado.nome_usuario
        email_usuario = doador_buscado.email_usuario
        cel_usuario = doador_buscado.cel_usuario
        senha_usuario = doador_buscado.senha_usuario
        status_usuario = doador_buscado.status_usuario

        # SETANDO O NÍVEL DO NOVO DOADOR
        nivel_doador = 0
        
        # SETANDO A QUANTIDADE DE MOEDAS DO NOVO DOADOR
        qtd_moedas_doador = 0
    
        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS
            cursor.execute("INSERT INTO doador (id_usuario, nivel_doador, qtd_moedas_doador) VALUES (:1, :2, :3)", (id_usuario, nivel_doador, qtd_moedas_doador))
            cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE
            novo_doador.id_usuario = id_usuario
            novo_doador.cpf_usuario = cpf_usuario
            novo_doador.nome_usuario = nome_usuario
            novo_doador.email_usuario = email_usuario
            novo_doador.cel_usuario = cel_usuario
            novo_doador.senha_usuario = senha_usuario
            novo_doador.status_usuario = status_usuario
            novo_doador.nivel_doador = nivel_doador
            novo_doador.qtd_moedas_doador = qtd_moedas_doador
            listaDoadores.append(novo_doador)
            id_usuario = id_usuario + 1

            print("DOADOR CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO DOADOR:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

    def editarDoador(dsn, listaDoadores):
        perfilDoador = True

        if (len(listaDoadores) == 0):
            input("NENHUM DOADOR CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirUsuariosAdmin(listaDoadores)
            id_buscado = int(input("DIGITE O ID DO DOADOR QUE DESEJA EDITAR: \n"))
            doador_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaDoadores)
            doador_buscado = Funcoes.validarUsuarioBuscado(doador_buscado, listaDoadores)

            while (perfilDoador):
                opcao = int(input(Doador.perfilDoador(doador_buscado)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 9, Doador.perfilDoador(doador_buscado)))

                if (opcao == 1):
                    # EDITAR O ID DO DOADOR
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR O CPF DO DOADOR
                    input(Funcoes.editarNegativo())

                elif (opcao == 3):
                    # EDITAR O NOME DO DOADOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O NOME DO DOADOR - SIM
                       Doador.editarNome(dsn, doador_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O NOME DO DOADOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR O EMAIL DO DOADOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O EMAIL DO DOADOR - SIM
                       Doador.editarEmail(dsn, doador_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O EMAIL DO DOADOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    # EDITAR O CELULAR DO DOADOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CELULAR DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CELULAR DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O CELULAR DO DOADOR - SIM
                       Doador.editarCel(dsn, doador_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O CELULAR DO DOADOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 6):
                    # EDITAR A SENHA DO DOADOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A SENHA DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A SENHA DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR A SENHA DO DOADOR - SIM
                       Doador.editarSenha(dsn, doador_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A SENHA DO DOADOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 7):
                    # EDITAR O STATUS DO DOADOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O STATUS DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O STATUS DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O STATUS DO DOADOR - SIM
                       Doador.editarStatus(dsn, doador_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O STATUS DO DOADOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 8):
                    # EDITAR O NÍVEL DO DOADOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NÍVEL DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NÍVEL DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O NÍVEL DO DOADOR - SIM
                       Doador.editarNivel(dsn, doador_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O NÍVEL DO DOADOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 9):
                    # EDITAR A QUANTIDADE DE MOEDAS DO DOADOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A QUANTIDADE DE MOEDAS DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A QUANTIDADE DE MOEDAS DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR A QUANTIDADE DE MOEDAS DO DOADOR - SIM
                       Doador.editarMoedas(dsn, doador_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A QUANTIDADE DE MOEDAS DO DOADOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 9):
                    perfilDoador = False

    def editarNivel(dsn, usuario_buscado):
        try:
            novo_nivel = int(input(f"DIGITE O NOVO NÍVEL DO DOADOR {usuario_buscado.nome_usuario}: "))
            novo_nivel = int(Funcoes.validarPreenchimento(f"DIGITE O NOVO NÍVEL DO DOADOR {usuario_buscado.nome_usuario}: ", novo_nivel))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE doador SET nivel_doador = :novo_nivel WHERE id_usuario = :id_usuario", {"novo_nivel": novo_nivel, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                usuario_buscado.nivel_doador = novo_nivel

                print("NÍVEL DO DOADOR EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO NÍVEL:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
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

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE doador SET moedas_doador = :novas_moedas WHERE id_usuario = :id_usuario", {"novas_moedas": novas_moedas, "id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                usuario_buscado.moedas_doador = novas_moedas

                print("MOEDAS DO DOADOR EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DAS MOEDAS:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DAS NOVAS MOEDAS:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DAS MOEDAS DO DOADOR:")
            print(str(e))

    def excluirDoador(dsn, listaDoadores):
        
        if len(listaDoadores) == 0:
            print("NÃO EXISTEM DOADORES CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirUsuariosAdmin(listaDoadores)
            try:
                id_buscado = int(input("DIGITE O ID DO DOADOR QUE DESEJA EXCLUIR: \n"))
                doador_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaDoadores)
                doador_buscado = Funcoes.validarUsuarioBuscado(doador_buscado, listaDoadores)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O DOADOR")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O DOADOR"))

                if opcao == 1:
                    for i in range(len(listaDoadores)):
                        if listaDoadores[i].id_usuario == id_buscado:
                            novo_status_usuario = "INATIVO"

                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try:
                                # FAZENDO UPDATE NO BANCO DE DADOS
                                cursor.execute("UPDATE usuario SET status_usuario = :novo_status_usuario WHERE id_usuario = :id_usuario", {"novo_status_usuario": novo_status_usuario, "id_usuario": doador_buscado.id_usuario})
                                cursor.connection.commit()

                                # FAZENDO UPDATE NO CONSOLE
                                doador_buscado.status_usuario = novo_status_usuario

                                print("STATUS DO DOADOR ALTERADO PARA INATIVO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A ALTERAÇÃO DO STATUS DO DOADOR:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO DOADOR A SER EXCLUÍDO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO DOADOR:")
                print(str(e))