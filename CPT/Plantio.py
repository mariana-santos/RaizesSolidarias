import sqlite3

from datetime import datetime

from Alimento import Alimento
from Colheita import Colheita
from Funcoes import Funcoes

class Plantio:
    def __init__(self, id_plantio: int = None, data_plantio: str = None, espaco_plantio: int = None, alimento: Alimento = None, colheita: Colheita = None, voluntarios_plantio: list = None):
        self._id_plantio = id_plantio
        self._data_plantio = data_plantio
        self._espaco_plantio = espaco_plantio
        self._alimento = alimento
        self._colheita = colheita
        self._voluntarios_plantio = voluntarios_plantio if voluntarios_plantio is not None else []

    @property
    def id_plantio(self) -> int:
        return self._id_plantio

    @id_plantio.setter
    def id_plantio(self, id_plantio: int):
        self._id_plantio = id_plantio

    @property
    def data_plantio(self) -> str:
        return self._data_plantio

    @data_plantio.setter
    def data_plantio(self, data_plantio: str):
        self._data_plantio = data_plantio

    @property
    def espaco_plantio(self) -> int:
        return self._espaco_plantio

    @espaco_plantio.setter
    def espaco_plantio(self, espaco_plantio: int):
        self._espaco_plantio = espaco_plantio

    @property
    def alimento(self) -> Alimento:
        return self._alimento

    @alimento.setter
    def alimento(self, alimento: Alimento):
        self._alimento = alimento

    @property
    def colheita(self) -> Colheita:
        return self._colheita

    @colheita.setter
    def colheita(self, colheita: Colheita):
        self._colheita = colheita

    @property
    def voluntarios_plantio(self):
        return self._voluntarios_plantio

    @voluntarios_plantio.setter
    def voluntarios_plantio(self, voluntarios_plantio: list):
        self._voluntarios_plantio = voluntarios_plantio

    def perfilPlantio(plantio_buscado):
        retornoPerfil = Funcoes.menuCabecalho()
        retornoPerfil += f"01. ID: {plantio_buscado.id_plantio}\n"
        retornoPerfil += f"02. DATA: {plantio_buscado.data_plantio}\n"
        retornoPerfil += f"03. ESPAÇO: {plantio_buscado.espaco_plantio}\n"
        retornoPerfil += f"04. ALIMENTO: {plantio_buscado.alimento}"
        if (plantio_buscado.colheita == None):
            retornoPerfil += f"05. COLHEITA: A COLHEITA AINDA NÃO FOI REALIZADA."
        else:
            retornoPerfil += f"05. COLHEITA: {plantio_buscado.colheita}"
        retornoPerfil += "06. VOLUNTÁRIOS: "
        if len(plantio_buscado.voluntarios_plantio) == 0:
            retornoPerfil += "NENHUM VOLUNTÁRIO RESPONSÁVEL.\n"
        else:
            for i, voluntario in enumerate(plantio_buscado.voluntarios_plantio):
                voluntario_numero = f"{i+1:02d}"
                if i == 0:
                    retornoPerfil += f"\n 06.{voluntario_numero}. ID: {voluntario.id_usuario} | NOME: {voluntario.nome_usuario}\n"
                else:
                    retornoPerfil += f" 06.{voluntario_numero}. ID: {voluntario.id_usuario} | NOME: {voluntario.nome_usuario}\n"
        retornoPerfil += "07. SAIR\n"
        retornoPerfil += Funcoes.menuRodape()
        return retornoPerfil
    
    def cadastrarPlantio(dsn, id_plantio, listaPlantios, listaAlimentos, listaVoluntarios):
        # INSTANCIANDO NOVO PLANTIO
        novo_plantio = Plantio()

        Funcoes.menuCabecalho

        # SETANDO O ID DO NOVO PLANTIO
        id_plantio = id_plantio

        # SETANDO A DATA DO NOVO PLANTIO
        try:
            data_plantio = input(f"DIGITE A DATA DO PLANTIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            data_plantio = Funcoes.validarPreenchimento(f"DIGITE A DATA DO PLANTIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", data_plantio)
            data_formatada = datetime.strptime(data_plantio, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%Y-%m-%d")

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA DATA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA DATA DO PLANTIO:")
            print(str(e))
    
        # SETANDO O ESPAÇO DO NOVO PLANTIO
        try:
            espaco_plantio = int(input(f"DIGITE O ESPAÇO DO PLANTIO: "))
            espaco_plantio = int(Funcoes.validarPreenchimento(f"DIGITE O ESPAÇO DO PLANTIO: ", espaco_plantio))

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ESPAÇO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO ESPAÇO DO PLANTIO:")
            print(str(e))

        # SETANDO O ALIMENTO DO NOVO PLANTIO
        try:
            if (len(listaAlimentos) == 0):
                input("NENHUM ALIMENTO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                Funcoes.exibirAlimentosAdmin(listaAlimentos)
                id_buscado = int(input("DIGITE O ID DO ALIMENTO QUE DESEJA INCLUIR AO PLANTIO: \n"))
                alimento_buscado = Funcoes.buscarAlimentoPorId(id_buscado, listaAlimentos)
                alimento_buscado = Funcoes.validarAlimentoBuscado(alimento_buscado, listaAlimentos)
                
                alimento_plantio = Alimento()
                alimento_plantio.id_alimento = alimento_buscado.id_alimento
                alimento_plantio.nome_alimento = alimento_buscado.nome_alimento
                alimento_plantio.tempo_colheita = alimento_buscado.tempo_colheita
                alimento_plantio.qtd_irrigacao = alimento_buscado.qtd_irrigacao
                alimento_plantio.preco_alimento = alimento_buscado.preco_alimento
                alimento_plantio.qtd_alimento = alimento_buscado.qtd_alimento
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO ALIMENTO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO ALIMENTO DO PLANTIO:")
            print(str(e))
        
        # SETANDO A COLHEITA DO NOVO PLANTIO
        colheita_plantio = None    

        # SETANDO OS VOLUNTÁRIOS DO NOVO PLANTIO
        try:
            voluntarios_plantio = []

            if (len(listaVoluntarios) == 0):
                input("NENHUM VOLUNTÁRIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirUsuariosAdmin(listaVoluntarios)
                    id_buscado = int(input("DIGITE O ID DO VOLUNTÁRIO QUE DESEJA INCLUIR AO PLANTIO: \n"))
                    voluntario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaVoluntarios)
                    voluntario_buscado = Funcoes.validarUsuarioBuscado(voluntario_buscado, listaVoluntarios)
                    
                    voluntarios_plantio.append(voluntario_buscado)

                    opcao = int(input("DESEJA ADICIONAR MAIS UM VOLUNTÁRIO AO NOVO PLANTIO?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UM VOLUNTÁRIO AO NOVO PLANTIO?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO VOLUNTÁRIO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO VOLUNTÁRIO DO PLANTIO:")
            print(str(e))    

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = Funcoes.connect(dsn)
        cursor = conn.cursor()

        try:           
            # FAZENDO INSERT NO BANCO DE DADOS
            cursor.execute("INSERT INTO plantio (id_plantio, data_plantio, espaco_plantio, id_alimento) VALUES (:1, :2, :3, :4)", (id_plantio, data_formatada_banco, espaco_plantio, alimento_plantio.id_alimento))
            cursor.connection.commit()

            if len(voluntarios_plantio) != 0:
                for voluntario_plantio in voluntarios_plantio:
                    cursor.execute("INSERT INTO plantio_voluntario (id_plantio, id_usuario) VALUES (:1, :2)", (id_plantio, voluntario_plantio.id_usuario))
                    cursor.connection.commit()

            # FAZENDO INSERT NO CONSOLE
            novo_plantio.id_plantio = id_plantio
            novo_plantio.data_plantio = data_formatada
            novo_plantio.espaco_plantio = espaco_plantio
            novo_plantio.alimento = alimento_plantio
            novo_plantio.colheita = colheita_plantio
            novo_plantio.voluntarios_plantio = voluntarios_plantio

            listaPlantios.append(novo_plantio)

            for voluntario in voluntarios_plantio:
                voluntario.adicionar_voluntario(novo_plantio)

            id_plantio = id_plantio + 1

            print("PLANTIO CADASTRADO COM SUCESSO!")

        except sqlite3.DatabaseError as db_error:
            print("ERRO NO BANCO DE DADOS DURANTE O CADASTRO DO PLANTIO:")
            print(str(db_error))

        finally:
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

    def editarPlantio(dsn, listaPlantios):
        perfilPlantio = True

        if (len(listaPlantios) == 0):
            input("NENHUM PLANTIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

        else:
            Funcoes.exibirPlantiosAdmin(listaPlantios)
            id_buscado = int(input("DIGITE O ID DO PLANTIO QUE DESEJA EDITAR: \n"))
            plantio_buscado = Funcoes.buscarPlantioPorId(id_buscado, listaPlantios)
            plantio_buscado = Funcoes.validarPlantioBuscado(plantio_buscado, listaPlantios)

            while (perfilPlantio):
                opcao = int(input(Plantio.perfilPlantio(plantio_buscado)))
                opcao = int(Funcoes.validarOpcao(opcao, 1, 7, Plantio.perfilPlantio(plantio_buscado)))

                if (opcao == 1):
                    # EDITAR O ID DO PLANTIO
                    input(Funcoes.editarNegativo())
                
                elif (opcao == 2):
                    # EDITAR A DATA DO PLANTIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A DATA DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A DATA DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    
                    if (opcao == 1):
                       # EDITAR A DATA DO PLANTIO - SIM
                       Plantio.editarData(dsn, plantio_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A DATA DO PLANTIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 3):
                    # EDITAR O ESPAÇO DO PLANTIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O ESPAÇO DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O ESPAÇO DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    
                    if (opcao == 1):
                       # EDITAR O ESPAÇO DO PLANTIO - SIM
                       Plantio.editarEspaco(dsn, plantio_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O ESPAÇO DO PLANTIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 4):
                    # EDITAR O ALIMENTO DO PLANTIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR O ALIMENTO DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR O ALIMENTO DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    
                    if (opcao == 1):
                       # EDITAR O ALIMENTO DO PLANTIO - SIM
                       Plantio.editarAlimento(dsn, plantio_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR O ALIMENTO DO PLANTIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 5):
                    # EDITAR A COLHEITA DO PLANTIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR A COLHEITA DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR A COLHEITA DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    
                    if (opcao == 1):
                       # EDITAR A COLHEITA DO PLANTIO - SIM
                       Plantio.editarColheita(dsn, plantio_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR A COLHEITA DO PLANTIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")

                elif (opcao == 6):
                    # EDITAR OS VOLUNTÁRIOS DO PLANTIO
                    opcao = int(input(Funcoes.confirmarAcao(f"EDITAR OS VOLUNTÁRIOS DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EDITAR OS VOLUNTÁRIOS DO PLANTIO DE ID {plantio_buscado.id_plantio}")))
                    
                    if (opcao == 1):
                       # EDITAR OS VOLUNTÁRIOS DO PLANTIO - SIM
                       Plantio.editarVoluntarios(dsn, plantio_buscado)
                    
                    elif (opcao == 2):
                        # EDITAR OS VOLUNTÁRIOS DO PLANTIO - NÃO
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                
                elif (opcao == 7):
                    perfilPlantio = False

    def editarData(dsn, plantio_buscado):
        try:
            nova_data = input(f"DIGITE A NOVA DATA DO PLANTIO DE ID {plantio_buscado.id_plantio} (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
            nova_data = Funcoes.validarPreenchimento(f"DIGITE A NOVA DATA DO PLANTIO DE ID {plantio_buscado.id_plantio} (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", nova_data)
            data_formatada = datetime.strptime(nova_data, "%d/%m/%Y").date()
            data_formatada_banco = data_formatada.strftime("%Y-%m-%d")

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE plantio SET data_plantio = :data_formatada_banco WHERE id_plantio = :id_plantio", {"data_formatada_banco": data_formatada_banco, "id_plantio": plantio_buscado.id_plantio})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                plantio_buscado.data_plantio = data_formatada

                print("DATA DO PLANTIO EDITADA COM SUCESSO!")

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
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DA DATA DO PLANTIO:")
            print(str(e))
    
    def editarEspaco(dsn, plantio_buscado):
        try:
            novo_espaco = int(input(f"DIGITE O NOVO ESPAÇO DO PLANTIO DE ID {plantio_buscado.id_plantio}: "))
            novo_espaco = int(Funcoes.validarPreenchimento(f"DIGITE O NOVO ESPAÇO DO PLANTIO DE ID {plantio_buscado.id_plantio}: ", novo_espaco))

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("UPDATE plantio SET espaco_plantio = :novo_espaco WHERE id_plantio = :id_plantio", {"novo_espaco": novo_espaco, "id_plantio": plantio_buscado.id_plantio})
                cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                plantio_buscado.espaco_plantio = novo_espaco

                print("ESPAÇO DO PLANTIO EDITADO COM SUCESSO!")

            except sqlite3.DatabaseError as db_error:
                print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO ESPAÇO:")
                print(str(db_error))

            finally:
                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                Funcoes.disconnect(conn, cursor)

        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO ESPAÇO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A ATUALIZAÇÃO DO ESPAÇO DO PLANTIO:")
            print(str(e))

    def editarAlimento(dsn, plantio_buscado, listaAlimentos):
        try:
            if (len(listaAlimentos) == 0):
                input("NENHUM ALIMENTO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                Funcoes.exibirAlimentosAdmin(listaAlimentos)
                id_buscado = int(input("DIGITE O ID DO ALIMENTO QUE DESEJA INCLUIR AO PLANTIO: \n"))
                alimento_buscado = Funcoes.buscarAlimentoPorId(id_buscado, listaAlimentos)
                alimento_buscado = Funcoes.validarAlimentoBuscado(alimento_buscado, listaAlimentos)
                
                novo_alimento = Alimento()
                novo_alimento.id_alimento = alimento_buscado.id_alimento
                novo_alimento.nome_alimento = alimento_buscado.nome_alimento
                novo_alimento.tempo_colheita = alimento_buscado.tempo_colheita
                novo_alimento.qtd_irrigacao = alimento_buscado.qtd_irrigacao
                novo_alimento.preco_alimento = alimento_buscado.preco_alimento
                novo_alimento.qtd_alimento = alimento_buscado.qtd_alimento

                # CRIANDO CONEXÃO COM O BANCO DE DADOS
                conn = Funcoes.connect(dsn)
                cursor = conn.cursor()

                try:           
                    # FAZENDO UPDATE NO BANCO DE DADOS
                    cursor.execute("UPDATE plantio SET id_alimento = :novo_alimento.id_alimento WHERE id_plantio = :id_plantio", {"novo_alimento.id_alimento": novo_alimento.id_alimento, "id_plantio": plantio_buscado.id_plantio})
                    cursor.connection.commit()

                    # FAZENDO UPDATE NO CONSOLE
                    plantio_buscado.alimento = novo_alimento

                    print("ALIMENTO DO PLANTIO EDITADO COM SUCESSO!")

                except sqlite3.DatabaseError as db_error:
                    print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DO ALIMENTO:")
                    print(str(db_error))

                finally:
                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO NOVO ALIMENTO:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO ALIMENTO DO PLANTIO:")
            print(str(e))

    def editarColheita(dsn, plantio_buscado, listaColheitas):
        try:
            if (len(listaColheitas) == 0):
                input("NENHUMA COLHEITA CADASTRADA. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                Funcoes.exibirColheitasAdmin(listaColheitas)
                id_buscado = int(input("DIGITE O ID DA COLHEITA QUE DESEJA INCLUIR AO PLANTIO: \n"))
                colheita_buscada = Funcoes.buscarColheitaPorId(id_buscado, listaColheitas)
                colheita_buscada = Funcoes.validarColheitaBuscada(colheita_buscada, listaColheitas)
                
                nova_colheita = Colheita()
                nova_colheita.id_colheita = colheita_buscada.id_colheita
                nova_colheita.data_colheita = colheita_buscada.data_colheita
                nova_colheita.descricao_colheita = colheita_buscada.descricao_colheita
                nova_colheita.voluntarios_colheita = colheita_buscada.voluntarios_colheita
                nova_colheita.plantios_colheita = colheita_buscada.plantios_colheita

                # CRIANDO CONEXÃO COM O BANCO DE DADOS
                conn = Funcoes.connect(dsn)
                cursor = conn.cursor()

                try:           
                    # FAZENDO UPDATE NO BANCO DE DADOS
                    cursor.execute("DELETE FROM plantio_colheita WHERE id_plantio = :id_plantio AND id_colheita = :id_colheita", {"id_plantio": plantio_buscado.id_plantio, "id_colheita": plantio_buscado.colheita.id_colheita})
                    cursor.connection.commit()

                    cursor.execute("INSERT INTO plantio_colheita (id_plantio, id_colheita) VALUES (:1, :2)", (plantio_buscado.id_plantio, nova_colheita.id_colheita))
                    cursor.connection.commit()

                    # FAZENDO UPDATE NO CONSOLE
                    if plantio_buscado.colheita is not None:
                        for colheita_buscada in listaColheitas:
                            colheita_buscada.remover_plantio(plantio_buscado)

                    plantio_buscado.colheita = nova_colheita

                    if plantio_buscado.colheita is not None:
                        nova_colheita.adicionar_plantio(plantio_buscado)

                    print("COLHEITA DO PLANTIO EDITADO COM SUCESSO!")

                except sqlite3.DatabaseError as db_error:
                    print("ERRO NO BANCO DE DADOS DURANTE A ATUALIZAÇÃO DA COLHEITA:")
                    print(str(db_error))

                finally:
                    # FECHANDO CONEXÃO COM O BANCO DE DADOS
                    Funcoes.disconnect(conn, cursor)
        
        except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA NOVA COLHEITA:")
            print(str(value_error))

        except Exception as e:
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DA COLHEITA DO PLANTIO:")
            print(str(e))

    def editarVoluntarios(dsn, plantio_buscado, listaVoluntarios):
        try:
            novos_voluntarios_plantio = []

            if (len(listaVoluntarios) == 0):
                input("NENHUM VOLUNTÁRIO CADASTRADO. TECLE ENTER PARA VOLTAR AO MENU\n")

            else:
                adicionar = True

                while (adicionar):
                    Funcoes.exibirUsuariosAdmin(listaVoluntarios)
                    id_buscado = int(input("DIGITE O ID DO VOLUNTÁRIO QUE DESEJA INCLUIR AO PLANTIO: \n"))
                    voluntario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, listaVoluntarios)
                    voluntario_buscado = Funcoes.validarUsuarioBuscado(voluntario_buscado, listaVoluntarios)
                    
                    novos_voluntarios_plantio.append(voluntario_buscado)

                    opcao = int(input("DESEJA ADICIONAR MAIS UM VOLUNTÁRIO AO PLANTIO?\n" + 
                                          "01. SIM\n" + 
                                          "02. NÃO\n"))
                    
                    opcao = int(Funcoes.validarOpcao(opcao, 1, 2, "DESEJA ADICIONAR MAIS UM VOLUNTÁRIO AO PLANTIO?\n01. SIM\n02. NÃO\n"))

                    if (opcao == 1):
                        adicionar = True
                    
                    elif (opcao == 2):
                        adicionar = False

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            try:
                # FAZENDO UPDATE NO BANCO DE DADOS
                cursor.execute("DELETE FROM plantio_voluntario WHERE id_plantio = :id_plantio", {"id_plantio": plantio_buscado.id_plantio})
                cursor.connection.commit()
                
                for voluntario_plantio in novos_voluntarios_plantio:
                    cursor.execute("INSERT INTO plantio_voluntario (id_plantio, id_usuario) VALUES (:1, :2)", (plantio_buscado.id_plantio, voluntario_plantio.id_usuario))
                    cursor.connection.commit()

                # FAZENDO UPDATE NO CONSOLE
                for voluntario in plantio_buscado.voluntarios_plantio:
                    voluntario.remover_voluntario(plantio_buscado)

                voluntario_buscado.voluntarios_plantio = novos_voluntarios_plantio

                for voluntario in plantio_buscado.voluntarios_plantio:
                    voluntario.adicionar_voluntario(plantio_buscado)   

                print("VOLUNTÁRIOS DO PLANTIO EDITADOS COM SUCESSO!")

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
            print("OCORREU UM ERRO DURANTE A DIGITAÇÃO DO VOLUNTÁRIO DO PLANTIO:")
            print(str(e))

    def excluirPlantio(dsn, listaPlantios):
        
        if len(listaPlantios) == 0:
            print("NÃO EXISTEM PLANTIOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirPlantiosAdmin(listaPlantios)
            try:
                id_buscado = int(input("DIGITE O ID DO PLANTIO QUE DESEJA EXCLUIR: \n"))
                plantio_buscado = Funcoes.buscarPlantioPorId(id_buscado, listaPlantios)
                plantio_buscado = Funcoes.validarPlantioBuscado(plantio_buscado, listaPlantios)
                opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O PLANTIO")))
                opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O PLANTIO"))

                if opcao == 1:
                    for i in range(len(listaPlantios)):
                        if listaPlantios[i].id_plantio == id_buscado:
                            # CRIANDO CONEXÃO COM O BANCO DE DADOS
                            conn = Funcoes.connect(dsn)
                            cursor = conn.cursor()

                            try: 
                                # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                                cursor.execute("DELETE FROM plantio_voluntario WHERE id_plantio = :1", (listaPlantios[i].id_plantio,))
                                cursor.connection.commit()

                                cursor.execute("DELETE FROM plantio WHERE id_plantio = :1", (listaPlantios[i].id_plantio,))
                                cursor.connection.commit()

                                for voluntario in listaPlantios[i].voluntarios_plantio:
                                    voluntario.remover_voluntario(listaPlantios[i])

                                del listaPlantios[i]

                                print("PLANTIO EXCLUÍDO COM SUCESSO!")
                                input("TECLE ENTER PARA VOLTAR AO MENU.")
                                break
                            
                            except sqlite3.DatabaseError as db_error:
                                print("ERRO NO BANCO DE DADOS DURANTE A EXCLUSÃO DO PLANTIO:")
                                print(str(db_error))

                            finally:
                                # FECHANDO CONEXÃO COM O BANCO DE DADOS
                                Funcoes.disconnect(conn, cursor)

                elif opcao == 2:
                    input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            except ValueError as value_error:
                print("ERRO DE VALOR DURANTE A DIGITAÇÃO DO ID DO PLANTIO A SER EXCLUÍDO:")
                print(str(value_error))

            except Exception as e:
                print("OCORREU UM ERRO DURANTE A EXCLUSÃO DO PLANTIO:")
                print(str(e))
