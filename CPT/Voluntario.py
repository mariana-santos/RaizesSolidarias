import sqlite3

from datetime import datetime

from Funcoes import Funcoes
from Usuario import Usuario

class Voluntario(Usuario):
    def __init__(self, id_usuario: int = None, cpf_usuario: str = None, nome_usuario: str = None, email_usuario: str = None, cel_usuario: str = None, senha_usuario: str = None, status_usuario: str = None, data_registro_voluntario: str = None):
        super().__init__(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
        self._data_registro_voluntario = data_registro_voluntario

    @property
    def data_registro_voluntario(self) -> str:
        return self._data_registro_voluntario

    @data_registro_voluntario.setter
    def data_registro_voluntario(self, data_registro_voluntario: str):
        self._data_registro_voluntario = data_registro_voluntario

    def perfilVoluntario(voluntario_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {voluntario_buscado.id_usuario}\n"
        retornoPerfil += f"02. CPF: {voluntario_buscado.cpf_usuario}\n"
        retornoPerfil += f"03. NOME: {voluntario_buscado.nome_usuario}\n"
        retornoPerfil += f"04. EMAIL: {voluntario_buscado.email_usuario}\n"
        retornoPerfil += f"05. CELULAR: {voluntario_buscado.cel_usuario}\n"
        retornoPerfil += f"06. SENHA: {voluntario_buscado.senha_usuario}\n"
        retornoPerfil += f"07. STATUS: {voluntario_buscado.status_usuario}\n"
        retornoPerfil += f"08. DATA DE REGISTRO: {voluntario_buscado.data_registro_voluntario}\n"
        retornoPerfil += "09. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarVoluntario(dsn, id_usuario, listaUsuarios, listaVoluntarios):
        Voluntario.cadastrarUsuario(dsn, id_usuario, listaUsuarios)
        voluntario_buscado = Funcoes.buscarUsuarioPorId(id_usuario, listaVoluntarios)

        # INSTANCIANDO NOVO VOLUNTARIO - OK
        novo_voluntario = Voluntario()

        # SETANDO OS ATRIBUTOS DO NOVO VOLUNTARIO PARA O NOVO VOLUNTARIO - OK
        id_usuario = voluntario_buscado.id_usuario
        cpf_usuario = voluntario_buscado.cpf_usuario
        nome_usuario = voluntario_buscado.nome_usuario
        email_usuario = voluntario_buscado.email_usuario
        cel_usuario = voluntario_buscado.cel_usuario
        senha_usuario = voluntario_buscado.senha_usuario
        status_usuario = voluntario_buscado.status_usuario

        # SETANDO A DATA DE REGISTRO DO NOVO VOLUNTARIO - OK
        data_registro_voluntario = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%d/%m/%Y')

        # CRIANDO CONEXÃO COM O BANCO DE DADOS - OK
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS - OK
            cursor.execute("INSERT INTO voluntario (id_usuario, data_registro_voluntario) VALUES (:1, :2)", (id_usuario, data_registro_voluntario))
            cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE - OK
            novo_voluntario.id_usuario = id_usuario
            novo_voluntario.cpf_usuario = cpf_usuario
            novo_voluntario.nome_usuario = nome_usuario
            novo_voluntario.email_usuario = email_usuario
            novo_voluntario.cel_usuario = cel_usuario
            novo_voluntario.senha_usuario = senha_usuario
            novo_voluntario.status_usuario = status_usuario
            novo_voluntario.data_registro_voluntario = data_registro_voluntario
            listaVoluntarios.append(novo_voluntario)
            id_usuario = id_usuario + 1

            print("VOLUNTARIO CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO VOLUNTARIO:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
            Funcoes.disconnect(conn, cursor)

    def editarVoluntario(dsn, listaVoluntarios):
        perfilVoluntario = True

        if (len(listaVoluntarios) == 0):
            input("NENHUM VOLUNTARIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirUsuariosAdmin(listaVoluntarios)
            id_buscado = int(input("DIGITE O ID DO VOLUNTARIO QUE DESEJA EDITAR: \n"))
            voluntario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaVoluntarios)
            voluntario_buscado = Funcoes.validarReceptorBuscado(voluntario_buscado, listaVoluntarios)

            while (perfilVoluntario):
                opcao = int(input(Voluntario.perfilVoluntario(voluntario_buscado)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 9, Voluntario.perfilVoluntario(voluntario_buscado)))

                if (opcao == 1):
                    # EDITAR O ID DO VOLUNTARIO - OK
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR O CPF DO VOLUNTARIO - OK
                    input(Funcoes.editarNegativo())

                elif (opcao == 3):
                    # EDITAR O NOME DO VOLUNTARIO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O NOME DO VOLUNTARIO - SIM - OK
                       Voluntario.editarNome(dsn, voluntario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O NOME DO VOLUNTARIO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR O EMAIL DO VOLUNTARIO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O EMAIL DO VOLUNTARIO - SIM - OK
                       Voluntario.editarEmail(dsn, voluntario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O EMAIL DO VOLUNTARIO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    # EDITAR O CELULAR DO VOLUNTARIO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CELULAR DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CELULAR DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O CELULAR DO VOLUNTARIO - SIM - OK
                       Voluntario.editarCel(dsn, voluntario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O CELULAR DO VOLUNTARIO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 6):
                    # EDITAR A SENHA DO VOLUNTARIO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A SENHA DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A SENHA DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR A SENHA DO VOLUNTARIO - SIM - OK
                       Voluntario.editarSenha(dsn, voluntario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A SENHA DO VOLUNTARIO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 7):
                    # EDITAR O STATUS DO VOLUNTARIO - OK
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O STATUS DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O STATUS DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O STATUS DO VOLUNTARIO - SIM - OK
                       Voluntario.editarStatus(dsn, voluntario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O STATUS DO VOLUNTARIO - NÃO - OK
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 8):
                    # EDITAR A DATA DE REGISTRO DO VOLUNTARIO - OK
                    input(Funcoes.editarNegativo())

                elif (opcao == 9):
                    perfilVoluntario = False

    def excluirVoluntario(dsn, listaVoluntarios):
        
        if len(listaVoluntarios) == 0:
            print("NÃO EXISTEM VOLUNTARIOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirUsuariosAdmin(listaVoluntarios)
            try:
                id_buscado = int(input("DIGITE O ID DO VOLUNTARIO QUE DESEJA EXCLUIR: \n"))
                usuario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaVoluntarios)
                usuario_buscado = Funcoes.validarReceptorBuscado(usuario_buscado, listaVoluntarios)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O VOLUNTARIO")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O VOLUNTARIO"))

                if opcao == 1:
                    for i in range(len(listaVoluntarios)):
                        if listaVoluntarios[i].id_usuario == id_buscado:
                            novo_status_usuario = "INATIVO"

                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try:
                                # FAZENDO UPDATE NO BANCO DE DADOS - OK
                                cursor.execute("UPDATE usuario SET status_usuario = :novo_status_usuario WHERE id_usuario = :id_usuario", {"novo_status_usuario": novo_status_usuario, "id_usuario": usuario_buscado.id_usuario})
                                cursor.connection.commit()

                                # FAZENDO UPDATE NO CONSOLE - OK
                                usuario_buscado.status_usuario = novo_status_usuario

                                print("STATUS DO VOLUNTARIO ALTERADO PARA INATIVO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A ALTERAÇÃO DO STATUS DO VOLUNTARIO:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS - OK
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO VOLUNTARIO A SER EXCLUÍDO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO VOLUNTARIO:")
                print(str(e))
