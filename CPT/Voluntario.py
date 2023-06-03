import sqlite3

from datetime import datetime

from Colheita import Colheita
from Funcoes import Funcoes
from Plantio import Plantio
from Usuario import Usuario

class Voluntario(Usuario):
    def __init__(self, id_usuario: int = None, cpf_usuario: str = None, nome_usuario: str = None, email_usuario: str = None, cel_usuario: str = None, senha_usuario: str = None, status_usuario: str = None, data_registro_voluntario: str = None, colheitas_voluntario: list = None, plantios_voluntario: list = None):
        super()._init_(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario)
        self._data_registro_voluntario = data_registro_voluntario
        self._colheitas_voluntario = colheitas_voluntario if colheitas_voluntario is not None else []
        self._plantios_voluntario = plantios_voluntario if plantios_voluntario is not None else []

    @property
    def data_registro_voluntario(self) -> str:
        return self._data_registro_voluntario

    @data_registro_voluntario.setter
    def data_registro_voluntario(self, data_registro_voluntario: str):
        self._data_registro_voluntario = data_registro_voluntario

    @property
    def colheitas_voluntario(self):
        return self._colheitas_voluntario

    @colheitas_voluntario.setter
    def colheitas_voluntario(self, colheitas_voluntario: list):
        self._colheitas_voluntario = colheitas_voluntario

    @property
    def plantios_voluntario(self):
        return self._plantios_voluntario

    @plantios_voluntario.setter
    def plantios_voluntario(self, plantios_voluntario: list):
        self._plantios_voluntario = plantios_voluntario

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
        retornoPerfil += "09. COLHEITAS: "
        if len(voluntario_buscado.colheitas_voluntario) == 0:
            retornoPerfil += "NENHUMA COLHEITA REALIZADA.\n"
        else:
            for i, colheita in enumerate(voluntario_buscado.colheitas_voluntario):
                colheita_numero = f"{i+1:02d}"
                if i == 0:
                    retornoPerfil += f"\n 09.{colheita_numero}. ID: {colheita.id_colheita} | DATA: {colheita.data_colheita}\n"
                else:
                    retornoPerfil += f" 09.{colheita_numero}. ID: {colheita.id_colheita} | DATA: {colheita.data_colheita}\n"
        retornoPerfil += "10. PLANTIOS: "
        if len(voluntario_buscado.plantios_voluntario) == 0:
            retornoPerfil += "NENHUM PLANTIO REALIZADO.\n"
        else:
            for i, plantio in enumerate(voluntario_buscado.plantios_voluntario):
                plantio_numero = f"{i+1:02d}"
                if i == 0:
                    retornoPerfil += f"\n 10.{plantio_numero}. ID: {plantio.id_plantio} | ALIMENTO: {plantio.alimento.nome_alimento}\n"
                else:
                    retornoPerfil += f" 10.{plantio_numero}. ID: {plantio.id_plantio} | ALIMENTO: {plantio.alimento.nome_alimento}\n"
        retornoPerfil += "11. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarVoluntario(dsn, id_usuario, listaUsuarios, listaVoluntarios, listaColheitas, listaPlantios):
        
        if (len(listaUsuarios) == 0):
            input("NENHUM USUÁRIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirUsuariosAdmin(listaUsuarios)
            id_buscado = int(input("DIGITE O ID DO USUÁRIO QUE DESEJA CADASTRAR COMO DOADOR: \n"))
            usuario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaUsuarios)
            usuario_buscado = Funcoes.validarUsuarioBuscado(usuario_buscado, listaUsuarios)

        # INSTANCIANDO NOVO VOLUNTARIO
        novo_voluntario = Voluntario()

        # SETANDO OS ATRIBUTOS DO NOVO VOLUNTARIO PARA O NOVO VOLUNTARIO
        id_usuario = usuario_buscado.id_usuario
        cpf_usuario = usuario_buscado.cpf_usuario
        nome_usuario = usuario_buscado.nome_usuario
        email_usuario = usuario_buscado.email_usuario
        cel_usuario = usuario_buscado.cel_usuario
        senha_usuario = usuario_buscado.senha_usuario
        status_usuario = usuario_buscado.status_usuario

        # SETANDO A DATA DE REGISTRO DO NOVO VOLUNTARIO
        data_registro_voluntario = datetime.fromtimestamp(datetime.now().timestamp()).strftime('%d/%m/%Y')

        # SETANDO AS COLHEITAS DO NOVO VOLUNTARIO
        colheitas_voluntario = []
        
        # SETANDO OS PLANTIOS DO NOVO VOLUNTARIO
        plantios_voluntario = []

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS
            cursor.execute("INSERT INTO voluntario (id_usuario, data_registro_voluntario) VALUES (:1, :2)", (id_usuario, data_registro_voluntario))
            cursor.connection.commit()

            if len(colheitas_voluntario) != 0:
                for colheita_voluntario in colheitas_voluntario:
                    cursor.execute("INSERT INTO colheita_voluntario (id_colheita, id_usuario) VALUES (:1, :2)", (colheita_voluntario.id_colheita, id_usuario))
                    cursor.connection.commit()

            if len(plantios_voluntario) != 0:
                for plantio_voluntario in plantios_voluntario:
                    cursor.execute("INSERT INTO plantio_voluntario (id_plantio, id_usuario) VALUES (:1, :2)", (plantio_voluntario.id_plantio, id_usuario))
                    cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE
            novo_voluntario.id_usuario = id_usuario
            novo_voluntario.cpf_usuario = cpf_usuario
            novo_voluntario.nome_usuario = nome_usuario
            novo_voluntario.email_usuario = email_usuario
            novo_voluntario.cel_usuario = cel_usuario
            novo_voluntario.senha_usuario = senha_usuario
            novo_voluntario.status_usuario = status_usuario
            novo_voluntario.data_registro_voluntario = data_registro_voluntario
            novo_voluntario.colheitas_voluntario = colheitas_voluntario
            novo_voluntario.plantios_voluntario = plantios_voluntario

            listaVoluntarios.append(novo_voluntario)

            print("VOLUNTARIO CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO VOLUNTARIO:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
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
                    # EDITAR O ID DO VOLUNTARIO
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR O CPF DO VOLUNTARIO
                    input(Funcoes.editarNegativo())

                elif (opcao == 3):
                    # EDITAR O NOME DO VOLUNTARIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O NOME DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O NOME DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O NOME DO VOLUNTARIO - SIM
                       Voluntario.editarNome(dsn, voluntario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O NOME DO VOLUNTARIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR O EMAIL DO VOLUNTARIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O EMAIL DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O EMAIL DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O EMAIL DO VOLUNTARIO - SIM
                       Voluntario.editarEmail(dsn, voluntario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O EMAIL DO VOLUNTARIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 5):
                    # EDITAR O CELULAR DO VOLUNTARIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O CELULAR DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O CELULAR DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O CELULAR DO VOLUNTARIO - SIM
                       Voluntario.editarCel(dsn, voluntario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O CELULAR DO VOLUNTARIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 6):
                    # EDITAR A SENHA DO VOLUNTARIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A SENHA DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A SENHA DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR A SENHA DO VOLUNTARIO - SIM
                       Voluntario.editarSenha(dsn, voluntario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A SENHA DO VOLUNTARIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 7):
                    # EDITAR O STATUS DO VOLUNTARIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O STATUS DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O STATUS DO VOLUNTARIO DE ID {voluntario_buscado.id_usuario}")))
                    
                    if (opcao == 1):
                       # EDITAR O STATUS DO VOLUNTARIO - SIM
                       Voluntario.editarStatus(dsn, voluntario_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O STATUS DO VOLUNTARIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 8):
                    # EDITAR A DATA DE REGISTRO DO VOLUNTARIO
                    input(Funcoes.editarNegativo())

                elif (opcao == 9):
                    perfilVoluntario = False

    def editarColheitas(dsn, voluntario_buscado, listaColheitas):
        try:
            novas_colheitas_voluntario = []

            if (len(listaColheitas) == 0):
                input("NENHUMA COLHEITA CADASTRADA. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirColheitasAdmin(listaColheitas)
                    id_buscado = int(input("DIGITE O ID DA COLHEITA QUE DESEJA INCLUIR AO VOLUNTÁRIO: \n"))
                    colheita_buscada = Funcoes.buscarColheitaPorId(id_buscado, listaColheitas)
                    colheita_buscada = Funcoes.validarColheitaBuscada(colheita_buscada, listaColheitas)
                    
                    novas_colheitas_voluntario.append(colheita_buscada)

                    opcao = int(input("DESEJA ADICIONAR MAIS UMA COLHEITA AO VOLUNTÁRIO?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UMA COLHEITA AO VOLUNTÁRIO?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("DELETE FROM colheita_voluntario WHERE id_usuario = :id_usuario", {"id_usuario": voluntario_buscado.id_usuario})
                cursor.connection.commit()
                
                for colheita_voluntario in novas_colheitas_voluntario:
                    cursor.execute("INSERT INTO colheita_voluntario (id_colheita, id_usuario) VALUES (:1, :2)", (colheita_voluntario.id_colheita, voluntario_buscado.id_usuario))
                    cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                for colheita in voluntario_buscado.colheitas_voluntario:
                    colheita.remover_voluntario(voluntario_buscado)

                voluntario_buscado.colheitas_voluntario = novas_colheitas_voluntario

                for colheita in voluntario_buscado.colheitas_voluntario:
                    colheita.adicionar_voluntario(voluntario_buscado)   

                print("COLHEITAS DO VOLUNTÁRIO EDITADAS COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DAS COLHEITAS:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA COLHEITA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA COLHEITA DO VOLUNTÁRIO:")
            print(str(e))

    def editarPlantios(dsn, voluntario_buscado, listaPlantios):
        try:
            novos_plantios_voluntario = []

            if (len(listaPlantios) == 0):
                input("NENHUM PLANTIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirPlantiosAdmin(listaPlantios)
                    id_buscado = int(input("DIGITE O ID DO PLANTIO QUE DESEJA INCLUIR AO VOLUNTÁRIO: \n"))
                    plantio_buscado = Funcoes.buscarPlantioPorId(id_buscado, listaPlantios)
                    plantio_buscado = Funcoes.validarPlantioBuscado(plantio_buscado, listaPlantios)
                    
                    novos_plantios_voluntario.append(plantio_buscado)

                    opcao = int(input("DESEJA ADICIONAR MAIS UM PLANTIO AO VOLUNTÁRIO?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UM PLANTIO AO VOLUNTÁRIO?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("DELETE FROM plantio_voluntario WHERE id_usuario = :id_usuario", {"id_usuario": voluntario_buscado.id_usuario})
                cursor.connection.commit()
                
                for plantio_voluntario in novos_plantios_voluntario:
                    cursor.execute("INSERT INTO plantio_voluntario (id_plantio, id_usuario) VALUES (:1, :2)", (plantio_voluntario.id_plantio, voluntario_buscado.id_usuario))
                    cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                for plantio in voluntario_buscado.plantios_voluntario:
                    plantio.remover_voluntario(voluntario_buscado)

                voluntario_buscado.plantios_voluntario = novos_plantios_voluntario

                for plantio in voluntario_buscado.plantios_voluntario:
                    plantio.adicionar_voluntario(voluntario_buscado)   

                print("PLANTIOS DO VOLUNTÁRIO EDITADOS COM SUCESSO!")

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
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO PLANTIO DO VOLUNTÁRIO:")
            print(str(e))

    def adicionar_plantio(self, plantio_adicionar):
        for plantio_existente in self.plantios_voluntario:
            if plantio_existente.id_plantio == plantio_adicionar.id_plantio:
                return
        self.plantios_voluntario.append(plantio_adicionar)

    def remover_plantio(self, plantio_remover):
        for plantio_existente in self.plantios_voluntario:
            if plantio_existente.id_plantio == plantio_remover.id_plantio:
                self.plantios_voluntario.remove(plantio_existente)
                return

    def adicionar_colheita(self, colheita_adicionar):
        for colheita_existente in self.colheitas_voluntario:
            if colheita_existente.id_colheita == colheita_adicionar.id_colheita:
                return
        self.colheitas_voluntario.append(colheita_adicionar)

    def remover_colheita(self, colheita_remover):
        for colheita_existente in self.colheitas_voluntario:
            if colheita_existente.id_colheita == colheita_remover.id_colheita:
                self.colheitas_voluntario.remove(colheita_existente)
                return

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
                                # FAZENDO UPDATE NO BANCO DE DADOS
                                cursor.execute("UPDATE usuario SET status_usuario = :novo_status_usuario WHERE id_usuario = :id_usuario", {"novo_status_usuario": novo_status_usuario, "id_usuario": usuario_buscado.id_usuario})
                                cursor.connection.commit()

                                # FAZENDO UPDATE NO CONSOLE
                                usuario_buscado.status_usuario = novo_status_usuario

                                print("STATUS DO VOLUNTARIO ALTERADO PARA INATIVO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A ALTERAÇÃO DO STATUS DO VOLUNTARIO:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO VOLUNTARIO A SER EXCLUÍDO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO VOLUNTARIO:")
                print(str(e))
