import cx_Oracle

import time
from datetime import datetime
from tqdm import tqdm

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
            "01. AGENDAMENTOS\n"
            "02. ALIMENTOS\n"
            "03. COLHEITAS\n"
            "04. DESTINOS\n"
            "05. DOAÇÕES\n"
            "06. DOADORES\n"
            "07. PLANTIOS\n"
            "08. RECEPTORES\n"
            "09. USUÁRIOS\n"
            "10. VOLUNTÁRIOS\n"
            "11. SAIR\n" +
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

    def menuAdminUsuarios():
        return (Funcoes.menuCabecalho() +
            "01. CADASTRAR USUÁRIO\n"
            "02. EXIBIR USUÁRIOS\n"
            "03. EDITAR USUÁRIO\n"
            "04. EXCLUIR USUÁRIO\n"
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
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

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
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

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
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)
            
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
    
    def buscarCelsCadastrados(dsn):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)
            
            cels_cadastrados = set()
            cursor.execute("SELECT cel_usuario FROM usuario")
            results = cursor.fetchall()
            for row in results:
                cels_cadastrados.add(row[0])
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)
            return cels_cadastrados
        except Exception as e:
            print(f"OCORREU UM ERRO: {str(e)}")
            return None
    
    def buscarAgendamentosBanco(dsn, Agendamento, Usuario):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor_agendamento = conn.cursor()
            Funcoes.connect(dsn)

            listaAgendamentos = []
            cursor_agendamento.execute("""
                SELECT * FROM agendamento ORDER BY id_agendamento
            """)

            for agendamento_row in cursor_agendamento:
                agendamento_banco = Agendamento(
                    id_agendamento = agendamento_row[0],
                    data_agendamento = agendamento_row[1],
                    turno_agendamento = agendamento_row[2],
                )

                id_usuario = agendamento_row[3]

                cursor_usuario_agendamento = conn.cursor()
                cursor_usuario_agendamento.execute("""
                    SELECT * FROM usuario WHERE id_usuario = :id_usuario ORDER BY id_usuario
                """, {"id_usuario": id_usuario})

                for usuario_agendamento_row in cursor_usuario_agendamento:
                    usuario_agendamento_banco = Usuario(
                        id_usuario = usuario_agendamento_row[0],
                        cpf_usuario = usuario_agendamento_row[1],
                        nome_usuario = usuario_agendamento_row[2],
                        email_usuario = usuario_agendamento_row[3],
                        cel_usuario = usuario_agendamento_row[4],
                        senha_usuario = usuario_agendamento_row[5],
                        status_usuario = cursor_usuario_agendamento[6]
                    )

                    agendamento_banco.usuario = usuario_agendamento_banco

                cursor_usuario_agendamento.close()

                listaAgendamentos.append(agendamento_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaAgendamentos)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE AGENDAMENTOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor_agendamento)

            return listaAgendamentos
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS AGENDAMENTOS NO BANCO DE DADOS: {str(e)}")
            return None

    def buscarAlimentosBanco(dsn, Alimento):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor_alimento = conn.cursor()
            Funcoes.connect(dsn)

            listaAlimentos = []
            cursor_alimento.execute("""
                SELECT * FROM alimento ORDER BY id_alimento
            """)

            for alimento_row in cursor_alimento:
                alimento_banco = Alimento(
                    id_alimento = alimento_row[0],
                    nome_alimento = alimento_row[1],
                    tempo_colheita = alimento_row[2],
                    qtd_irrigacao = alimento_row[3],
                    preco_alimento = alimento_row[4],
                    qtd_alimento = alimento_row[5]
                )

                listaAlimentos.append(alimento_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaAlimentos)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE ALIMENTOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor_alimento)

            return listaAlimentos
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS ALIMENTOS NO BANCO DE DADOS: {str(e)}")
            return None
        
    def buscarColheitasBanco(dsn, Colheita, Voluntario, Plantio, Alimento):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor_colheita = conn.cursor()
            Funcoes.connect(dsn)

            listaColheitas = []
            cursor_colheita.execute("""
                SELECT * FROM colheita ORDER BY id_colheita
            """)

            for colheita_row in cursor_colheita:
                colheita_banco = Colheita(
                    id_colheita = colheita_row[0],
                    data_colheita = colheita_row[1],
                    descricao_colheita = colheita_row[2],
                    voluntarios_colheita = [],
                    plantios_colheita = []
                )

                cursor_voluntarios_colheita = conn.cursor()
                cursor_voluntarios_colheita.execute("""
                    SELECT cv.id_usuario, 
                    u.cpf_usuario, u.nome_usuario, u.email_usuario, u.cel_usuario, u.senha_usuario, u.status_usuario, 
                    v.data_registro_voluntario
                    FROM Colheita_Voluntario cv 
                    JOIN Voluntario v ON cv.id_usuario = v.id_usuario 
                    JOIN Usuario u ON cv.id_usuario = u.id_usuario 
                    WHERE cv.id_colheita = :id_colheita 
                    ORDER BY cv.id_usuario
                """, {"id_colheita": colheita_banco.id_colheita})

                for voluntarios_colheita_row in cursor_voluntarios_colheita:
                    voluntario_colheita_banco = Voluntario(
                        id_usuario = voluntarios_colheita_row[0],
                        cpf_usuario = voluntarios_colheita_row[1],
                        nome_usuario = voluntarios_colheita_row[2],
                        email_usuario = voluntarios_colheita_row[3],
                        cel_usuario = voluntarios_colheita_row[4],
                        senha_usuario = voluntarios_colheita_row[5],
                        status_usuario = voluntarios_colheita_row[6],
                        data_registro_voluntario = voluntarios_colheita_row[7]
                    )
                    colheita_banco.voluntarios_colheita.append(voluntario_colheita_banco)

                cursor_voluntarios_colheita.close()

                cursor_plantios_colheita = conn.cursor()
                cursor_plantios_colheita.execute("""
                    SELECT pc.id_plantio, 
                    p.data_plantio, p.espaco_plantio, p.id_alimento
                    FROM Plantio_Colheita pc  
                    JOIN Plantio p ON pc.id_plantio = p.id_plantio
                    WHERE pc.id_colheita = :id_colheita 
                    ORDER BY pc.id_colheita
                """, {"id_colheita": colheita_banco.id_colheita})
                
                for plantios_colheita_row in cursor_plantios_colheita:
                    plantio_colheita_banco = Plantio(
                        id_plantio = plantios_colheita_row[0],
                        data_plantio = plantios_colheita_row[1],
                        espaco_plantio = plantios_colheita_row[2],
                    )

                    id_alimento = plantios_colheita_row[3]

                    cursor_alimento_plantio = conn.cursor
                    cursor_alimento_plantio.execute("""
                        SELECT * FROM alimento
                        WHERE id_alimento = :id_alimento 
                        ORDER BY id_alimento
                    """, {"id_alimento": id_alimento})

                    for alimento_plantio_row in cursor_alimento_plantio:
                        alimento_plantio_banco = Alimento(
                            id_alimento = alimento_plantio_row[0],
                            nome_alimento = alimento_plantio_row[1],
                            tempo_colheita = alimento_plantio_row[2],
                            qtd_irrigacao = alimento_plantio_row[3],
                            preco_alimento = alimento_plantio_row[4],
                            qtd_alimento = alimento_plantio_row[5]
                        )

                    plantio_colheita_banco.alimento = alimento_plantio_banco
                
                    cursor_alimento_plantio.close()

                cursor_plantios_colheita.close()

                colheita_banco.plantios_colheita.append(plantio_colheita_banco)

                listaColheitas.append(colheita_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaColheitas)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE COLHEITAS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor_colheita)

            return listaColheitas
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR AS COLHEITAS NO BANCO DE DADOS: {str(e)}")
            return None

    def buscarDestinosBanco(dsn, Destino, Receptor):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor_destino = conn.cursor()
            Funcoes.connect(dsn)

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

                cursor_receptores_destino = conn.cursor()
                cursor_receptores_destino.execute("""
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

                for receptores_destino_row in cursor_receptores_destino:
                    receptor_destino_banco = Receptor(
                        id_usuario = receptores_destino_row[0],
                        cpf_usuario = receptores_destino_row[1],
                        nome_usuario = receptores_destino_row[2],
                        email_usuario = receptores_destino_row[3],
                        cel_usuario = receptores_destino_row[4],
                        senha_usuario = receptores_destino_row[5],
                        status_usuario = receptores_destino_row[6],
                        carga_receptor = receptores_destino_row[7],
                        endereco_receptor = receptores_destino_row[8]
                    )
                    destino_banco.receptores_destino.append(receptor_destino_banco)

                cursor_receptores_destino.close()

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

    def buscarDoacoesBanco(dsn, Doacao, Doador):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor_doacao = conn.cursor()
            Funcoes.connect(dsn)

            listaDoacoes = []
            cursor_doacao.execute("""
                SELECT * FROM doacao ORDER BY id_doacao
            """)

            for doacao_row in cursor_doacao:
                doacao_banco = Doacao(
                    id_doacao = doacao_row[0],
                    data_doacao = doacao_row[2],
                    qtd_moedas_doacao = doacao_row[3]
                )

                id_usuario = doacao_row[1]

                cursor_doador_doacao = conn.cursor()
                cursor_doador_doacao.execute("""
                    SELECT do.id_usuario, 
                    u.cpf_usuario, u.nome_usuario, u.email_usuario, u.cel_usuario, u.senha_usuario, u.status_usuario, 
                    d.nivel_doador, d.moedas_doador 
                    FROM Doacao do 
                    JOIN Usuario u ON do.id_usuario = u.id_usuario 
                    JOIN Doador d ON do.id_usuario = d.id_usuario 
                    WHERE do.id_usuario = :id_usuario 
                    ORDER BY do.id_usuario
                """, {"id_usuario": id_usuario})

                for doador_doacao_row in cursor_doador_doacao:
                    doador_doacao_banco = Doador(
                        id_usuario = doador_doacao_row[0],
                        cpf_usuario = doador_doacao_row[1],
                        nome_usuario = doador_doacao_row[2],
                        email_usuario = doador_doacao_row[3],
                        cel_usuario = doador_doacao_row[4],
                        senha_usuario = doador_doacao_row[5],
                        status_usuario = doador_doacao_row[6],
                        nivel_doador = doador_doacao_row[7],
                        moedas_doador = doador_doacao_row[8]
                    )
                    doacao_banco.doador = doador_doacao_banco

                cursor_doador_doacao.close()

                listaDoacoes.append(doacao_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaDoacoes)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE DOAÇÕES: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor_doacao)

            return listaDoacoes
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR AS DOAÇÕES NO BANCO DE DADOS: {str(e)}")
            return None
    
    def buscarDoadoresBanco(dsn, Doador, Doacao):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor_doador = conn.cursor()
            Funcoes.connect(dsn)

            listaDoadores = []
            cursor_doador.execute("""
                SELECT 
                    u.id_usuario, 
                    u.cpf_usuario, 
                    u.nome_usuario, 
                    u.email_usuario, 
                    u.cel_usuario,
                    u.senha_usuario,
                    u.status_usuario,
                    d.nivel_doador,
                    d.moedas_doador, 
                    FROM usuario u 
                    INNER JOIN doador a ON d.id_usuario = u.id_usuario
                    ORDER BY u.id_usuario
            """)

            for doador_row in cursor_doador:
                doador_banco = Doador(
                    id_usuario = doador_row[0],
                    cpf_usuario = doador_row[1],
                    nome_usuario = doador_row[2],
                    email_usuario = doador_row[3],
                    cel_usuario = doador_row[4],
                    senha_usuario = doador_row[5],
                    status_usuario = doador_row[6],
                    nivel_doador = doador_row[7],
                    moedas_doador = doador_row[8],
                    doacoes_doador = []
                )

                cursor_doacoes_doador = conn.cursor()
                cursor_doacoes_doador.execute("""
                    SELECT * FROM doacao WHERE id_usuario = :id_usuario ORDER BY id_doacao
                """, {"id_usuario": doador_banco.id_usuario})

                for doacoes_doador_row in cursor_doacoes_doador:
                    doacao_doador_banco = Doacao(
                        id_doacao = doacoes_doador_row[0],
                        data_doacao = doacoes_doador_row[2],
                        qtd_moedas_doacao = doacoes_doador_row[3]
                    )
                    doador_banco.doacoes_doador.append(doacao_doador_banco)

                cursor_doacoes_doador.close()

                listaDoadores.append(doador_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaDoadores)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE DOADORES: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor_doador)

            return listaDoadores
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS DOADORES NO BANCO DE DADOS: {str(e)}")
            return None

    def buscarPlantiosBanco(dsn, Plantio, Alimento, Colheita, Voluntario):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor_plantio = conn.cursor()
            Funcoes.connect(dsn)

            listaPlantios = []
            cursor_plantio.execute("""
                SELECT * FROM plantio ORDER BY id_plantio
            """)

            for plantio_row in cursor_plantio:
                plantio_banco = Plantio(
                    id_plantio = plantio_row[0],
                    data_plantio = plantio_row[1],
                    espaco_plantio = plantio_row[2],
                )

                id_alimento = plantio_row[3]

                cursor_alimento_plantio = conn.cursor
                cursor_alimento_plantio.execute("""
                    SELECT * FROM alimento
                    WHERE id_alimento = :id_alimento 
                    ORDER BY id_alimento
                """, {"id_alimento": id_alimento})

                for alimento_plantio_row in cursor_alimento_plantio:
                    alimento_plantio_banco = Alimento(
                        id_alimento = alimento_plantio_row[0],
                        nome_alimento = alimento_plantio_row[1],
                        tempo_colheita = alimento_plantio_row[2],
                        qtd_irrigacao = alimento_plantio_row[3],
                        preco_alimento = alimento_plantio_row[4],
                        qtd_alimento = alimento_plantio_row[5]
                    )

                    plantio_banco.alimento = alimento_plantio_banco
                
                cursor_alimento_plantio.close()
                
                cursor_colheita_plantio = conn.cursor()
                cursor_colheita_plantio.execute("""
                    SELECT pc.id_colheita, 
                    c.data_colheita, c.descricao_colheita
                    FROM Plantio_Colheita pc 
                    JOIN Colheita c ON pc.id_colheita = c.id_colheita 
                    WHERE pc.id_plantio = :id_plantio 
                    ORDER BY pc_id_plantio
                """, {"id_plantio": plantio_banco.id_plantio})
                
                for colheita_plantio_row in cursor_colheita_plantio:
                    colheita_plantio_banco = Colheita(
                        id_colheita = colheita_plantio_row[0],
                        data_colheita = colheita_plantio_row[1],
                        descricao_colheita = colheita_plantio_row[2]
                    )

                    plantio_banco.colheita = colheita_plantio_banco
                
                cursor_colheita_plantio.close()

                cursor_voluntarios_plantio = conn.cursor()
                cursor_voluntarios_plantio.execute("""
                    SELECT pv.id_usuario, 
                    u.cpf_usuario, u.nome_usuario, u.email_usuario, u.cel_usuario, u.senha_usuario, u.status_usuario, 
                    v.data_registro_voluntario 
                    FROM Plantio_Voluntario pv 
                    JOIN Voluntario v ON pv.id_usuario = v.id_usuario 
                    JOIN Usuario u ON pv.id_usuario = u.id_usuario 
                    WHERE pv.id_plantio = :id_plantio 
                    ORDER BY pv.id_usuario
                """, {"id_plantio": plantio_banco.id_plantio})

                for voluntarios_plantio_row in cursor_voluntarios_plantio:
                    voluntario_plantio_banco = Voluntario(
                        id_usuario = voluntarios_plantio_row[0],
                        cpf_usuario = voluntarios_plantio_row[1],
                        nome_usuario = voluntarios_plantio_row[2],
                        email_usuario = voluntarios_plantio_row[3],
                        cel_usuario = voluntarios_plantio_row[4],
                        senha_usuario = voluntarios_plantio_row[5],
                        status_usuario = voluntarios_plantio_row[6],
                        data_registro_voluntario = voluntarios_plantio_row[7]
                    )
                    plantio_banco.voluntarios_plantio.append(voluntario_plantio_banco)
                
                cursor_voluntarios_plantio.close()

                listaPlantios.append(plantio_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaPlantios)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE PLANTIOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor_plantio)

            return listaPlantios
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS PLANTIOS NO BANCO DE DADOS: {str(e)}")
            return None

    def buscarReceptoresBanco(dsn, Receptor, Destino, Agendamento):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor_receptor = conn.cursor()
            Funcoes.connect(dsn)

            listaReceptores = []
            cursor_receptor.execute("""
                SELECT 
                    u.id_usuario, 
                    u.cpf_usuario, 
                    u.nome_usuario, 
                    u.email_usuario, 
                    u.cel_usuario,
                    u.senha_usuario,
                    u.status_usuario,
                    r.carga_receptor,
                    r.endereco_receptor, 
                    FROM usuario u 
                    INNER JOIN receptor r ON r.id_usuario = u.id_usuario
                    ORDER BY u.id_usuario
            """)

            for receptor_row in cursor_receptor:
                receptor_banco = Receptor(
                    id_usuario = receptor_row[0],
                    cpf_usuario = receptor_row[1],
                    nome_usuario = receptor_row[2],
                    email_usuario = receptor_row[3],
                    cel_usuario = receptor_row[4],
                    senha_usuario = receptor_row[5],
                    status_usuario = receptor_row[6],
                    carga_receptor = receptor_row[7],
                    endereco_receptor = receptor_row[8],
                    destinos_receptor = []
                )

                cursor_destinos_receptor = conn.cursor()
                cursor_destinos_receptor.execute("""
                    SELECT rd.id_destino, 
                    d.endereco_destino, d.responsavel_destino, d.cel_destino, d.qtd_dependentes_destino
                    FROM Receptor_Destino rd 
                    JOIN Destino d ON rd.id_destino = d.id_destino 
                    WHERE rd.id_usuario = :id_usuario 
                    ORDER BY rd.id_destino
                """, {"id_usuario": receptor_banco.id_usuario})

                for destinos_receptor_row in cursor_destinos_receptor:
                    destino_receptor_banco = Destino(
                        id_destino = destinos_receptor_row[0],
                        endereco_destino = destinos_receptor_row[1],
                        responsavel_destino = destinos_receptor_row[2],
                        cel_destino = destinos_receptor_row[3],
                        qtd_dependentes_destino = destinos_receptor_row[4],
                    )
                    receptor_banco.destinos_receptor.append(destino_receptor_banco)

                cursor_destinos_receptor.close()

                cursor_agendamentos_receptor = conn.cursor()
                cursor_agendamentos_receptor.execute("""
                    SELECT * FROM agendamento WHERE id_usuario = :id_usuario
                """, {"id_usuario": receptor_banco.id_usuario})

                for agendamentos_receptor_row in cursor_agendamentos_receptor:
                    agendamento_receptor_banco = Agendamento(
                        id_agendamento = agendamentos_receptor_row[0],
                        data_agendamento = agendamentos_receptor_row[1],
                        turno_agendamento = agendamentos_receptor_row[2],
                    )
                    receptor_banco.agendamentos_receptor.append(agendamento_receptor_banco)

                cursor_agendamentos_receptor.close()

                listaReceptores.append(receptor_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaReceptores)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE RECEPTORES: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor_receptor)

            return listaReceptores
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS RECEPTORES NO BANCO DE DADOS: {str(e)}")
            return None
    
    def buscarUsuariosBanco(dsn, Usuario):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            listaUsuarios = []
            cursor.execute("""
                SELECT * FROM usuario
            """)

            for row in cursor:
                usuario_banco = Usuario(
                    id_usuario = row[0],
                    cpf_usuario = row[1],
                    nome_usuario = row[2],
                    email_usuario = row[3],
                    cel_usuario = row[4],
                    senha_usuario = row[5],
                    status_usuario = row[6]
                )

                listaUsuarios.append(usuario_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaUsuarios)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE USUÁRIOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            return listaUsuarios
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS USUÁRIOS NO BANCO DE DADOS: {str(e)}")
            return None
    
    def buscarVoluntariosBanco(dsn, Voluntario, Colheita, Plantio, Alimento, Agendamento):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
            cursor_voluntario = conn.cursor()
            Funcoes.connect(dsn)

            listaVoluntarios = []
            cursor_voluntario.execute("""
                SELECT 
                    u.id_usuario, 
                    u.cpf_usuario, 
                    u.nome_usuario, 
                    u.email_usuario, 
                    u.cel_usuario, 
                    u.senha_usuario,
                    u.status_usuario,
                    v.data_registro_voluntario, 
                    FROM usuario u 
                    INNER JOIN voluntario v ON v.id_usuario = u.id_usuario
                    ORDER BY u.id_usuario
            """)

            for voluntario_row in cursor_voluntario:
                voluntario_banco = Voluntario(
                    id_usuario = voluntario_row[0],
                    cpf_usuario = voluntario_row[1],
                    nome_usuario = voluntario_row[2],
                    email_usuario = voluntario_row[3],
                    cel_usuario = voluntario_row[4],
                    senha_usuario = voluntario_row[5],
                    status_usuario = voluntario_row[6],
                    data_registro_voluntario = voluntario_row[7]
                )

                cursor_colheitas_voluntario = conn.cursor()
                cursor_colheitas_voluntario.execute("""
                    SELECT cv.id_colheita, 
                    c.data_colheita, c.descricao_colheita
                    FROM Colheita_Voluntario cv 
                    JOIN Colheita c ON cv.id_colheita = c.id_colheita 
                    WHERE cv.id_usuario = :id_usuario 
                    ORDER BY cv.id_colheita
                """, {"id_usuario": voluntario_banco.id_usuario})
                
                for colheitas_voluntario_row in cursor_colheitas_voluntario:
                    colheita_voluntario_banco = Colheita(
                        id_colheita = colheitas_voluntario_row[0],
                        data_colheita = colheitas_voluntario_row[1],
                        descricao_colheita = colheitas_voluntario_row[2]
                    )

                    voluntario_banco.colheitas_voluntario.append(colheita_voluntario_banco)
                
                cursor_colheitas_voluntario.close()

                cursor_plantios_voluntario = conn.cursor()
                cursor_plantios_voluntario.execute("""
                    SELECT pv.id_plantio, 
                    p.data_plantio, p.espaco_plantio, p.id_alimento
                    FROM Plantio_Voluntario pv
                    JOIN Plantio p ON pv.id_plantio = p.id_plantio  
                    WHERE pv.id_usuario = :id_usuario 
                    ORDER BY pv.id_plantio
                """, {"id_usuario": voluntario_banco.id_usuario})
                
                for plantios_voluntario_row in cursor_plantios_voluntario:
                    plantio_voluntario_banco = Plantio(
                        id_plantio = plantios_voluntario_row[0],
                        data_plantio = plantios_voluntario_row[1],
                        espaco_plantio = plantios_voluntario_row[2],
                    )

                    id_alimento = plantios_voluntario_row[3]

                    cursor_alimento_plantio_voluntario = conn.cursor
                    cursor_alimento_plantio_voluntario.execute("""
                        SELECT * FROM alimento
                        WHERE id_alimento = :id_alimento 
                        ORDER BY id_alimento
                    """, {"id_alimento": id_alimento})

                    for alimento_plantio_voluntario_row in cursor_alimento_plantio_voluntario:
                        alimento_plantio_voluntario_banco = Alimento(
                            id_alimento = alimento_plantio_voluntario_row[0],
                            nome_alimento = alimento_plantio_voluntario_row[1],
                            tempo_colheita = alimento_plantio_voluntario_row[2],
                            qtd_irrigacao = alimento_plantio_voluntario_row[3],
                            preco_alimento = alimento_plantio_voluntario_row[4],
                            qtd_alimento = alimento_plantio_voluntario_row[5]
                        )

                    plantio_voluntario_banco.alimento = alimento_plantio_voluntario_banco
                
                    cursor_alimento_plantio_voluntario.close()

                cursor_plantios_voluntario.close()

                cursor_agendamentos_voluntario = conn.cursor()
                cursor_agendamentos_voluntario.execute("""
                    SELECT * FROM agendamento WHERE id_usuario = :id_usuario
                """, {"id_usuario": voluntario_banco.id_usuario})

                for agendamentos_voluntario_row in cursor_agendamentos_voluntario:
                    agendamento_voluntario_banco = Agendamento(
                        id_agendamento = agendamentos_voluntario_row[0],
                        data_agendamento = agendamentos_voluntario_row[1],
                        turno_agendamento = agendamentos_voluntario_row[2],
                    )
                    voluntario_banco.agendamentos_voluntario.append(agendamento_voluntario_banco)

                cursor_agendamentos_voluntario.close()

                listaVoluntarios.append(voluntario_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaVoluntarios)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE VOLUNTÁRIOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor_voluntario)

            return listaVoluntarios
        except Exception as e:
            print(f"OCORREU UM ERRO AO BUSCAR OS VOLUNTÁRIOS NO BANCO DE DADOS: {str(e)}")
            return None