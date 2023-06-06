# OBSERVAÇÕES
# OS DADOS PARA VALIDAÇÃO DAS ALTERAÇÕES NO BANCO SÃO:  
# dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
# conn = cx_Oracle.connect(user='RM97503', password='280304', dsn=dsn)
# 
# NO CASO DE DELETAR USUÁRIOS (RECEPTOR, DOADOR OU VOLUNTÁRIO) OPTAMOS POR NÃO FAZER O DELETE E SIM ALTERAR O STATUS DO MESMO PARA MANTER AS AÇÕES JÁ REALIZADAS NO BANCO DE DADOS

# IMPORTANDO CLASSES
from Agendamento import Agendamento
from Alimento import Alimento
from Colheita import Colheita
from Destino import Destino
from Doacao import Doacao
from Doador import Doador
from Funcoes import Funcoes
from Plantio import Plantio
from Receptor import Receptor
from Usuario import Usuario
from Voluntario import Voluntario
import cx_Oracle

# ESTABELECENDO CONEXÃO COM O BANCO DE DADOS
cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient_21_9")
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')

# MENSAGEM INICIAL
print("==> RAÍZES SOLIDÁRIAS - GLOBAL SOLUTIONS - 1TDSPR <==")
print("------------------------------------------")
print("AGUARDE ENQUANTO O SISTEMA ESTÁ ATUALIZANDO O BANCO DE DADOS")
print("------------------------------------------")

# CRIANDO LISTAS E SET'S
listaAgendamentos = Funcoes.buscarAgendamentosBanco(dsn, Agendamento, Usuario)
listaAlimentos = Funcoes.buscarAlimentosBanco(dsn, Alimento)
listaColheitas = Funcoes.buscarColheitasBanco(dsn, Colheita, Voluntario, Plantio, Alimento)
listaDestinos = Funcoes.buscarDestinosBanco(dsn, Destino, Receptor)
listaDoacoes = Funcoes.buscarDoacoesBanco(dsn, Doacao, Doador)
listaDoadores = Funcoes.buscarDoadoresBanco(dsn, Doador, Doacao)
listaPlantios = Funcoes.buscarPlantiosBanco(dsn, Plantio, Alimento, Colheita, Voluntario)
listaReceptores = Funcoes.buscarReceptoresBanco(dsn, Receptor, Destino, Agendamento)
listaUsuarios = Funcoes.buscarUsuariosBanco(dsn, Usuario)
listaVoluntarios = Funcoes.buscarVoluntariosBanco(dsn, Voluntario, Colheita, Plantio, Alimento, Agendamento)
cpfs_cadastrados = Funcoes.buscarCpfsCadastrados(dsn)
emails_cadastrados = Funcoes.buscarEmailsCadastrados(dsn)
cel_cadastrados = Funcoes.buscarCelsCadastrados(dsn)
listaUsuariosNaoDoadores = Funcoes.criarListaUsuariosNaoDoadores(listaUsuarios, listaDoadores)
listaUsuariosNaoReceptores = Funcoes.criarListaUsuariosNaoReceptores(listaUsuarios, listaReceptores)
listaUsuariosNaoVoluntarios = Funcoes.criarListaUsuariosNaoVoluntarios(listaUsuarios, listaVoluntarios)

# DECLARANDO VARIÁVEIS INICIAIS - OK
iniciar = True
id_agendamento = Funcoes.buscarIdMax(dsn, "id_agendamento", "agendamento")
id_alimento = Funcoes.buscarIdMax(dsn, "id_alimento", "alimento")
id_colheita = Funcoes.buscarIdMax(dsn, "id_colheita", "colheita")
id_destino = Funcoes.buscarIdMax(dsn, "id_destino", "destino")
id_doacao = Funcoes.buscarIdMax(dsn, "id_doacao", "doacao")
id_plantio = Funcoes.buscarIdMax(dsn, "id_plantio", "plantio")
id_usuario = Funcoes.buscarIdMax(dsn, "id_usuario", "usuario")

