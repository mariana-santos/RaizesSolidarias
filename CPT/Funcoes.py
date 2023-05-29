from datetime import datetime
import time
from tqdm import tqdm
import cx_Oracle

class Funcoes:

    # MENUS - OK
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

    # CONFIRMAR - OK
    def confirmarAcao(acao):
        return ("TEM CERTEZA QUE DESEJA " + acao + "?\n"
        "01. SIM\n"
        "02. NÃO\n"
        "------------------------------------------\n"
        "DIGITE A OPÇÃO DESEJADA: \n")
    
    # VALIDAR E VERIFICAR - OK
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
            usuario_buscado = Funcoes.buscarPorIdUsuario(id_buscado, lista)
        
        return usuario_buscado

    def validarVoluntarioBuscado(voluntario_buscado, lista):
        while voluntario_buscado is None:
            input("ID INVÁLIDO. TECLE ENTER PARA VOLTAR AO MENU")
            Funcoes.exibirVoluntariosAdmin(lista)
            id_buscado = int(input("DIGITE O ID DO VOLUNTÁRIO NOVAMENTE: \n"))
            voluntario_buscado = Funcoes.buscarPorIdVoluntario(id_buscado, lista)
        
        return voluntario_buscado

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

    # FORMATAR - OK
    def formatarCpf(cpf_usuario):
        cpf_usuario_formatado = '{}.{}.{}-{}'.format(cpf_usuario[:3], cpf_usuario[3:6], cpf_usuario[6:9], cpf_usuario[9:])
        return cpf_usuario_formatado

    def formatarData(data):
        if isinstance(data, str):
            data = datetime.strptime(data, "%d/%m/%Y")
        data_formatada = data.strftime("%d/%m/%Y")
        return data_formatada

    # BUSCAR - OK
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
    
    def buscarPorIdUsuario(id_buscado, lista):
        objeto_buscado = lista.get(id_buscado)
        if objeto_buscado is None:
            return None
        return objeto_buscado

    # EDITAR - OK
    def editarNegativo():
        return("NÃO É POSSÍVEL EDITAR ESTA OPÇÃO.\n"
            "TECLE ENTER PARA VOLTAR AO MENU")

    def editarNome(dsn, usuario_buscado):
        novo_nome = input("DIGITE O NOVO NOME: ")
        novo_nome = Funcoes.validarPreenchimento("DIGITE O NOVO NOME: ", novo_nome)
        usuario_buscado.nome_usuario = novo_nome

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        cursor.execute("UPDATE usuario SET nome_usuario = :novo_nome WHERE id_usuario = :id_usuario", {"novo_nome": novo_nome, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()
        print("NOME DO USUÁRIO EDITADO COM SUCESSO!")

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

    def editarEmail(dsn, usuario_buscado, emails_cadastrados, Aluno):
        novo_email = input("DIGITE O NOVO EMAIL: ")
        novo_email = Funcoes.validarPreenchimento("DIGITE O NOVO EMAIL: ", novo_email)
        novo_email = Funcoes.verificarEmail(novo_email, emails_cadastrados)
        if isinstance(usuario_buscado, Aluno):
            emails_cadastrados.remove(usuario_buscado.email_usuario)
            emails_cadastrados.add(novo_email)
        usuario_buscado.email_usuario = novo_email

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        cursor.execute("UPDATE usuario SET email_usuario = :novo_email WHERE id_usuario = :id_usuario", {"novo_email": novo_email, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("EMAIL DO USUÁRIO EDITADO COM SUCESSO!")

    def editarDataNasc(dsn, usuario_buscado):
        nova_data_nasc = input("DIGITE A NOVA DATA DE NASCIMENTO DO USUÁRIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ")
        nova_data_nasc = Funcoes.validarPreenchimento("DIGITE A NOVA DATA DE NASCIMENTO DO USUÁRIO (DD/MM/YYYY, EXEMPLO: 22/06/1993): ", nova_data_nasc)
        data_formatada = datetime.strptime(nova_data_nasc, '%d/%m/%Y')
        data_formatada = data_formatada.strftime("%d/%m/%Y")
        usuario_buscado.data_nasc_aluno = data_formatada
        
        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)
        
        cursor.execute("UPDATE aluno SET dt_nasc_aluno = TO_DATE(:nova_data, 'DD/MM/YYYY') WHERE id_usuario = :id_usuario", {"nova_data": data_formatada, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()
        
        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("DATA DE NASCIMENTO DO USUÁRIO EDITADO COM SUCESSO!")

    def editarMoedas(dsn, usuario_buscado):
        try:
            moedas_adicionar = int(input(f"QUANTAS MOEDAS DESEJA ADICIONAR/SUBTRAIR DO USUÁRIO {usuario_buscado.nome_usuario}? "))
        except ValueError:
            print("POR FAVOR, DIGITE UM NÚMERO INTEIRO VÁLIDO.")
            return
        moedas_adicionar = int(Funcoes.validarPreenchimento("QUANTAS MOEDAS DESEJA ADICIONAR/SUBTRAIR DO USUÁRIO " + usuario_buscado.nome_usuario + "?", str(moedas_adicionar)))
        novas_moedas = moedas_adicionar + usuario_buscado.moedas_aluno
        usuario_buscado.moedas_aluno = novas_moedas

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        cursor.execute("UPDATE aluno SET moedas_aluno = :novas_moedas WHERE id_usuario = :id_usuario", {"novas_moedas": novas_moedas, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()

         # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("MOEDAS DO USUÁRIO ATUALIZADAS COM SUCESSO!")

    def editarLevel(dsn, usuario_buscado):
        novo_level = ("QUAL O NOVO LEVEL DO USUÁRIO {usuario_buscado['nome_usuario']}?" + "\n" +
                        "01. Iniciante" + "\n" +
                        "02. Intermediário" + "\n" + 
                        "03. Avançado" + "\n" +
                        "04. CURSO CONCLUÍDO" + "\n" + 
                        Funcoes.menuRodape())
        
        opcao = int(input(novo_level))

        opcao = int(Funcoes.validarOpcao(opcao, 1, 4, novo_level))

        if (opcao == 1):
            usuario_buscado.level_aluno = "Iniciante"

        elif (opcao == 2):
            usuario_buscado.level_aluno = "Intermediário"
        
        elif (opcao == 3):
            usuario_buscado.level_aluno = "Avançado"

        elif (opcao == 4):
            usuario_buscado.level_aluno = "CURSO CONCLUÍDO"

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)
        
        cursor.execute("UPDATE aluno SET nivel_aluno = :novo_nivel WHERE id_usuario = :id_usuario", {"novo_nivel": usuario_buscado.level_aluno, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()

         # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("LEVEL DO USUÁRIO ATUALIZADO COM SUCESSO!")

    def editarSenha(dsn, usuario_buscado, StringClasse):
        nova_senha_usuario = input("DIGITE A NOVA SENHA: ")
        conf_senha = input("CONFIRME A NOVA SENHA: ")
        nova_senha_usuario = Funcoes.validarSenha(nova_senha_usuario, conf_senha)

         # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        if StringClasse == "Aluno":
            usuario_buscado.senha_aluno = nova_senha_usuario
            cursor.execute("UPDATE aluno SET senha_aluno = :nova_senha_usuario WHERE id_usuario = :id_usuario", {"nova_senha_usuario": nova_senha_usuario, "id_usuario": usuario_buscado.id_usuario})
            cursor.connection.commit()
        
        elif StringClasse == "Funcionario":
            usuario_buscado.senha_funcionario = nova_senha_usuario
            cursor.execute("UPDATE funcionario SET senha_funcionario = :nova_senha_usuario WHERE id_usuario = :id_usuario", {"nova_senha_usuario": nova_senha_usuario, "id_usuario": usuario_buscado.id_usuario})
            cursor.connection.commit()
        
        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("SENHA DO USUÁRIO EDITADA COM SUCESSO!")

    def editarCargo(dsn, usuario_buscado):
        novo_cargo = input("DIGITE O NOVO CARGO: ")
        novo_cargo = Funcoes.validarPreenchimento("DIGITE O NOVO CARGO: ", novo_cargo)
        usuario_buscado.cargo_funcionario = novo_cargo

        # CRIANDO CONEXÃO COM O BANCO DE DADOS
        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
        cursor = conn.cursor()
        Funcoes.connect(dsn)

        cursor.execute("UPDATE funcionario SET cargo_funcionario = :novo_cargo WHERE id_usuario = :id_usuario", {"novo_cargo": novo_cargo, "id_usuario": usuario_buscado.id_usuario})
        cursor.connection.commit()

        # FECHANDO CONEXÃO COM O BANCO DE DADOS
        Funcoes.disconnect(conn, cursor)

        print("CARGO DO FUNCIONÁRIO EDITADO COM SUCESSO!")

    # EXCLUIR - OK
    def excluirUsuario(dsn, lista, StringClasse):
        Funcoes.exibirUsuariosAdmin(lista)
        id_buscado = int(input("DIGITE O ID DO USUÁRIO QUE DESEJA EXCLUIR: \n"))
        usuario_buscado = Funcoes.buscarPorIdUsuario(id_buscado, lista)
        usuario_buscado = Funcoes.validarUsuarioBuscado(usuario_buscado, lista)
        opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O USUÁRIO {usuario_buscado.nome_usuario}")))
        opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O USUÁRIO {usuario_buscado.nome_usuario}")))
        
        if (opcao == 1):
            del lista[id_buscado]

            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
            cursor = conn.cursor()
            Funcoes.connect(dsn)

            if (StringClasse == "Aluno"):
                cursor.execute("DELETE FROM aluno WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

            elif (StringClasse == "Professor"):
                cursor.execute("DELETE FROM professor WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()

            elif (StringClasse == "Funcionario"):
                cursor.execute("DELETE FROM funcionario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.execute("DELETE FROM usuario WHERE id_usuario = :id_usuario", {"id_usuario": usuario_buscado.id_usuario})
                cursor.connection.commit()
            
            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

            print("USUÁRIO EXCLUÍDO COM SUCESSO!")
            input("TECLE ENTER PARA VOLTAR AO MENU.")
        
        elif (opcao == 2):
            input("TECLE ENTER PARA VOLTAR AO MENU.")

    def excluirModulo(dsn, listaModulos):
        if len(listaModulos) == 0:
            print("NÃO EXISTEM MÓDULOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirModulosAdmin(listaModulos)
            id_buscado = int(input("DIGITE O ID DO MÓDULO QUE DESEJA EXCLUIR: \n"))
            modulo_buscado = Funcoes.buscarPorIdModulo(id_buscado, listaModulos)
            modulo_buscado = Funcoes.validarModuloBuscado(modulo_buscado, listaModulos)
            opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O MÓDULO")))
            opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O MÓDULO"))
            
            if opcao == 1:
                for i in range(len(listaModulos)):
                    if listaModulos[i].id_modulo == id_buscado:
                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                        cursor.execute("DELETE FROM modulo_aula WHERE id_modulo = :1", (listaModulos[i].id_modulo,))
                        cursor.connection.commit()

                        cursor.execute("DELETE FROM modulo_questao WHERE id_modulo = :1", (listaModulos[i].id_modulo,))
                        cursor.connection.commit()

                        cursor.execute("DELETE FROM modulo WHERE id_modulo = :1", (listaModulos[i].id_modulo,))
                        cursor.connection.commit()

                        del listaModulos[i]

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                        print("MÓDULO EXCLUÍDO COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                        break
                
            elif opcao == 2:
                input("TECLE ENTER PARA VOLTAR AO MENU.")
    
    def excluirAula(dsn, listaAulas):
        if len(listaAulas) == 0:
            print("NÃO EXISTEM AULAS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirAulasAdmin(listaAulas)
            id_buscado = int(input("DIGITE O ID DA AULA QUE DESEJA EXCLUIR: \n"))
            aula_buscada = Funcoes.buscarPorIdAula(id_buscado, listaAulas)
            aula_buscada = Funcoes.validarAulaBuscada(aula_buscada, listaAulas)
            opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR A AULA")))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR A AULA")))
            
            if (opcao == 1):
                for i in range(len(listaAulas)):
                    if listaAulas[i].id_aula == id_buscado:
                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                        cursor.execute("DELETE FROM modulo_aula WHERE id_aula = :1", (listaAulas[i].id_aula,))
                        cursor.connection.commit()

                        cursor.execute("DELETE FROM aula WHERE id_aula = :1", (listaAulas[i].id_aula,))
                        cursor.connection.commit()

                        del listaAulas[i]

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                        print("AULA EXCLUÍDA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 2):
                input("TECLE ENTER PARA VOLTAR AO MENU.")
    
    def excluirQuestao(dsn, listaQuestoes):
        if len(listaQuestoes) == 0:
            print("NÃO EXISTEM QUESTÕES CADASTRADAS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirQuestoesAdmin(listaQuestoes)
            id_buscado = int(input("DIGITE O ID DA QUESTÃO QUE DESEJA EXCLUIR: \n"))
            questao_buscada = Funcoes.buscarPorIdQuestao(id_buscado, listaQuestoes)
            questao_buscada = Funcoes.validarQuestaoBuscada(questao_buscada, listaQuestoes)
            opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR A QUESTÃO")))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR A QUESTÃO")))
            
            if (opcao == 1):
                for i in range(len(listaQuestoes)):
                    if listaQuestoes[i].id_questao == id_buscado:
                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                        cursor.execute("DELETE FROM modulo_questao WHERE id_questao = :1", (listaQuestoes[i].id_questao,))
                        cursor.connection.commit()

                        cursor.execute("DELETE FROM questao WHERE id_questao = :1", (listaQuestoes[i].id_questao,))
                        cursor.connection.commit()

                        del listaQuestoes[i]

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                        print("QUESTÃO EXCLUÍDA COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
                        
            elif (opcao == 2):
                input("TECLE ENTER PARA VOLTAR AO MENU.")

    def excluirProduto(dsn, listaProdutos):
        if len(listaProdutos) == 0:
            print("NÃO EXISTEM PRODUTOS CADASTRADOS. TECLE ENTER PARA VOLTAR AO MENU")
        
        else:
            Funcoes.exibirProdutosAdmin(listaProdutos)
            id_buscado = int(input("DIGITE O ID DO PRODUTO QUE DESEJA EXCLUIR: \n"))
            produto_buscado = Funcoes.buscarPorIdProduto(id_buscado, listaProdutos)
            produto_buscado = Funcoes.validarAulaBuscada(produto_buscado, listaProdutos)
            opcao = int(input(Funcoes.confirmarAcao(f"EXCLUIR O PRODUTO")))
            opcao = int(Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao(f"EXCLUIR O PRODUTO")))
            
            if (opcao == 1):
                for i in range(len(listaProdutos)):
                    if listaProdutos[i].id_produto == id_buscado:
                        # CRIANDO CONEXÃO COM O BANCO DE DADOS
                        conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
                        cursor = conn.cursor()
                        Funcoes.connect(dsn)

                        # EXCLUINDO DO BANCO DE DADOS E DA LISTA
                        cursor.execute("DELETE FROM produto WHERE id_produto = :1", (listaProdutos[i].id_produto,))
                        cursor.connection.commit()

                        del listaProdutos[i]

                        # FECHANDO CONEXÃO COM O BANCO DE DADOS
                        Funcoes.disconnect(conn, cursor)

                        print("PRODUTO EXCLUÍDO COM SUCESSO!")
                        input("TECLE ENTER PARA VOLTAR AO MENU.")
            
            elif (opcao == 2):
                input("TECLE ENTER PARA VOLTAR AO MENU.")
    
    # EXIBIR - OK
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

    def exibirUsuariosAdmin(dicionario):
        Funcoes.menuCabecalho()

        if len(dicionario) == 0:
            print("NÃO EXISTEM USUÁRIOS CADASTRADOS.")
        else:
            for id_usuario, usuario in dicionario.items():
                print(f"ID: {id_usuario} | CPF: {Funcoes.formatarCpf(usuario.cpf_usuario)} | NOME: {usuario.nome_usuario}")
                print("------------------------------------------")

    # BANCO DE DADOS
    def connect(dsn):
        try:
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
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
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
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
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
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
            conn = cx_Oracle.connect(user='RM96466', password='220693', dsn=dsn)
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

    def buscarDestinosBanco(dsn, Destino):
        try:
            # CRIANDO CONEXÃO COM O BANCO DE DADOS
            conn = Funcoes.connect(dsn)
            cursor = conn.cursor()

            listaDestinos = []
            cursor.execute("""
                SELECT * FROM destino ORDER BY id_destino
            """)

            for row in cursor:
                destino_banco = Destino(
                    id_destino = row[0],
                    endereco_destino = row[1],
                    responsavel_destino = row[2],
                    cel_destino = row[3],
                    qtd_dependentes_destino = row[4]
                )

                listaDestinos.append(destino_banco)

            # MOSTRANDO BARRA DE PROGRESSO
            barra_progresso = tqdm(listaDestinos)
            for i in barra_progresso:
                time.sleep(0.25)
                barra_progresso.set_description('CARREGANDO BASE DE DADOS DE DESTINOS: ')

            # FECHANDO CONEXÃO COM O BANCO DE DADOS
            Funcoes.disconnect(conn, cursor)

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