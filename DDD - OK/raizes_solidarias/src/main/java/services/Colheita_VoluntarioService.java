package services;

import dao.Colheita_VoluntarioDAO;
import model.Colheita_Voluntario;

/**
 * Classe de serviços para Colheita_Voluntario.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Colheita_Voluntario
 * @see dao.Colheita_VoluntarioDAO
 * @see controller.Colheita_VoluntarioResource
 * @see model.Colheita_Voluntario
 * @see model.Colheita
 * @see model.Voluntario
 * 
 * @author Raízes Solidárias
 *
 */
public class Colheita_VoluntarioService {
	
	/**
	 * Verifica se um Colheita_Voluntario com os ID's especificados existe.
	 *
	 * @param id_colheita 	o ID da Colheita.
	 * @param id_usuario	o ID do Voluntario (Usuario)
	 * @return true se um Colheita_Voluntario com os ID's especificados existe, caso contrário, false.
	 */
	public static boolean validarIdsColheita_Voluntario(int id_colheita, int id_usuario) {
		return Colheita_VoluntarioDAO.buscarColheita_VoluntarioPorIds(id_colheita, id_usuario) != null;
	}
	
	/**
	 * Busca e retorna um Colheita_Voluntario com o ID da Colheita e o ID do Voluntario (Usuario) especificados.
	 *
	 * @param id_colheita o ID da Colheita.
	 * @param id_usuario  o ID do Voluntario (Usuario).
	 * @return true se um Colheita_Voluntario com o ID da Colheita e ID do Voluntario (Usuario) especificados existe, caso contrário, false.
	 */
	public static Colheita_Voluntario exibirColheita_VoluntarioPorIds(int id_colheita, int id_usuario) {
		return Colheita_VoluntarioDAO.buscarColheita_VoluntarioPorIds(id_colheita, id_usuario);
	}

	/**
	 * Atualiza um Colheita_Voluntario com as informações fornecidas.
	 *
	 * @param id_usuario_novo 	o ID do Voluntario (Usuario) que será atualizado.
	 * @param id_usuario_antigo o ID do Voluntario (Usuario) a ser atualizado.
	 * @param id_colheita		o ID da Colheita a ser atualizada.
	 * @return true se o Colheita_Voluntario foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarColheita_Voluntario(int id_usuario_novo, int id_usuario_antigo, int id_colheita) {
		Colheita_Voluntario colheita_voluntario_atualizar = exibirColheita_VoluntarioPorIds(id_colheita, id_usuario_antigo);

		if (colheita_voluntario_atualizar == null || colheita_voluntario_atualizar.getColheita().getId_colheita() != id_colheita || colheita_voluntario_atualizar.getVoluntario().getId_usuario() != id_usuario_antigo) {
			return false;
		} else {
			if (Colheita_VoluntarioDAO.atualizarColheita_Voluntario(id_usuario_novo, id_usuario_antigo, id_colheita))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Colheita_Voluntario.
	 *
	 * @param colheita_voluntario_novo o novo Colheita_Voluntario a ser cadastrado.
	 * @return o Colheita_Voluntario cadastrado.
	 */
	public static Colheita_Voluntario cadastrarColheita_Voluntario(Colheita_Voluntario colheita_voluntario_novo) {
		return Colheita_VoluntarioDAO.cadastrarColheita_Voluntario(colheita_voluntario_novo);
	}

	/**
	 * Exclui um Colheita_Voluntario pelos ID's da Colheita e do Voluntario (Usuario).
	 *
	 * @param id_colheita 	o ID da Colheita do Colheita_Voluntario a ser excluído.
	 * @param id_usuario 	o ID do Voluntario (Usuario) do Colheita_Voluntario a ser excluído.
	 * @return true se o Colheita_Voluntario foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarColheita_Voluntario(int id_colheita, int id_usuario) {
		if (validarIdsColheita_Voluntario(id_colheita, id_usuario)) {
			return Colheita_VoluntarioDAO.deletarColheita_Voluntario(id_colheita, id_usuario);
		} else {
			return false;
		}
	}
}