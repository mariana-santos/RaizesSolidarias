import sqlite3
import copy

from Funcoes import Funcoes
from Usuario import Usuario

class Receptor(Usuario):
    def __init__(self, id_usuario: int = None, cpf_usuario: str = None, nome_usuario: str = None, email_usuario: str = None, cel_usuario: str = None, senha_usuario: str = None, status_usuario: str = None, carga_receptor: int = None, endereco_receptor: str = None, destinos_receptor: list = None, agendamentos_receptor: list = None):
        super().__init__(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
        self._carga_receptor = carga_receptor
        self._endereco_receptor = endereco_receptor
        self._destinos_receptor = destinos_receptor if destinos_receptor is not None else []
        self._agendamentos_receptor = agendamentos_receptor if agendamentos_receptor is not None else []

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

    @property
    def destinos_receptor(self):
        return self._destinos_receptor

    @destinos_receptor.setter
    def destinos_receptor(self, destinos_receptor: list):
        self._destinos_receptor = destinos_receptor

    @property
    def agendamentos_receptor(self):
        return self._agendamentos_receptor

    @agendamentos_receptor.setter
    def agendamentos_receptor(self, agendamentos_receptor: list):
        self._agendamentos_receptor = agendamentos_receptor

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
        retornoPerfil += "10. DESTINOS: "
        if len(receptor_buscado.destinos_receptor) == 0:
            retornoPerfil += "NENHUM DESTINO ATENDIDO.\n"
        else:
            for i, destino in enumerate(receptor_buscado.destinos_receptor):
                destino_numero = f"{i+1:02d}"
                if i == 0:
                    retornoPerfil += f"\n 10.{destino_numero}. ID: {destino.id_destino} | ENDEREÇO: {destino.endereco_destino}\n"
                else:
                    retornoPerfil += f" 10.{destino_numero}. ID: {destino.id_destino} | ENDEREÇO: {destino.endereco_destino}\n"
        retornoPerfil += "11. AGENDAMENTOS: "
        if len(receptor_buscado.agendamentos_receptor) == 0:
            retornoPerfil += "NENHUM AGENDAMENTO REALIZADO.\n"
        else:
            for i, agendamento in enumerate(receptor_buscado.agendamentos_receptor):
                agendamento_numero = f"{i+1:02d}"
                if i == 0:
                    retornoPerfil += f"\n 11.{agendamento_numero}. ID: {agendamento.id_agendamento} | DATA: {Funcoes.formatarData(agendamento.data_agendamento)}\n"
                else:
                    retornoPerfil += f" 11.{agendamento_numero}. ID: {agendamento.id_agendamento} | DATA: {Funcoes.formatarData(agendamento.data_agendamento)}\n"
        retornoPerfil += "12. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarReceptor(dsn, id_usuario, listaUsuariosNaoReceptores, listaReceptores, listaDestinos):
        
        if (len(listaUsuariosNaoReceptores) == 0):
            input("NENHUM USUÁRIO PARA CADASTRAR COMO RECEPTOR. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirUsuariosAdmin(listaUsuariosNaoReceptores)
            id_buscado = int(input("DIGITE O ID DO USUÁRIO QUE DESEJA CADASTRAR COMO RECEPTOR: \n"))
            usuario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaUsuariosNaoReceptores)
            usuario_buscado = Funcoes.validarUsuarioBuscado(usuario_buscado, listaUsuariosNaoReceptores)

        # INSTANCIANDO NOVO RECEPTOR
        novo_receptor = Receptor()

        # SETANDO OS ATRIBUTOS DO NOVO RECEPTOR PARA O NOVO RECEPTOR
        id_usuario = usuario_buscado.id_usuario
        cpf_usuario = usuario_buscado.cpf_usuario
        nome_usuario = usuario_buscado.nome_usuario
        email_usuario = usuario_buscado.email_usuario
        cel_usuario = usuario_buscado.cel_usuario
        senha_usuario = usuario_buscado.senha_usuario
        status_usuario = usuario_buscado.status_usuario

        # SETANDO A CARGA DO NOVO RECEPTOR
        try:
            carga_receptor = int(input(f"DIGITE A CAPACIDADE MÁXIMA DA CARGA DO NOVO RECEPTOR (EM KGS, NÚMERO INTEIRO): "))
            carga_receptor = int(Funcoes.validarPreenchimento(f"DIGITE A CAPACIDADE MÁXIMA DA CARGA DO NOVO RECEPTOR (EM KGS, NÚMERO INTEIRO): ", carga_receptor))

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA CARGA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA CARGA DO RECEPTOR:")
            print(str(e))
        
        # SETANDO O ENDEREÇO DO NOVO RECEPTOR
        try:
            endereco_receptor = input(f"DIGITE O ENDEREÇO DO NOVO RECEPTOR: ")
            endereco_receptor = Funcoes.validarPreenchimento(f"DIGITE O ENDEREÇO DO NOVO RECEPTOR: ", endereco_receptor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ENDEREÇO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO ENDEREÇO DO RECEPTOR:")
            print(str(e))

        # SETANDO OS DESTINOS DO NOVO RECEPTOR
        try:
            destinos_receptor = []

            listaDestinosTemp = copy.copy(listaDestinos)

            if (len(listaDestinosTemp) == 0):
                input("NENHUM DESTINO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirDestinosAdmin(listaDestinosTemp)
                    id_buscado = int(input("DIGITE O ID DO DESTINO QUE DESEJA INCLUIR AO RECEPTOR: \n"))
                    destino_buscado = Funcoes.buscarDestinoPorId(id_buscado, listaDestinosTemp)
                    destino_buscado = Funcoes.validarDestinoBuscado(destino_buscado, listaDestinosTemp)
                    
                    destinos_receptor.append(destino_buscado)
                    listaDestinosTemp.remove(destino_buscado)

                    opcao = int(input("DESEJA ADICIONAR MAIS UM DESTINO AO NOVO RECEPTOR?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UM DESTINO AO NOVO RECEPTOR?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO DESTINO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO DESTINO DO RECEPTOR:")
            print(str(e))
        
        # SETANDO OS AGENDAMENTOS DO NOVO RECEPTOR
        agendamentos_receptor = []

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS
            cursor.execute("INSERT INTO receptor (id_usuario, carga_receptor, endereco_receptor) VALUES (:1, :2, :3)", (id_usuario, carga_receptor, endereco_receptor))
            cursor.connection.commit()

            if len(destinos_receptor) != 0:
                for destino_receptor in destinos_receptor:
                    cursor.execute("INSERT INTO receptor_destino (id_usuario, id_destino) VALUES (:1, :2)", (id_usuario, destino_receptor.id_destino))
                    cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE
            novo_receptor.id_usuario = id_usuario
            novo_receptor.cpf_usuario = cpf_usuario
            novo_receptor.nome_usuario = nome_usuario
            novo_receptor.email_usuario = email_usuario
            novo_receptor.cel_usuario = cel_usuario
            novo_receptor.senha_usuario = senha_usuario
            novo_receptor.status_usuario = status_usuario
            novo_receptor.carga_receptor = carga_receptor
            novo_receptor.endereco_receptor = endereco_receptor
            novo_receptor.destinos_receptor = destinos_receptor
            novo_receptor.agendamentos_receptor = agendamentos_receptor
            
            listaReceptores.append(novo_receptor)
            listaUsuariosNaoReceptores.remove(usuario_buscado)

            for destino in destinos_receptor:
                destino.adicionar_receptor(novo_receptor)

            print("RECEPTOR CADASTRADO COM SUCESSO!")
            input("TECLE ENTER PARA VOLTAR AO MENU.")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO RECEPTOR:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

    def editarReceptor(dsn, listaReceptores, listaDestinos, listaAgendamentos, emails_cadastrados, cel_cadastrados):
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
                opcao = int(Funcoes.validarOpcao(opcao, 1, 12, Receptor.perfilReceptor(receptor_buscado)))

                if (opcao == 1):
                    # EDITAR O ID DO RECEPTOR
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR O CPF DO RECEPTOR
                    input(Funcoes.editarNegativo())

                elif (opcao == 3):
                    # EDITAR O NOME DO RECEPTOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O NOME DO RECEPTOR - SIM
                       Receptor.editarNome(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O NOME DO RECEPTOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR O EMAIL DO RECEPTOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O EMAIL DO RECEPTOR - SIM
                       Receptor.editarEmail(dsn, receptor_buscado, emails_cadastrados)
                    
                    elif (opcao == 2):
                        # EDITAR O EMAIL DO RECEPTOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    # EDITAR O CELULAR DO RECEPTOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CELULAR DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CELULAR DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O CELULAR DO RECEPTOR - SIM
                       Receptor.editarCel(dsn, receptor_buscado, cel_cadastrados)
                    
                    elif (opcao == 2):
                        # EDITAR O CELULAR DO RECEPTOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 6):
                    # EDITAR A SENHA DO RECEPTOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A SENHA DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A SENHA DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR A SENHA DO RECEPTOR - SIM
                       Receptor.editarSenha(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A SENHA DO RECEPTOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 7):
                    # EDITAR O STATUS DO RECEPTOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O STATUS DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O STATUS DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O STATUS DO RECEPTOR - SIM
                       Receptor.editarStatus(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O STATUS DO RECEPTOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 8):
                    # EDITAR A CARGA DO RECEPTOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A CARGA DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A CARGA DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR A CARGA DO RECEPTOR - SIM
                       Receptor.editarCarga(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A CARGA DO RECEPTOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 9):
                    # EDITAR O ENDEREÇO DO RECEPTOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O ENDEREÇO DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O ENDEREÇO DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O ENDEREÇO DO RECEPTOR - SIM
                       Receptor.editarEndereco(dsn, receptor_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O ENDEREÇO DO RECEPTOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 10):
                    # EDITAR OS DESTINOS DO RECEPTOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR OS DESTINOS DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR OS DESTINOS DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR OS DESTINOS DO RECEPTOR - SIM
                       Receptor.editarDestinos(dsn, receptor_buscado, listaDestinos)
                    
                    elif (opcao == 2):
                        # EDITAR OS DESTINOS DO RECEPTOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 11):
                    # EDITAR OS AGENDAMENTOS DO RECEPTOR
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR OS AGENDAMENTOS DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR OS AGENDAMENTOS DO RECEPTOR DE ID {receptor_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR OS AGENDAMENTOS DO RECEPTOR - SIM
                       Receptor.editarAgendamentos(dsn, receptor_buscado, listaAgendamentos)
                    
                    elif (opcao == 2):
                        # EDITAR OS AGENDAMENTOS DO RECEPTOR - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 12):
                    perfilReceptor = False

    def editarCarga(dsn, receptor_buscado):
        try:
            nova_carga = int(input(f"DIGITE A NOVA CARGA SUPORTADA DO RECEPTOR {receptor_buscado.nome_usuario}: "))
            nova_carga = int(Funcoes.validarPreenchimento(f"DIGITE A NOVA CARGA SUPORTADA DO RECEPTOR {receptor_buscado.nome_usuario}: ", nova_carga))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE receptor SET carga_receptor = :nova_carga WHERE id_usuario = :id_usuario", {"nova_carga": nova_carga, "id_usuario": receptor_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                receptor_buscado.carga_receptor = nova_carga

                print("CARGA DO RECEPTOR EDITADA COM SUCESSO!")
                input("TECLE ENTER PARA VOLTAR AO MENU.")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA CARGA:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
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

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE receptor SET endereco_receptor = :novo_endereco WHERE id_usuario = :id_usuario", {"novo_endereco": novo_endereco, "id_usuario": receptor_buscado.id_usuario})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                receptor_buscado.endereco_receptor = novo_endereco

                print("ENDEREÇO DO RECEPTOR EDITADO COM SUCESSO!")
                input("TECLE ENTER PARA VOLTAR AO MENU.")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO ENDEREÇO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO ENDEREÇO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO ENDEREÇO DO RECEPTOR:")
            print(str(e))

    def editarDestinos(dsn, receptor_buscado, listaDestinos):
        try:
            novos_destinos_receptor = []

            listaDestinosTemp = copy.copy(listaDestinos)

            if (len(listaDestinosTemp) == 0):
                input("NENHUM DESTINO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirDestinosAdmin(listaDestinosTemp)
                    id_buscado = int(input("DIGITE O ID DO DESTINO QUE DESEJA INCLUIR AO RECEPTOR: \n"))
                    destino_buscado = Funcoes.buscarDestinoPorId(id_buscado, listaDestinosTemp)
                    destino_buscado = Funcoes.validarDestinoBuscado(destino_buscado, listaDestinosTemp)
                    
                    novos_destinos_receptor.append(destino_buscado)
                    listaDestinosTemp.remove(destino_buscado)

                    opcao = int(input("DESEJA ADICIONAR MAIS UM DESTINO AO RECEPTOR?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UM DESTINO AO RECEPTOR?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("DELETE FROM receptor_destino WHERE id_usuario = :id_usuario", {"id_usuario": receptor_buscado.id_usuario})
                cursor.connection.commit()
                
                for destino_receptor in novos_destinos_receptor:
                    cursor.execute("INSERT INTO receptor_destino (id_usuario, id_destino) VALUES (:1, :2)", (receptor_buscado.id_usuario, destino_receptor.id_destino))
                    cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                for destino in receptor_buscado.destinos_receptor:
                    destino.remover_receptor(receptor_buscado)

                receptor_buscado.destinos_receptor = novos_destinos_receptor

                for destino in receptor_buscado.destinos_receptor:
                    destino.adicionar_receptor(receptor_buscado)                    

                print("DESTINOS DO RECEPTOR EDITADOS COM SUCESSO!")
                input("TECLE ENTER PARA VOLTAR AO MENU.")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DOS DESTINOS:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO DESTINO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO DESTINO DO RECEPTOR:")
            print(str(e))

    def editarAgendamentos(dsn, receptor_buscado, listaAgendamentos):
        try:
            novos_agendamentos_receptor = []

            listaAgendamentosTemp = copy.copy(listaAgendamentos)

            if (len(listaAgendamentosTemp) == 0):
                input("NENHUM AGENDAMENTO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirAgendamentosAdmin(listaAgendamentosTemp)
                    id_buscado = int(input("DIGITE O ID DO AGENDAMENTO QUE DESEJA INCLUIR AO RECEPTOR: \n"))
                    agendamento_buscado = Funcoes.buscarAgendamentoPorId(id_buscado, listaAgendamentosTemp)
                    agendamento_buscado = Funcoes.validarAgendamentoBuscado(agendamento_buscado, listaAgendamentosTemp)
                    
                    novos_agendamentos_receptor.append(agendamento_buscado)
                    listaAgendamentosTemp.remove(agendamento_buscado)

                    opcao = int(input("DESEJA ADICIONAR MAIS UM AGENDAMENTO AO RECEPTOR?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UM AGENDAMENTO AO RECEPTOR?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                agendamentos_excluir = []

                for agendamento_antigo_receptor in receptor_buscado.agendamentos_receptor:
                    agendamento_encontrado = False
                    for agendamento_receptor in novos_agendamentos_receptor:
                        if agendamento_antigo_receptor.id_agendamento == agendamento_receptor.id_agendamento:
                            agendamento_encontrado = True
                            cursor.execute("UPDATE agendamento SET id_usuario = :1 WHERE id_agendamento = :2", (receptor_buscado.id_usuario, agendamento_antigo_receptor.id_agendamento))
                            cursor.connection.commit()
                            break

                    if not agendamento_encontrado:
                        agendamentos_excluir.append(agendamento_antigo_receptor.id_agendamento)

                for id_agendamento_excluir in agendamentos_excluir:
                    cursor.execute("DELETE FROM agendamento WHERE id_agendamento = :1", (id_agendamento_excluir,))
                    cursor.connection.commit()

                for agendamento_receptor in novos_agendamentos_receptor:
                    cursor.execute("UPDATE agendamento SET id_usuario = :1 WHERE id_agendamento = :2", (receptor_buscado.id_usuario, agendamento_receptor.id_agendamento))
                    cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                receptor_buscado.agendamentos_receptor = novos_agendamentos_receptor

                for agendamento in receptor_buscado.agendamentos_receptor:
                    agendamento.usuario = receptor_buscado   

                print("AGENDAMENTOS DO RECEPTOR EDITADOS COM SUCESSO!")
                input("TECLE ENTER PARA VOLTAR AO MENU.")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DOS PLANTIOS:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO PLANTIO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO PLANTIO DO RECEPTOR:")
            print(str(e))

    def adicionar_destino(self, destino_adicionar):
        for destino_existente in self.destinos_receptor:
            if destino_existente.id_destino == destino_adicionar.id_destino:
                return
        self.destinos_receptor.append(destino_adicionar)

    def remover_destino(self, destino_remover):
        for destino_existente in self.destinos_receptor:
            if destino_existente.id_destino == destino_remover.id_destino:
                self.destinos_receptor.remove(destino_existente)
                return

    def adicionar_agendamento(self, agendamento_adicionar):
        for agendamento_existente in self.agendamentos_receptor:
            if agendamento_existente.id_agendamento == agendamento_adicionar.id_agendamento:
                return
        self.agendamentos_receptor.append(agendamento_adicionar)

    def remover_agendamento(self, agendamento_remover):
        for agendamento_existente in self.agendamentos_receptor:
            if agendamento_existente.id_agendamento == agendamento_remover.id_agendamento:
                self.agendamentos_receptor.remove(agendamento_existente)
                return

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
                            novo_status_usuario = "Inativo"

                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try:
                                # FAZENDO UPDATE NO BANCO DE DADOS
                                cursor.execute("DELETE FROM receptor_destino WHERE id_usuario = :1", (listaReceptores[i].id_usuario,))
                                cursor.connection.commit()

                                cursor.execute("UPDATE usuario SET status_usuario = :novo_status_usuario WHERE id_usuario = :id_usuario", {"novo_status_usuario": novo_status_usuario, "id_usuario": receptor_buscado.id_usuario})
                                cursor.connection.commit()

                                # FAZENDO UPDATE NO CONSOLE
                                for destino in listaReceptores[i].destinos_receptor:
                                    destino.remover_receptor(listaReceptores[i])

                                receptor_buscado.status_usuario = novo_status_usuario

                                print("STATUS DO RECEPTOR ALTERADO PARA INATIVO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A ALTERAÇÃO DO STATUS DO RECEPTOR:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO RECEPTOR A SER INATIVO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO RECEPTOR:")
                print(str(e))