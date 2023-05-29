package services;

import dao.AgendamentoDAO;
import model.Agendamento;

/**
 * Classe de serviços para Agendamento.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Agendamento
 * @see dao.AgendamentoDAO
 * @see controller.AgendamentoResource
 * @see model.Agendamento
 * 
 * @author Raízes Solidárias
 *
 */
public class AgendamentoService {

	/**
	 * Verifica se um Agendamento com o ID especificado existe.
	 *
	 * @param id_agendamento o ID do Agendamento.
	 * @return true se um Agendamento com o ID especificado existe, caso contrário, false.
	 */
	public static boolean validarIdAgendamento(int id_agendamento) {
		return AgendamentoDAO.buscarAgendamentoPorId(id_agendamento) != null;
	}

	/**
	 * Busca e retorna um Agendamento pelo ID.
	 *
	 * @param id_agendamento o ID do Agendamento.
	 * @return o Agendamento correspondente ao ID, ou null se não encontrado.
	 */
	public static Agendamento exibirAgendamentoPorId(int id_agendamento) {
		return AgendamentoDAO.buscarAgendamentoPorId(id_agendamento);
	}

	/**
	 * Atualiza um Agendamento com as informações fornecidas.
	 *
	 * @param id_agendamento o ID do Agendamento a ser atualizado.
	 * @param usuario o Agendamento com as novas informações.
	 * @return true se o Agendamento foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarAgendamento(int id_agendamento, Agendamento agendamento) {
		Agendamento usuario_atualizar = exibirAgendamentoPorId(id_agendamento);

		if (usuario_atualizar == null || usuario_atualizar.getId_agendamento() != agendamento.getId_agendamento()) {
			return false;
		} else {
			if (AgendamentoDAO.atualizarAgendamento(agendamento))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Agendamento.
	 *
	 * @param agendamento_novo o novo Agendamento a ser cadastrado.
	 * @return o Agendamento cadastrado.
	 */
	public static Agendamento cadastrarAgendamento(Agendamento agendamento_novo) {
		return AgendamentoDAO.cadastrarAgendamento(agendamento_novo);
	}

	/**
	 * Exclui um Agendamento pelo ID.
	 *
	 * @param id_agendamento o ID do Agendamento a ser excluído.
	 * @return true se o Agendamento foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarAgendamento(int id_agendamento) {
		if (validarIdAgendamento(id_agendamento)) {
			return AgendamentoDAO.deletarAgendamento(id_agendamento);
		} else {
			return false;
		}
	}
}