import sqlite3

from Funcoes import Funcoes
from Usuario import Usuario

class Doador(Usuario):
    def __init__(self, id_usuario: int = None, cpf_usuario: str = None, nome_usuario: str = None, email_usuario: str = None, cel_usuario: str = None, senha_usuario: str = None, status_usuario: str = None, nivel_doador: int = None, moedas_doador: int = None, doacoes_doador: list = None):
        super()._init_(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
        self._nivel_doador = nivel_doador
        self._moedas_doador = moedas_doador
        self._doacoes_doador = doacoes_doador if doacoes_doador is not None else []

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

    @property
    def doacoes_doador(self):
        return self._doacoes_doador

    @doacoes_doador.setter
    def doacoes_doador(self, doacoes_doador: list):
        self._doacoes_doador = doacoes_doador

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
        retornoPerfil += "10. DOAÇÕES: "
        if len(doador_buscado.doacoes_doador) == 0:
            retornoPerfil += "NENHUMA DOAÇÃO REALIZADA.\n"
        else:
            for i, doacao in enumerate(doador_buscado.doacoes_doador):
                doacao_numero = f"{i+1:02d}"
                if i == 0:
                    retornoPerfil += f"\n 10.{doacao_numero}. ID: {doacao.id_doacao} | DATA: {doacao.data_doacao}\n"
                else:
                    retornoPerfil += f" 10.{doacao_numero}. ID: {doacao.id_doacao} | DATA: {doacao.data_doacao}\n"
        retornoPerfil += "11. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarDoador(dsn, id_usuario, listaUsuarios, listaDoadores):
        
        if (len(listaUsuarios) == 0):
            input("NENHUM USUÁRIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirUsuariosAdmin(listaUsuarios)
            id_buscado = int(input("DIGITE O ID DO USUÁRIO QUE DESEJA CADASTRAR COMO DOADOR: \n"))
            usuario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaUsuarios)
            usuario_buscado = Funcoes.validarUsuarioBuscado(usuario_buscado, listaUsuarios)

        # INSTANCIANDO NOVO DOADOR
        novo_doador = Doador()

        # SETANDO OS ATRIBUTOS DO NOVO DOADOR PARA O NOVO DOADOR
        id_usuario = usuario_buscado.id_usuario
        cpf_usuario = usuario_buscado.cpf_usuario
        nome_usuario = usuario_buscado.nome_usuario
        email_usuario = usuario_buscado.email_usuario
        cel_usuario = usuario_buscado.cel_usuario
        senha_usuario = usuario_buscado.senha_usuario
        status_usuario = usuario_buscado.status_usuario

        # SETANDO O NÍVEL DO NOVO DOADOR
        nivel_doador = 0
        
        # SETANDO A QUANTIDADE DE MOEDAS DO NOVO DOADOR
        qtd_moedas_doador = 0
        
        # SETANDO AS DOAÇÕES DO NOVO DOADOR
        doacoes_doador = []
    
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
            novo_doador.moedas_doador = qtd_moedas_doador
            novo_doador.doacoes_doador = doacoes_doador
            listaDoadores.append(novo_doador)

            print("DOADOR CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO DOADOR:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

    def editarDoador(dsn, listaDoadores, listaDoacoes):
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
                opcao = int(Funcoes.validarOpcao(opcao, 1, 11, Doador.perfilDoador(doador_buscado)))

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

                elif (opcao == 10):
                    # EDITAR AS DOAÇÕES DO DOADOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR AS DOAÇÕES DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR AS DOAÇÕES DO DOADOR DE ID {doador_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR AS DOAÇÕES DO DOADOR - SIM
                       Doador.editarDoador(dsn, doador_buscado, listaDoacoes)
                    
                    elif (opcao == 2):
                        # EDITAR AS DOAÇÕES DO DOADOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 11):
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

    def editarDoacoes(dsn, doador_buscado, listaDoacoes):
        try:
            novas_doacoes_doador = []

            if (len(listaDoacoes) == 0):
                input("NENHUMA DOAÇÃO CADASTRADA. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirDoacoesAdmin(listaDoacoes)
                    id_buscado = int(input("DIGITE O ID DA DOAÇÃO QUE DESEJA INCLUIR AO DOADOR: \n"))
                    doacao_buscada = Funcoes.buscarDoacaoPorId(id_buscado, listaDoacoes)
                    doacao_buscada = Funcoes.validarDoacaoBuscada(doacao_buscada, listaDoacoes)
                    
                    novas_doacoes_doador.append(doacao_buscada)

                    opcao = int(input("DESEJA ADICIONAR MAIS UMA DOAÇÃO AO DOADOR?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UMA DOAÇÃO AO DOADOR?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("DELETE FROM doacao WHERE id_usuario = :id_usuario", {"id_usuario": doador_buscado.id_usuario})
                cursor.connection.commit()
                
                for doacao_doador in novas_doacoes_doador:
                    cursor.execute("INSERT INTO doacao (id_doacao, id_usuario, data_doacao, qtd_moedas_doacao) VALUES (:1, :2, :3, :4)", (doacao_doador.id_doacao, doador_buscado.id_usuario, doacao_doador.data_doacao, doacao_doador.qtd_moedas_doacao))
                    cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                for doacao in doador_buscado.doacoes_doador:
                    doacao.remover_doacao(doacao)

                doador_buscado.doacoes_doador = novas_doacoes_doador

                for doacao in doador_buscado.doacoes_doador:
                    doacao.adicionar_doacao(doacao)                    

                print("DOAÇÕES DO DOADOR EDITADAS COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DAS DOAÇÕES:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA DOAÇÃO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA DOAÇÃO DO DOADOR:")
            print(str(e))

    def adicionar_doacao(self, doacao_adicionar):
        for doacao_existente in self.doacaos_receptor:
            if doacao_existente.id_doacao == doacao_adicionar.id_doacao:
                return
        self.doacaos_receptor.append(doacao_adicionar)

    def remover_doacao(self, doacao_remover):
        for doacao_existente in self.doacaos_receptor:
            if doacao_existente.id_doacao == doacao_remover.id_doacao:
                self.doacaos_receptor.remove(doacao_existente)
                return

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