while (iniciar):
    try:
        # MENU INICIAL
        print("------------------------------------------")
        opcao = int(input(Funcoes.menuInicial()))
        opcao = int(Funcoes.validarOpcao(opcao, 1, 12, Funcoes.menuInicial()))

        if (opcao == 1):
            # MENU AGENDAMENTO
            menuAdminAgendamentos = True

            while (menuAdminAgendamentos):
                opcao = int(input(Funcoes.menuAdminAgendamentos()))
                opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminAgendamentos())

                if (opcao == 1):
                    # CADASTRAR AGENDAMENTO
                    Agendamento.cadastrarAgendamento(dsn, id_agendamento, listaReceptores, listaVoluntarios, listaAgendamentos)
                    id_agendamento = id_agendamento + 1

                elif (opcao == 2):
                    # EXIBIR AGENDAMENTOS
                    Funcoes.exibirAgendamentosAdmin(listaAgendamentos)
                    input("TECLE ENTER PARA VOLTAR AO MENU\n")
                
                elif (opcao == 3):
                    # EDITAR AGENDAMENTO
                    Agendamento.editarAgendamento(dsn, listaAgendamentos, listaReceptores, listaVoluntarios)
                
                elif (opcao == 4):
                    # EXCLUIR AGENDAMENTO
                    Agendamento.excluirAgendamento(dsn, listaAgendamentos)
                
                elif (opcao == 5):
                    # SAIR DO MENU AGENDAMENTO
                    menuAdminAgendamentos = False

        elif (opcao == 2):
            # MENU ALIMENTO
            menuAdminAlimentos = True

            while (menuAdminAlimentos):
                opcao = int(input(Funcoes.menuAdminAlimentos()))
                opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminAlimentos())

                if (opcao == 1):
                    # CADASTRAR ALIMENTO
                    Alimento.cadastrarAlimento(dsn, id_alimento, listaAlimentos)
                    id_alimento = id_alimento + 1

                elif (opcao == 2):
                    # EXIBIR ALIMENTOS
                    Funcoes.exibirAlimentosAdmin(listaAlimentos)
                    input("TECLE ENTER PARA VOLTAR AO MENU\n")
                
                elif (opcao == 3):
                    # EDITAR ALIMENTO
                    Alimento.editarAlimento(dsn, listaAlimentos)
                
                elif (opcao == 4):
                    # EXCLUIR ALIMENTO
                    Alimento.excluirAlimento(dsn, listaAlimentos)
                
                elif (opcao == 5):
                    # SAIR DO MENU ALIMENTO
                    menuAdminAlimentos = False
        
        elif (opcao == 3):
            # MENU COLHEITA
            menuAdminColheitas = True

            while (menuAdminColheitas):
                opcao = int(input(Funcoes.menuAdminColheitas()))
                opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminColheitas())

                if (opcao == 1):
                    # CADASTRAR COLHEITA
                    Colheita.cadastrarColheita(dsn, id_colheita, listaColheitas, listaVoluntarios, listaPlantios)
                    id_colheita = id_colheita + 1

                elif (opcao == 2):
                    # EXIBIR COLHEITAS
                    Funcoes.exibirColheitasAdmin(listaColheitas)
                    input("TECLE ENTER PARA VOLTAR AO MENU\n")
                
                elif (opcao == 3):
                    # EDITAR COLHEITA
                    Colheita.editarColheita(dsn, listaColheitas, listaVoluntarios, listaPlantios)
                
                elif (opcao == 4):
                    # EXCLUIR COLHEITA
                    Colheita.excluirColheita(dsn, listaColheitas)
                
                elif (opcao == 5):
                    # SAIR DO MENU COLHEITA
                    menuAdminColheitas = False
            
        elif (opcao == 4):
            # MENU DESTINO
            menuAdminDestinos = True

            while (menuAdminDestinos):
                opcao = int(input(Funcoes.menuAdminDestinos()))
                opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminDestinos())

                if (opcao == 1):
                    # CADASTRAR DESTINO
                    Destino.cadastrarDestino(dsn, id_destino, listaDestinos, listaReceptores)
                    id_destino = id_destino + 1

                elif (opcao == 2):
                    # EXIBIR DESTINOS
                    Funcoes.exibirDestinosAdmin(listaDestinos)
                    input("TECLE ENTER PARA VOLTAR AO MENU\n")
                
                elif (opcao == 3):
                    # EDITAR DESTINO
                    Destino.editarDestino(dsn, listaDestinos, listaReceptores)
                
                elif (opcao == 4):
                    # EXCLUIR DESTINO
                    Destino.excluirDestino(dsn, listaDestinos)
                
                elif (opcao == 5):
                    # SAIR DO MENU DESTINO
                    menuAdminDestinos = False
        
        elif (opcao == 5):
            # MENU DOAÇÃO
            menuAdminDoacoes = True

            while (menuAdminDoacoes):
                opcao = int(input(Funcoes.menuAdminDoacoes()))
                opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminDoacoes())

                if (opcao == 1):
                    # CADASTRAR DOAÇÃO
                    Doacao.cadastrarDoacao(dsn, id_doacao, listaDoacoes, listaDoadores)
                    id_doacao = id_doacao + 1

                elif (opcao == 2):
                    # EXIBIR DOAÇÕES
                    Funcoes.exibirDoacoesAdmin(listaDoacoes)
                    input("TECLE ENTER PARA VOLTAR AO MENU\n")
                
                elif (opcao == 3):
                    # EDITAR DOAÇÃO
                    Doacao.editarDoacao(dsn, listaDoacoes, listaDoadores)
                
                elif (opcao == 4):
                    # EXCLUIR DOAÇÃO
                    Doacao.excluirDoacao(dsn, listaDoacoes)
                
                elif (opcao == 5):
                    # SAIR DO MENU DOAÇÃO
                    menuAdminDoacoes = False

        elif (opcao == 6):
            # MENU DOADOR
            menuAdminDoadores = True

            while (menuAdminDoadores):
                opcao = int(input(Funcoes.menuAdminDoadores()))
                opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminDoadores())

                if (opcao == 1):
                    # CADASTRAR DOADOR
                    Doador.cadastrarDoador(dsn, id_usuario, listaUsuariosNaoDoadores, listaDoadores)
                    id_usuario = id_usuario + 1

                elif (opcao == 2):
                    # EXIBIR DOADORES
                    Funcoes.exibirUsuariosAdmin(listaDoadores)
                    input("TECLE ENTER PARA VOLTAR AO MENU\n")
                
                elif (opcao == 3):
                    # EDITAR DOADOR
                    Doador.editarDoador(dsn, listaDoadores, listaDoacoes, emails_cadastrados, cel_cadastrados)
                
                elif (opcao == 4):
                    # EXCLUIR DOADOR
                    Doador.excluirDoador(dsn, listaDoadores)

                elif (opcao == 5):
                    # SAIR DO MENU DOADOR
                    menuAdminDoadores = False
        
        elif (opcao == 7):
            # MENU PLANTIO
            menuAdminPlantios = True

            while (menuAdminPlantios):
                opcao = int(input(Funcoes.menuAdminPlantios()))
                opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminPlantios())

                if (opcao == 1):
                    # CADASTRAR PLANTIO
                    Plantio.cadastrarPlantio(dsn, id_plantio, listaPlantios, listaAlimentos, listaVoluntarios)
                    id_plantio = id_plantio + 1

                elif (opcao == 2):
                    # EXIBIR PLANTIOS
                    Funcoes.exibirPlantiosAdmin(listaPlantios)
                    input("TECLE ENTER PARA VOLTAR AO MENU\n")
                
                elif (opcao == 3):
                    # EDITAR PLANTIO
                    Plantio.editarPlantio(dsn, listaPlantios, listaAlimentos, listaColheitas, listaVoluntarios)
                
                elif (opcao == 4):
                    # EXCLUIR PLANTIO
                    Plantio.excluirPlantio(dsn, listaPlantios)
                
                elif (opcao == 5):
                    # SAIR DO MENU PLANTIO
                    menuAdminPlantios = False
        
        elif (opcao == 8):
            # MENU RECEPTOR
            menuAdminReceptores = True

            while (menuAdminReceptores):
                opcao = int(input(Funcoes.menuAdminReceptores()))
                opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminReceptores())

                if (opcao == 1):
                    # CADASTRAR RECEPTOR
                    Receptor.cadastrarReceptor(dsn, id_usuario, listaUsuariosNaoReceptores, listaReceptores, listaDestinos)
                    id_usuario = id_usuario + 1

                elif (opcao == 2):
                    # EXIBIR RECEPTORES
                    Funcoes.exibirUsuariosAdmin(listaReceptores)
                    input("TECLE ENTER PARA VOLTAR AO MENU\n")
                
                elif (opcao == 3):
                    # EDITAR RECEPTOR
                    Receptor.editarReceptor(dsn, listaReceptores, listaDestinos, listaAgendamentos, emails_cadastrados, cel_cadastrados)
                
                elif (opcao == 4):
                    # EXCLUIR RECEPTOR
                    Receptor.excluirReceptor(dsn, listaReceptores)
                
                elif (opcao == 5):
                    # SAIR DO MENU RECEPTOR
                    menuAdminReceptores = False
        
        elif (opcao == 9):
            # MENU USUÁRIO
            menuAdminUsuarios = True

            while (menuAdminUsuarios):
                opcao = int(input(Funcoes.menuAdminUsuarios()))
                opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminUsuarios())

                if (opcao == 1):
                    # CADASTRAR USUÁRIO
                    Usuario.cadastrarUsuario(dsn, id_usuario, listaUsuarios, cpfs_cadastrados, emails_cadastrados, cel_cadastrados)
                    id_usuario = id_usuario + 1

                elif (opcao == 2):
                    # EXIBIR USUÁRIOS
                    Funcoes.exibirUsuariosAdmin(listaUsuarios)
                    input("TECLE ENTER PARA VOLTAR AO MENU\n")
                
                elif (opcao == 3):
                    # EDITAR USUÁRIO
                    Usuario.editarUsuario(dsn, listaUsuarios, emails_cadastrados, cel_cadastrados)
                
                elif (opcao == 4):
                    # EXCLUIR USUÁRIO
                    Usuario.excluirUsuario(dsn, listaUsuarios)
                
                elif (opcao == 5):
                    # SAIR DO MENU USUÁRIO
                    menuAdminUsuarios = False

        elif (opcao == 10):
            # MENU VOLUNTÁRIO
            menuAdminVoluntarios = True

            while (menuAdminVoluntarios):
                opcao = int(input(Funcoes.menuAdminVoluntarios()))
                opcao = Funcoes.validarOpcao(opcao, 1, 5, Funcoes.menuAdminVoluntarios())

                if (opcao == 1):
                    # CADASTRAR VOLUNTÁRIO
                    Voluntario.cadastrarVoluntario(dsn, id_usuario, listaUsuariosNaoVoluntarios, listaVoluntarios)
                    id_usuario = id_usuario + 1

                elif (opcao == 2):
                    # EXIBIR VOLUNTÁRIOS
                    Funcoes.exibirUsuariosAdmin(listaVoluntarios)
                    input("TECLE ENTER PARA VOLTAR AO MENU\n")
                
                elif (opcao == 3):
                    # EDITAR VOLUNTÁRIO
                    Voluntario.editarVoluntario(dsn, listaVoluntarios, listaColheitas, listaPlantios, listaAgendamentos, emails_cadastrados, cel_cadastrados)
                
                elif (opcao == 4):
                    # EXCLUIR VOLUNTÁRIO
                    Voluntario.excluirVoluntario(dsn, listaVoluntarios)
                
                elif (opcao == 5):
                    # SAIR DO MENU VOLUNTÁRIO
                    menuAdminVoluntarios = False

        elif (opcao == 11):
            # ATUALIZAR TODAS AS LISTAS
            listaAgendamentos = Funcoes.buscarAgendamentosBanco(dsn, Agendamento, Usuario)
            listaAlimentos = Funcoes.buscarAlimentosBanco(dsn, Alimento)
            listaColheitas = Funcoes.buscarColheitasBanco(dsn, Colheita, Voluntario, Plantio, Alimento)
            listaDestinos = Funcoes.buscarDestinosBanco(dsn, Destino, Receptor)
            listaDoacoes = Funcoes.buscarDoacoesBanco(dsn, Doacao, Doador)
            listaDoadores = Funcoes.buscarDoadoresBanco(dsn, Doador, Doacao)
            listaPlantios = Funcoes.buscarPlantiosBanco(dsn, Plantio, Alimento, Colheita, Voluntario)
            listaReceptores = Funcoes.buscarReceptoresBanco(dsn, Receptor, Destino, Agendamento)
            listaUsuarios = Funcoes.buscarUsuariosBanco(dsn, Usuario)
            listaVoluntarios = Funcoes.buscarVoluntariosBanco(dsn, Voluntario, Colheita, Plantio, Alimento, Agendamento)
            cpfs_cadastrados = Funcoes.buscarCpfsCadastrados(dsn)
            emails_cadastrados = Funcoes.buscarEmailsCadastrados(dsn)
            cel_cadastrados = Funcoes.buscarCelsCadastrados(dsn)
            listaUsuariosNaoDoadores = Funcoes.criarListaUsuariosNaoDoadores(listaUsuarios, listaDoadores)
            listaUsuariosNaoReceptores = Funcoes.criarListaUsuariosNaoReceptores(listaUsuarios, listaReceptores)
            listaUsuariosNaoVoluntarios = Funcoes.criarListaUsuariosNaoVoluntarios(listaUsuarios, listaVoluntarios)

        elif (opcao == 12):
            # ENCERRAR O PROGRAMA
            opcao = int(input(Funcoes.confirmarAcao("SAIR")))
            opcao = Funcoes.validarOpcao(opcao, 1, 2, Funcoes.confirmarAcao("SAIR"))
        
            if opcao == 1:        
                print("PROGRAMA ENCERRADO.")
                iniciar = False
                
            elif (opcao == 2):
                input("TECLE ENTER PARA VOLTAR AO MENU")
    
    except ValueError as value_error:
            print("ERRO DE VALOR DURANTE A DIGITAÇÃO DA OPÇÃO:")
            print(str(value_error))
    
    except Exception as e:
            print(f"OCORREU UM ERRO AO EXECUTAR O PROGRAMA: {str(e)}")