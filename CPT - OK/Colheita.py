import sqlite3
import copy

from datetime import datetime

from Funcoes import Funcoes

class Colheita:
    def __init__(self, id_colheita: int = None, data_colheita: str = None, descricao_colheita: str = None, voluntarios_colheita: list = None, plantios_colheita: list = None):
        self._id_colheita = id_colheita
        self._data_colheita = data_colheita
        self._descricao_colheita = descricao_colheita
        self._voluntarios_colheita = voluntarios_colheita if voluntarios_colheita is not None else []
        self._plantios_colheita = plantios_colheita if plantios_colheita is not None else []

    @property
    def id_colheita(self) -> int:
        return self._id_colheita

    @id_colheita.setter
    def id_colheita(self, id_colheita: int):
        self._id_colheita = id_colheita

    @property
    def data_colheita(self) -> str:
        return self._data_colheita

    @data_colheita.setter
    def data_colheita(self, data_colheita: str):
        self._data_colheita = data_colheita

    @property
    def descricao_colheita(self) -> str:
        return self._descricao_colheita

    @descricao_colheita.setter
    def descricao_colheita(self, descricao_colheita: str):
        self._descricao_colheita = descricao_colheita

    @property
    def voluntarios_colheita(self):
        return self._voluntarios_colheita

    @voluntarios_colheita.setter
    def voluntarios_colheita(self, voluntarios_colheita: list):
        self._voluntarios_colheita = voluntarios_colheita

    @property
    def plantios_colheita(self):
        return self._plantios_colheita

    @plantios_colheita.setter
    def plantios_colheita(self, plantios_colheita: list):
        self._plantios_colheita = plantios_colheita

    def perfilColheita(colheita_buscada):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {colheita_buscada.id_colheita}\n"
        retornoPerfil += f"02. DATA: {Funcoes.formatarData(colheita_buscada.data_colheita)}\n"
        retornoPerfil += f"03. DESCRIÇÃO: {colheita_buscada.descricao_colheita}\n"
        retornoPerfil += "04. VOLUNTÁRIOS: "
        if len(colheita_buscada.voluntarios_colheita) == 0:
            retornoPerfil += "NENHUM VOLUNTÁRIO RESPONSÁVEL.\n"
        else:
            for i, voluntario in enumerate(colheita_buscada.voluntarios_colheita):
                voluntario_numero = f"{i+1:02d}"
                if i == 0:
                    retornoPerfil += f"\n 04.{voluntario_numero}. ID: {voluntario.id_usuario} | NOME: {voluntario.nome_usuario}\n"
                else:
                    retornoPerfil += f" 04.{voluntario_numero}. ID: {voluntario.id_usuario} | NOME: {voluntario.nome_usuario}\n"
        retornoPerfil += "05. PLANTIOS: "
        if len(colheita_buscada.plantios_colheita) == 0:
            retornoPerfil += "NENHUM PLANTIO ASSOCIADO.\n"
        else:
            for i, plantio in enumerate(colheita_buscada.plantios_colheita):
                plantio_numero = f"{i+1:02d}"
                if i == 0:
                    retornoPerfil += f"\n 05.{plantio_numero}. ID: {plantio.id_plantio} | ALIMENTO: {plantio.alimento.nome_alimento}\n"
                else:
                    retornoPerfil += f" 05.{plantio_numero}. ID: {plantio.id_plantio} | ALIMENTO: {plantio.alimento.nome_alimento}\n"
        retornoPerfil += "06. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarColheita(dsn, id_colheita, listaColheitas, listaVoluntarios, listaPlantios):
        # INSTANCIANDO NOVA COLHEITA
        nova_colheita = Colheita()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVA COLHEITA
        id_colheita = id_colheita

        # SETANDO A DATA DA NOVA COLHEITA
        try:
            data_colheita = input(f"DIGITE A DATA DA COLHEITA (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            data_colheita = Funcoes.validarPreenchimento(f"DIGITE A DATA DA COLHEITA (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", data_colheita)
            data_formatada = datetime.strptime(data_colheita, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%d/%m/%Y")

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA DATA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA DATA DA COLHEITA:")
            print(str(e))
    
        # SETANDO A DESCRIÇÃO DA NOVA COLHEITA
        try:
            descricao_colheita = input(f"DIGITE A DESCRIÇÃO DA COLHEITA: ")
            descricao_colheita = Funcoes.validarPreenchimento(f"DIGITE A DESCRIÇÃO DA COLHEITA: ", descricao_colheita)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA DESCRIÇÃO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA DESCRIÇÃO DA COLHEITA:")
            print(str(e))

        # SETANDO OS VOLUNTÁRIOS DA NOVA COLHEITA
        try:
            voluntarios_colheita = []

            listaVoluntariosTemp = copy.copy(listaVoluntarios)

            if (len(listaVoluntariosTemp) == 0):
                input("NENHUM VOLUNTÁRIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirUsuariosAdmin(listaVoluntariosTemp)
                    id_buscado = int(input("DIGITE O ID DO VOLUNTÁRIO QUE DESEJA INCLUIR À COLHEITA: \n"))
                    voluntario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaVoluntariosTemp)
                    voluntario_buscado = Funcoes.validarUsuarioBuscado(voluntario_buscado, listaVoluntariosTemp)
                    
                    voluntarios_colheita.append(voluntario_buscado)
                    listaVoluntariosTemp.remove(voluntario_buscado)

                    opcao = int(input("DESEJA ADICIONAR MAIS UM VOLUNTÁRIO À NOVA COLHEITA?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UM VOLUNTÁRIO À NOVA COLHEITA?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO VOLUNTÁRIO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO VOLUNTÁRIO DA COLHEITA:")
            print(str(e))

        # SETANDO OS PLANTIOS DA NOVA COLHEITA
        try:
            plantios_colheita = []

            listaPlantiosTemp = copy.copy(listaPlantios)

            if (len(listaPlantiosTemp) == 0):
                input("NENHUM PLANTIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirPlantiosAdmin(listaPlantiosTemp)
                    id_buscado = int(input("DIGITE O ID DO PLANTIO QUE DESEJA INCLUIR À COLHEITA: \n"))
                    plantio_buscado = Funcoes.buscarPlantioPorId(id_buscado, listaPlantiosTemp)
                    plantio_buscado = Funcoes.validarPlantioBuscado(plantio_buscado, listaPlantiosTemp)
                    
                    plantios_colheita.append(plantio_buscado)
                    listaPlantiosTemp.remove(plantio_buscado)

                    opcao = int(input("DESEJA ADICIONAR MAIS UM PLANTIO À NOVA COLHEITA?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UM PLANTIO À NOVA COLHEITA?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO PLANTIO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO PLANTIO DA COLHEITA:")
            print(str(e))
        
        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS
            cursor.execute("INSERT INTO colheita (id_colheita, data_colheita, descricao_colheita) VALUES (:1, TO_DATE(:2, 'DD/MM/YYYY'), :3)", (id_colheita, data_formatada_banco, descricao_colheita))
            cursor.connection.commit()

            if len(voluntarios_colheita) != 0:
                for voluntario_colheita in voluntarios_colheita:
                    cursor.execute("INSERT INTO colheita_voluntario (id_colheita, id_usuario) VALUES (:1, :2)", (id_colheita, voluntario_colheita.id_usuario))
                    cursor.connection.commit()

            if len(plantios_colheita) != 0:
                for plantio_colheita in plantios_colheita:
                    cursor.execute("INSERT INTO plantio_colheita (id_plantio, id_colheita) VALUES (:1, :2)", (plantio_colheita.id_plantio, id_colheita))
                    cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE
            nova_colheita.id_colheita = id_colheita
            nova_colheita.data_colheita = data_formatada
            nova_colheita.descricao_colheita = descricao_colheita
            nova_colheita.voluntarios_colheita = voluntarios_colheita
            nova_colheita.plantios_colheita = plantios_colheita

            listaColheitas.append(nova_colheita)

            for voluntario in voluntarios_colheita:
                voluntario.adicionar_colheita(nova_colheita)

            for plantio in plantios_colheita:
                plantio.colheita = nova_colheita

            print("COLHEITA CADASTRADA COM SUCESSO!")
            input("TECLE ENTER PARA VOLTAR AO MENU.")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DA COLHEITA:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

    def editarColheita(dsn, listaColheitas, listaVoluntarios, listaPlantios):
        perfilColheita = True

        if (len(listaColheitas) == 0):
            input("NENHUMA COLHEITA CADASTRADA. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirColheitasAdmin(listaColheitas)
            id_buscado = int(input("DIGITE O ID DA COLHEITA QUE DESEJA EDITAR: \n"))
            colheita_buscada = Funcoes.buscarColheitaPorId(id_buscado, listaColheitas)
            colheita_buscada = Funcoes.validarColheitaBuscada(colheita_buscada, listaColheitas)

            while (perfilColheita):
                opcao = int(input(Colheita.perfilColheita(colheita_buscada)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 7, Colheita.perfilColheita(colheita_buscada)))

                if (opcao == 1):
                    # EDITAR O ID DA COLHEITA
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR A DATA DA COLHEITA
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DATA DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DATA DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    
                    if (opcao == 1):
                       # EDITAR A DATA DA COLHEITA - SIM
                       Colheita.editarData(dsn, colheita_buscada)
                    
                    elif (opcao == 2):
                        # EDITAR A DATA DA COLHEITA - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 3):
                    # EDITAR A DESCRIÇÃO DA COLHEITA
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DESCRIÇÃO DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DESCRIÇÃO DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    
                    if (opcao == 1):
                       # EDITAR A DESCRIÇÃO DA COLHEITA - SIM
                       Colheita.editarDescricao(dsn, colheita_buscada)
                    
                    elif (opcao == 2):
                        # EDITAR A DESCRIÇÃO DA COLHEITA - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 4):
                    # EDITAR OS VOLUNTÁRIOS DA COLHEITA
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR OS VOLUNTÁRIOS DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR OS VOLUNTÁRIOS DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    
                    if (opcao == 1):
                       # EDITAR OS VOLUNTÁRIOS DA COLHEITA - SIM
                       Colheita.editarVoluntarios(dsn, colheita_buscada, listaVoluntarios)
                    
                    elif (opcao == 2):
                        # EDITAR OS VOLUNTÁRIOS DA COLHEITA - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 5):
                    # EDITAR OS PLANTIOS DA COLHEITA
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR OS PLANTIOS DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR OS PLANTIOS DA COLHEITA DE ID {colheita_buscada.id_colheita}")))
                    
                    if (opcao == 1):
                       # EDITAR OS PLANTIOS DA COLHEITA - SIM
                       Colheita.editarPlantios(dsn, colheita_buscada, listaPlantios)
                    
                    elif (opcao == 2):
                        # EDITAR OS PLANTIOS DA COLHEITA - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 6):
                    perfilColheita = False

    def editarData(dsn, colheita_buscada):
        try:
            nova_data = input(f"DIGITE A NOVA DATA DA COLHEITA DE ID {colheita_buscada.id_colheita} (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            nova_data = Funcoes.validarPreenchimento(f"DIGITE A NOVA DATA DA COLHEITA DE ID {colheita_buscada.id_colheita} (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", nova_data)
            data_formatada = datetime.strptime(nova_data, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%d/%m/%Y")

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE colheita SET data_colheita = TO_DATE(:data_formatada_banco, 'DD/MM/YYYY') WHERE id_colheita = :id_colheita", {"data_formatada_banco": data_formatada_banco, "id_colheita": colheita_buscada.id_colheita})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                colheita_buscada.data_colheita = data_formatada

                print("DATA DA COLHEITA EDITADA COM SUCESSO!")
                input("TECLE ENTER PARA VOLTAR AO MENU.")

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
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA DATA DA COLHEITA:")
            print(str(e))
    
    def editarDescricao(dsn, colheita_buscada):
        try:
            nova_descricao = input(f"DIGITE A NOVA DESCRIÇÃO DA COLHEITA DE ID {colheita_buscada.id_colheita}: ")
            nova_descricao = Funcoes.validarPreenchimento(f"DIGITE A NOVA DESCRIÇÃO DA COLHEITA DE ID {colheita_buscada.id_colheita}: ", nova_descricao)

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE colheita SET descricao_colheita = :nova_descricao WHERE id_colheita = :id_colheita", {"nova_descricao": nova_descricao, "id_colheita": colheita_buscada.id_colheita})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                colheita_buscada.descricao_colheita = nova_descricao

                print("DESCRIÇÃO DA COLHEITA EDITADA COM SUCESSO!")
                input("TECLE ENTER PARA VOLTAR AO MENU.")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA DESCRIÇÃO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA DESCRIÇÃO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA DESCRIÇÃO DA COLHEITA:")
            print(str(e))

    def editarVoluntarios(dsn, colheita_buscada, listaVoluntarios):
        try:
            novos_voluntarios_colheita = []

            listaVoluntariosTemp = copy.copy(listaVoluntarios)

            if (len(listaVoluntarios) == 0):
                input("NENHUM VOLUNTÁRIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirUsuariosAdmin(listaVoluntariosTemp)
                    id_buscado = int(input("DIGITE O ID DO VOLUNTÁRIO QUE DESEJA INCLUIR À COLHEITA: \n"))
                    voluntario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaVoluntariosTemp)
                    voluntario_buscado = Funcoes.validarUsuarioBuscado(voluntario_buscado, listaVoluntariosTemp)
                    
                    novos_voluntarios_colheita.append(voluntario_buscado)
                    listaVoluntariosTemp.remove(voluntario_buscado)

                    opcao = int(input("DESEJA ADICIONAR MAIS UM VOLUNTÁRIO À COLHEITA?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UM VOLUNTÁRIO À COLHEITA?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("DELETE FROM colheita_voluntario WHERE id_colheita = :id_colheita", {"id_colheita": colheita_buscada.id_colheita})
                cursor.connection.commit()
                
                for voluntario_colheita in novos_voluntarios_colheita:
                    cursor.execute("INSERT INTO colheita_voluntario (id_colheita, id_usuario) VALUES (:1, :2)", (colheita_buscada.id_colheita, voluntario_colheita.id_usuario))
                    cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                for voluntario in colheita_buscada.voluntarios_colheita:
                    voluntario.remover_colheita(colheita_buscada)

                colheita_buscada.voluntarios_colheita = novos_voluntarios_colheita

                for voluntario in colheita_buscada.voluntarios_colheita:
                    voluntario.adicionar_colheita(colheita_buscada)   

                print("VOLUNTÁRIOS DA COLHEITA EDITADOS COM SUCESSO!")
                input("TECLE ENTER PARA VOLTAR AO MENU.")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DOS VOLUNTÁRIOS:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO VOLUNTÁRIO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO VOLUNTÁRIO DA COLHEITA:")
            print(str(e))

    def editarPlantios(dsn, colheita_buscada, listaPlantios):
        try:
            novos_plantios_colheita = []

            listaPlantiosTemp = copy.copy(listaPlantios)

            if (len(listaPlantiosTemp) == 0):
                input("NENHUM PLANTIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirPlantiosAdmin(listaPlantiosTemp)
                    id_buscado = int(input("DIGITE O ID DO PLANTIO QUE DESEJA INCLUIR À COLHEITA: \n"))
                    plantio_buscado = Funcoes.buscarPlantioPorId(id_buscado, listaPlantiosTemp)
                    plantio_buscado = Funcoes.validarPlantioBuscado(plantio_buscado, listaPlantiosTemp)
                    
                    novos_plantios_colheita.append(plantio_buscado)
                    listaPlantiosTemp.remove(plantio_buscado)

                    opcao = int(input("DESEJA ADICIONAR MAIS UM PLANTIO À COLHEITA?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UM PLANTIO À COLHEITA?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("DELETE FROM plantio_colheita WHERE id_colheita = :id_colheita", {"id_colheita": colheita_buscada.id_colheita})
                cursor.connection.commit()
                
                for plantio_colheita in novos_plantios_colheita:
                    cursor.execute("INSERT INTO plantio_colheita (id_plantio, id_colheita) VALUES (:1, :2)", (plantio_colheita.id_plantio, colheita_buscada.id_colheita))
                    cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                for plantio in colheita_buscada.plantios_colheita:
                    plantio.colheita = None

                print(colheita_buscada.plantios_colheita)
                colheita_buscada.plantios_colheita = novos_plantios_colheita
                print(colheita_buscada.plantios_colheita)

                for plantio in colheita_buscada.plantios_colheita:
                    plantio.colheita = colheita_buscada   

                print("PLANTIOS DA COLHEITA EDITADOS COM SUCESSO!")
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
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO PLANTIO DA COLHEITA:")
            print(str(e))

    def adicionar_voluntario(self, voluntario_adicionar):
        for voluntario_existente in self.voluntarios_colheita:
            if voluntario_existente.id_usuario == voluntario_adicionar.id_usuario:
                return
        self.voluntarios_colheita.append(voluntario_adicionar)

    def remover_voluntario(self, voluntario_remover):
        for voluntario_existente in self.voluntarios_colheita:
            if voluntario_existente.id_usuario == voluntario_remover.id_usuario:
                self.voluntarios_colheita.remove(voluntario_existente)
                return

    def adicionar_plantio(self, plantio_adicionar):
        for plantio_existente in self.plantios_colheita:
            if plantio_existente.id_plantio == plantio_adicionar.id_plantio:
                return
        self.plantios_colheita.append(plantio_adicionar)

    def remover_plantio(self, plantio_remover):
        for plantio_existente in self.plantios_colheita:
            if plantio_existente.id_plantio == plantio_remover.id_plantio:
                self.plantios_colheita.remove(plantio_existente)
                return

    def excluirColheita(dsn, listaColheitas):
        
        if len(listaColheitas) == 0:
            print("NÃO EXISTEM COLHEITAS CADASTRADAS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirColheitasAdmin(listaColheitas)
            try:
                id_buscado = int(input("DIGITE O ID DA COLHEITA QUE DESEJA EXCLUIR: \n"))
                colheita_buscada = Funcoes.buscarColheitaPorId(id_buscado, listaColheitas)
                colheita_buscada = Funcoes.validarColheitaBuscada(colheita_buscada, listaColheitas)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR A COLHEITA")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR A COLHEITA"))

                if opcao == 1:
                    for i in range(len(listaColheitas)):
                        if listaColheitas[i].id_colheita == id_buscado:
                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try: 
                                # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                                cursor.execute("DELETE FROM colheita_voluntario WHERE id_colheita = :1", (listaColheitas[i].id_colheita,))
                                cursor.connection.commit()

                                cursor.execute("DELETE FROM plantio_colheita WHERE id_colheita = :1", (listaColheitas[i].id_colheita,))
                                cursor.connection.commit()

                                cursor.execute("DELETE FROM colheita WHERE id_colheita = :1", (listaColheitas[i].id_colheita,))
                                cursor.connection.commit()

                                for voluntario in listaColheitas[i].voluntarios_colheita:
                                    voluntario.remover_colheita(listaColheitas[i])

                                for plantio in listaColheitas[i].plantios_colheita:
                                    plantio.colheita = None

                                del listaColheitas[i]

                                print("COLHEITA EXCLUÍDA COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A EXCLUSÃO DA COLHEITA:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DA COLHEITA A SER EXCLUÍDA:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DA COLHEITA:")
                print(str(e))
