import cx_Oracle

import time
from datetime import datetime
from tqdm import tqdm

from Receptor import Receptor

class Funcoes:

    # MENUS
    def menuCabecalho():
        return ("==> RAÍZES SOLIDÁRIAS - GLOBAL SOLUTIONS - 1TDSPR <==\n"
        "------------------------------------------\n")

    def menuRodape():
        return ("------------------------------------------\n"
        "DIGITE A OPÇÃO DESEJADA: \n")

    def menuInicial(): 
        return (Funcoes.menuCabecalho() + 
            "01. LOGIN ADMIN\n"
            "02. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdmin():
        return (Funcoes.menuCabecalho() +
            "01. AGENDAMENTOS\n"
            "02. ALIMENTOS\n"
            "03. COLHEITAS\n"
            "04. DESTINOS\n"
            "05. DOAÇÕES\n"
            "06. DOADORES\n"
            "07. PLANTIOS\n"
            "08. RECEPTORES\n"
            "09. VOLUNTÁRIOS\n"
            "10. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdminAgendamentos():
        return (Funcoes.menuCabecalho() +
            "01. CADASTRAR AGENDAMENTO\n"
            "02. EXIBIR AGENDAMENTOS\n"
            "03. EDITAR AGENDAMENTO\n"
            "04. EXCLUIR AGENDAMENTO\n"
            "05. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdminAlimentos():
        return (Funcoes.menuCabecalho() +
            "01. CADASTRAR ALIMENTO\n"
            "02. EXIBIR ALIMENTOS\n"
            "03. EDITAR ALIMENTO\n"
            "04. EXCLUIR ALIMENTO\n"
            "05. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdminColheitas():
        return (Funcoes.menuCabecalho() +
            "01. CADASTRAR COLHEITA\n"
            "02. EXIBIR COLHEITAS\n"
            "03. EDITAR COLHEITA\n"
            "04. EXCLUIR COLHEITA\n"
            "05. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdminDestinos():
        return (Funcoes.menuCabecalho() +
            "01. CADASTRAR DESTINO\n"
            "02. EXIBIR DESTINOS\n"
            "03. EDITAR DESTINO\n"
            "04. EXCLUIR DESTINO\n"
            "05. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdminDoacoes():
        return (Funcoes.menuCabecalho() +
            "01. CADASTRAR DOAÇÃO\n"
            "02. EXIBIR DOAÇÕES\n"
            "03. EDITAR DOAÇÃO\n"
            "04. EXCLUIR DOAÇÃO\n"
            "05. SAIR\n" +
            Funcoes.menuRodape())
    
    def menuAdminDoadores():
        return (Funcoes.menuCabecalho() +
            "01. CADASTRAR DOADOR\n"
            "02. EXIBIR DOADORES\n"
            "03. EDITAR DOADOR\n"
            "04. EXCLUIR DOADOR\n"
            "05. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdminPlantios():
        return (Funcoes.menuCabecalho() +
            "01. CADASTRAR PLANTIO\n"
            "02. EXIBIR PLANTIOS\n"
            "03. EDITAR PLANTIO\n"
            "04. EXCLUIR PLANTIO\n"
            "05. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdminReceptores():
        return (Funcoes.menuCabecalho() +
            "01. CADASTRAR RECEPTOR\n"
            "02. EXIBIR RECEPTORES\n"
            "03. EDITAR RECEPTOR\n"
            "04. EXCLUIR RECEPTOR\n"
            "05. SAIR\n" +
            Funcoes.menuRodape())

    def menuAdminVoluntarios():
        return (Funcoes.menuCabecalho() +
            "01. CADASTRAR VOLUNTÁRIO\n"
            "02. EXIBIR VOLUNTÁRIOS\n"
            "03. EDITAR VOLUNTÁRIO\n"
            "04. EXCLUIR VOLUNTÁRIO\n"
            "05. SAIR\n" +
            Funcoes.menuRodape())

    # CONFIRMAR
    def confirmarAcao(acao):
        return ("TEM CERTEZA QUE DESEJA " + acao + "?\n"
        "01. SIM\n"
        "02. NÃO\n"
        "------------------------------------------\n"
        "DIGITE A OPÇÃO DESEJADA: \n")
    
    # VALIDAR
    def validarCPF(cpf_usuario):
        if (cpf_usuario == "00000000000" or cpf_usuario == "11111111111" or cpf_usuario == "22222222222" or cpf_usuario == "33333333333" or cpf_usuario == "44444444444" or cpf_usuario == "55555555555" or cpf_usuario == "66666666666" or cpf_usuario == "77777777777" or cpf_usuario == "88888888888" or cpf_usuario == "99999999999" or (len(cpf_usuario) != 11)):
            return False

        dig10, dig11 = '', ''
        sm, r, peso = 0, 0, 0
        for i in range(9):
            num = int(cpf_usuario[i])
            sm += num * (10 - i)
        r = 11 - sm % 11
        if (r == 10 or r == 11):
            dig10 = '0'
        else:
            dig10 = str(r)

        sm = 0
        peso = 11
        for i in range(10):
            num = int(cpf_usuario[i])
            sm += num * peso
            peso -= 1
        r = 11 - sm % 11
        if (r == 10 or r == 11):
            dig11 = '0'
        else:
            dig11 = str(r)

        if (dig10 == cpf_usuario[9] and dig11 == cpf_usuario[10]):
            return True
        else:
            return False
    
    def validarOpcao(opcao, opcao_min, opcao_max, menu):
        while opcao is None or opcao < opcao_min or opcao > opcao_max:
            print("OPÇÃO INVÁLIDA! DIGITE UM NÚMERO ENTRE {} E {}.".format(opcao_min, opcao_max))
            input("TECLE ENTER PARA VOLTAR AO MENU.")
            try:
                opcao = int(input(menu))
            except ValueError:
                print("ERRO: DIGITE UM NÚMERO INTEIRO VÁLIDO!")
        return opcao

    def validarPreenchimento(stringRepeticao, campopreenchido) -> str:
        while (len(str(campopreenchido)) == 0) or (str(campopreenchido) == "") or (str(campopreenchido) == None) or (str(campopreenchido) == "\r"):
            print("O PREENCHIMENTO DO CAMPO É OBRIGATÓRIO.")
            campopreenchido = input(stringRepeticao)
            
        return str(campopreenchido) if isinstance(campopreenchido, str) else campopreenchido

    def validarSenha(senha_usuario, conf_senha):
        while ((senha_usuario != conf_senha) or (len(senha_usuario) == 0) or (senha_usuario == "") or (senha_usuario == None) or (senha_usuario == "\r")):
            input("SENHAS NÃO CONFEREM OU SENHA INVÁLIDA. TECLE ENTER PARA CADASTRAR NOVA SENHA")
            senha_usuario = input("DIGITE A SUA SENHA: ")
            conf_senha = input("CONFIRME A SUA SENHA: ")
        return senha_usuario

    def validarCel(cel_usuario):
        while (len(cel_usuario) != 11):
            print("CELULAR INVÁLIDO OU JÁ CADASTRADO.")
            cel_usuario = input("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
        
        return cel_usuario

    def validarAgendamentoBuscado(agendamento_buscado, lista):
        while agendamento_buscado is None:
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirAgendamentosAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO AGENDAMENTO NOVAMENTE: \n"))
            agendamento_buscado = Funcoes.buscarPorIdAgendamento(id_buscado, lista)
        
        return agendamento_buscado

    def validarAlimentoBuscado(alimento_buscado, lista):
        while alimento_buscado is None:
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirAlimentosAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO ALIMENTO NOVAMENTE: \n"))
            alimento_buscado = Funcoes.buscarPorIdAlimento(id_buscado, lista)
        
        return alimento_buscado

    def validarColheitaBuscada(colheita_buscada, lista):
        while colheita_buscada is None:
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirColheitasAdmin(lista)
            id_buscado = int(input("DIGITE O ID DA COLHEITA NOVAMENTE: \n"))
            colheita_buscada = Funcoes.buscarPorIdColheita(id_buscado, lista)
        
        return colheita_buscada

    def validarDestinoBuscado(destino_buscado, lista):
        while destino_buscado is None:
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirDestinosAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO DESTINO NOVAMENTE: \n"))
            destino_buscado = Funcoes.buscarPorIdDestino(id_buscado, lista)
        
        return destino_buscado

    def validarDoacaoBuscada(doacao_buscada, lista):
        while doacao_buscada is None:
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirDoacoesAdmin(lista)
            id_buscado = int(input("DIGITE O ID DA DOAÇÃO NOVAMENTE: \n"))
            doacao_buscada = Funcoes.buscarPorIdDoacao(id_buscado, lista)
        
        return doacao_buscada

    def validarDoadorBuscado(doador_buscado, lista):
        while doador_buscado is None:
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirDoadoresAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO DOADOR NOVAMENTE: \n"))
            doador_buscado = Funcoes.buscarPorIdDoador(id_buscado, lista)
        
        return doador_buscado

    def validarPlantioBuscado(plantio_buscado, lista):
        while plantio_buscado is None:
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirPlantiosAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO PLANTIO NOVAMENTE: \n"))
            plantio_buscado = Funcoes.buscarPorIdPlantio(id_buscado, lista)
        
        return plantio_buscado

    def validarReceptorBuscado(receptor_buscado, lista):
        while receptor_buscado is None:
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirReceptoresAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO RECEPTOR NOVAMENTE: \n"))
            receptor_buscado = Funcoes.buscarPorIdReceptor(id_buscado, lista)
        
        return receptor_buscado
    
    def validarUsuarioBuscado(usuario_buscado, lista):
        while (usuario_buscado == None):
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirUsuariosAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO USUÁRIO NOVAMENTE: \n"))
            usuario_buscado = Funcoes.buscarUsuarioPorId(id_buscado, lista)
        
        return usuario_buscado

    def validarVoluntarioBuscado(voluntario_buscado, lista):
        while voluntario_buscado is None:
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirVoluntariosAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO VOLUNTÁRIO NOVAMENTE: \n"))
            voluntario_buscado = Funcoes.buscarPorIdVoluntario(id_buscado, lista)
        
        return voluntario_buscado

    # VERIFICAR
    def verificarCPF(cpf_usuario, cpfs_cadastrados):
        while (cpf_usuario in cpfs_cadastrados or Funcoes.validarCPF(cpf_usuario) == False):
            print("CPF INVÁLIDO OU JÁ CADASTRADO.")
            cpf_usuario = input("DIGITE O SEU CPF (APENAS NÚMEROS, EXEMPLO: 43102154278): ")
        
        return cpf_usuario

    def verificarEmail(email_usuario, emails_cadastrados):
        while (email_usuario in emails_cadastrados or email_usuario == ""):
            print("EMAIL INVÁLIDO OU JÁ CADASTRADO.")
            email_usuario = input("DIGITE O SEU EMAIL: ")
        
        return email_usuario

    def verificarCel(cel_usuario, cel_cadastrados):
        while (cel_usuario in cel_cadastrados or cel_usuario == "" or len(cel_usuario) != 11):
            print("CELULAR INVÁLIDO OU JÁ CADASTRADO.")
            cel_usuario = input("DIGITE O SEU CELULAR (SOMENTE NÚMEROS, COM DDD, EXEMPLO: 11983050165): ")
        
        return cel_usuario

    # FORMATAR
    def formatarCpf(cpf_usuario):
        cpf_usuario_formatado = '{}.{}.{}-{}'.format(cpf_usuario[:3], cpf_usuario[3:6], cpf_usuario[6:9], cpf_usuario[9:])
        return cpf_usuario_formatado

    def formatarCel(cel_usuario):
        cel_usuario_formatado = '({}) {}-{}'.format(cel_usuario[:2], cel_usuario[2:7], cel_usuario[7:11])
        return cel_usuario_formatado

    def formatarData(data):
        if isinstance(data, str):
            data = datetime.strptime(data, "%d/%m/%Y")
        data_formatada = data.strftime("%d/%m/%Y")
        return data_formatada

    # BUSCAR
    def buscarAgendamentoPorId(id_buscado, lista):
        agendamento_buscado = lista.get(id_buscado)
        if agendamento_buscado is None:
            return None
        return agendamento_buscado
    
    def buscarAlimentoPorId(id_buscado, lista):
        alimento_buscado = lista.get(id_buscado)
        if alimento_buscado is None:
            return None
        return alimento_buscado

    def buscarColheitaPorId(id_buscado, lista):
        colheita_buscada = lista.get(id_buscado)
        if colheita_buscada is None:
            return None
        return colheita_buscada

    def buscarDestinoPorId(id_buscado, lista):
        destino_buscado = lista.get(id_buscado)
        if destino_buscado is None:
            return None
        return destino_buscado

    def buscarDoacaoPorId(id_buscado, lista):
        doacao_buscada = lista.get(id_buscado)
        if doacao_buscada is None:
            return None
        return doacao_buscada

    def buscarPlantioPorId(id_buscado, lista):
        plantio_buscado = lista.get(id_buscado)
        if plantio_buscado is None:
            return None
        return plantio_buscado
    
    def buscarUsuarioPorId(id_buscado, lista):
        objeto_buscado = lista.get(id_buscado)
        if objeto_buscado is None:
            return None
        return objeto_buscado

    # EDITAR
    def editarNegativo():
        return("NÃO É POSSÍVEL EDITAR ESTA OPÇÃO.\n"
            "TECLE ENTER PARA VOLTAR AO MENU")
    
    # EXIBIR
    def exibirAgendamentosAdmin(listaAgendamentos):
        Funcoes.menuCabecalho()

        if len(listaAgendamentos) == 0:
            print("NÃO EXISTEM AGENDAMENTOS CADASTRADOS.")
        else:
            for agendamento in listaAgendamentos:
                print(f"ID: {agendamento.id_agendamento} | USUÁRIO DO AGENDAMENTO: {agendamento.usuario}")
                print(f"------------------------------------------")

    def exibirAlimentosAdmin(listaAlimentos):
        Funcoes.menuCabecalho()

        if len(listaAlimentos) == 0:
            print("NÃO EXISTEM ALIMENTOS CADASTRADOS.")
        else:
            for alimento in listaAlimentos:
                print(f"ID: {alimento.id_alimento} | NOME DO ALIMENTO: {alimento.nome_alimento}")
                print(f"------------------------------------------")

    def exibirColheitasAdmin(listaColheitas):
        Funcoes.menuCabecalho()

        if len(listaColheitas) == 0:
            print("NÃO EXISTEM COLHEITAS CADASTRADAS.")
        else:
            for colheita in listaColheitas:
                print(f"ID: {colheita.id_colheita} | DATA DA COLHEITA: {colheita.data_colheita}")
                print(f"------------------------------------------")

    def exibirDestinosAdmin(listaDestinos):
        Funcoes.menuCabecalho()

        if len(listaDestinos) == 0:
            print("NÃO EXISTEM DESTINOS CADASTRADOS.")
        else:
            for destino in listaDestinos:
                print(f"ID: {destino.id_destino} | ENDEREÇO DO DESTINO: {destino.endereco_destino}")
                print(f"------------------------------------------")

    def exibirDoacoesAdmin(listaDoacoes):
        Funcoes.menuCabecalho()

        if len(listaDoacoes) == 0:
            print("NÃO EXISTEM DOAÇÕES CADASTRADAS.")
        else:
            for doacao in listaDoacoes:
                print(f"ID: {doacao.id_doacao} | DOADOR: {doacao.doador.nome}")
                print(f"------------------------------------------")

    def exibirPlantiosAdmin(listaPlantios):
        Funcoes.menuCabecalho()

        if len(listaPlantios) == 0:
            print("NÃO EXISTEM PLANTIOS CADASTRADOS.")
        else:
            for plantio in listaPlantios:
                print(f"ID: {plantio.id_plantio} | DATA DO PLANTIO: {plantio.data_plantio}")
                print(f"------------------------------------------")

    def exibirUsuariosAdmin(lista):
        Funcoes.menuCabecalho()

        if len(lista) == 0:
            print("NÃO EXISTEM USUÁRIOS CADASTRADOS.")
        else:
            for usuario in lista:
                print(f"ID: {usuario.id_usuario} | NOME: {usuario.nome_usuario}")
                print(f"------------------------------------------")

    # BANCO DE DADOS
    def connect(dsn):
        try:
            conn = Funcoes.connect(dsn)
            return conn
        except cx_Oracle.Error as e:
            print(f"ERRO AO CONECTAR COM O BANCO DE DADOS: {e}")

    def disconnect(conn, cursor):
        try:
            if not conn.close:
                conn.close()
            if not cursor.close:
                cursor.close()
        except cx_Oracle.Error as e:
            print(f"ERRO AO DESCONECTAR DO BANCO DE DADOS: {e}")

    def buscarIdMax(dsn, coluna_tabela, nome_tabela):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            cursor.execute(f"SELECT MAX({coluna_tabela}) FROM {nome_tabela}")
            result = cursor.fetchone()
            if result[0] is None:
                id_max = 1
            else:
                id_max = result[0] + 1
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)
            return id_max
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarCpfsCadastrados(dsn):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            cpfs_cadastrados = set()
            cursor.execute("SELECT cpf_usuario FROM usuario")
            results = cursor.fetchall()
            for row in results:
                cpfs_cadastrados.add(row[0])

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)
            return cpfs_cadastrados
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None

    def buscarEmailsCadastrados(dsn):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()
            
            emails_cadastrados = set()
            cursor.execute("SELECT email_usuario FROM usuario")
            results = cursor.fetchall()
            for row in results:
                emails_cadastrados.add(row[0])
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)
            return emails_cadastrados
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None
    
    def buscarAgendamentosBanco(dsn, Agendamento):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            listaAgendamentos = []
            cursor.execute("""
                SELECT * FROM agendamento ORDER BY id_agendamento
            """)

            for row in cursor:
                agendamento_banco = Agendamento(
                    id_agendamento = row[0],
                    data_agendamento = row[1],
                    turno_agendamento = row[2],
                    usuario = row[3]
                )

                listaAgendamentos.append(agendamento_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaAgendamentos)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE AGENDAMENTOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaAgendamentos
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS AGENDAMENTOS NO BANCO DE DADOS: {str(e)}")
            return None

    def buscarAlimentosBanco(dsn, Alimento):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            listaAlimentos = []
            cursor.execute("""
                SELECT * FROM alimento ORDER BY id_alimento
            """)

            for row in cursor:
                alimento_banco = Alimento(
                    id_alimento = row[0],
                    nome_alimento = row[1],
                    tempo_colheita = row[2],
                    qtd_irrigacao = row[3],
                    preco_alimento = row[4],
                    qtd_alimento = row[5]
                )

                listaAlimentos.append(alimento_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaAlimentos)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE ALIMENTOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaAlimentos
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS ALIMENTOS NO BANCO DE DADOS: {str(e)}")
            return None
        
    def buscarColheitasBanco(dsn, Colheita):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            listaColheitas = []
            cursor.execute("""
                SELECT * FROM colheita ORDER BY id_colheita
            """)

            for row in cursor:
                colheita_banco = Colheita(
                    id_colheita = row[0],
                    data_colheita = row[1],
                    descricao_colheita = row[2]
                )

                listaColheitas.append(colheita_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaColheitas)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE COLHEITAS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaColheitas
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR AS COLHEITAS NO BANCO DE DADOS: {str(e)}")
            return None

    # PAREI AQUI!

    def buscarDestinosBanco(dsn, Destino):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor_destino = conn.cursor()

            listaDestinos = []
            cursor_destino.execute("""
                SELECT * FROM destino ORDER BY id_destino
            """)

            for destino_row in cursor_destino:
                destino_banco = Destino(
                    id_destino = destino_row[0],
                    endereco_destino = destino_row[1],
                    responsavel_destino = destino_row[2],
                    cel_destino = destino_row[3],
                    qtd_dependentes_destino = destino_row[4],
                    receptores_destino = []
                )

                cursor_receptor = conn.cursor()
                cursor_receptor.execute("""
                    SELECT rd.id_usuario, 
                    u.cpf_usuario, u.nome_usuario, u.email_usuario, u.cel_usuario, u.senha_usuario, u.status_usuario, 
                    r.carga_receptor, r.endereco_receptor 
                    FROM Receptor_Destino rd 
                    JOIN Receptor r ON rd.id_usuario = r.id_usuario 
                    JOIN Usuario u ON rd.id_usuario = u.id_usuario 
                    JOIN Destino d ON rd.id_destino = d.id_destino 
                    WHERE rd.id_destino = :id_destino 
                    ORDER BY rd.id_usuario
                """, {"id_destino": destino_banco.id_destino})

                for receptor_row in cursor_receptor:
                    receptor_destino_banco = Receptor(
                        id_usuario = receptor_row[0],
                        cpf_usuario = receptor_row[1],
                        nome_usuario = receptor_row[2],
                        email_usuario = receptor_row[3],
                        senha_usuario = receptor_row[4],
                        status_usuario = receptor_row[5],
                        carga_receptor = receptor_row[6],
                        endereco_receptor = receptor_row[7]
                    )
                    autor_banco.livros.append(livro)

                cursor_livro.close()
                lista_autores.append(autor_banco)

                listaDestinos.append(destino_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaDestinos)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE DESTINOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor_destino)

            return listaDestinos
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS DESTINOS NO BANCO DE DADOS: {str(e)}")
            return None

    def buscarDoacoesBanco(dsn, Doacao):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            listaDoacoes = []
            cursor.execute("""
                SELECT * FROM doacao ORDER BY id_doacao
            """)

            for row in cursor:
                doacao_banco = Doacao(
                    id_doacao = row[0],
                    doador = row[1],
                    data_doacao = row[2],
                    qtd_moedas_doacao = row[3]
                )

                listaDoacoes.append(doacao_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaDoacoes)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE DOAÇÕES: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaDoacoes
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR AS DOAÇÕES NO BANCO DE DADOS: {str(e)}")
            return None
    
    def buscarDoadoresBanco(dsn, Doador):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            listaDoadores = []
            cursor.execute("""
                SELECT 
                    u.id_usuario, 
                    u.cpf_usuario, 
                    u.nome_usuario, 
                    u.email_usuario, 
                    u.senha_usuario,
                    u.status_usuario,
                    d.nivel_doador,
                    d.moedas_doador, 
                    FROM usuario u 
                    INNER JOIN doador a ON d.id_usuario = u.id_usuario
                    ORDER BY u.id_usuario
            """)

            for row in cursor:
                doador_banco = Doador(
                    id_usuario = row[0],
                    cpf_usuario = row[1],
                    nome_usuario = row[2],
                    email_usuario = row[3],
                    senha_usuario = row[4],
                    status_usuario = row[5],
                    nivel_doador = row[6],
                    moedas_doador = row[7]
                )

                listaDoadores.append(doador_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaDoadores)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE DOADORES: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaDoadores
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS DOADORES NO BANCO DE DADOS: {str(e)}")
            return None

    def buscarPlantiosBanco(dsn, Plantio):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            listaPlantios = []
            cursor.execute("""
                SELECT * FROM plantio ORDER BY id_plantio
            """)

            for row in cursor:
                plantio_banco = Plantio(
                    id_plantio = row[0],
                    data_plantio = row[1],
                    espaco_plantio = row[2],
                    alimento_plantio = row[3]
                )

                listaPlantios.append(plantio_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaPlantios)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE PLANTIOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaPlantios
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS PLANTIOS NO BANCO DE DADOS: {str(e)}")
            return None

    def buscarReceptoresBanco(dsn, Receptor):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            listaReceptores = []
            cursor.execute("""
                SELECT 
                    u.id_usuario, 
                    u.cpf_usuario, 
                    u.nome_usuario, 
                    u.email_usuario, 
                    u.senha_usuario,
                    u.status_usuario,
                    r.carga_receptor,
                    r.endereco_receptor, 
                    FROM usuario u 
                    INNER JOIN receptor r ON r.id_usuario = u.id_usuario
                    ORDER BY u.id_usuario
            """)

            for row in cursor:
                receptor_banco = Receptor(
                    id_usuario = row[0],
                    cpf_usuario = row[1],
                    nome_usuario = row[2],
                    email_usuario = row[3],
                    senha_usuario = row[4],
                    status_usuario = row[5],
                    carga_receptor = row[6],
                    endereco_receptor = row[7]
                )

                listaReceptores.append(receptor_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaReceptores)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE RECEPTORES: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaReceptores
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS RECEPTORES NO BANCO DE DADOS: {str(e)}")
            return None
        
    def buscarVoluntariosBanco(dsn, Voluntario):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            listaVoluntarios = []
            cursor.execute("""
                SELECT 
                    u.id_usuario, 
                    u.cpf_usuario, 
                    u.nome_usuario, 
                    u.email_usuario, 
                    u.senha_usuario,
                    u.status_usuario,
                    v.data_registro_voluntario, 
                    FROM usuario u 
                    INNER JOIN voluntario v ON v.id_usuario = u.id_usuario
                    ORDER BY u.id_usuario
            """)

            for row in cursor:
                voluntario_banco = Voluntario(
                    id_usuario = row[0],
                    cpf_usuario = row[1],
                    nome_usuario = row[2],
                    email_usuario = row[3],
                    senha_usuario = row[4],
                    status_usuario = row[5],
                    data_registro_voluntario = row[6]
                )

                listaVoluntarios.append(voluntario_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaVoluntarios)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE VOLUNTÁRIOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaVoluntarios
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS VOLUNTÁRIOS NO BANCO DE DADOS: {str(e)}")
            return None