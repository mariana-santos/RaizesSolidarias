package services;

import dao.VoluntarioDAO;
import model.Voluntario;

/**
 * Classe de serviços para Voluntario.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Voluntario
 * @see dao.VoluntarioDAO
 * @see controller.VoluntarioResource
 * @see model.Usuario
 * @see model.Voluntario
 * 
 * @author Raízes Solidárias
 *
 */
public class VoluntarioService {

	/**
	 * Verifica se um Voluntario com o ID especificado existe.
	 *
	 * @param id_usuario o ID do Usuario.
	 * @return true se um Voluntario com o ID especificado existe, caso contrário, false.
	 */
	public static boolean validarIdVoluntario(int id_usuario) {
		return VoluntarioDAO.buscarVoluntarioPorId(id_usuario) != null;
	}

	/**
	 * Busca e retorna um Voluntario pelo ID.
	 *
	 * @param id_usuario o ID do Usuario.
	 * @return o Voluntario correspondente ao ID, ou null se não encontrado.
	 */
	public static Voluntario exibirVoluntarioPorId(int id_usuario) {
		return VoluntarioDAO.buscarVoluntarioPorId(id_usuario);
	}

	/**
	 * Atualiza um Voluntario com as informações fornecidas.
	 *
	 * @param id_usuario o ID do Usuario a ser atualizado.
	 * @param usuario o Voluntario com as novas informações.
	 * @return true se o Voluntario foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarVoluntario(int id_usuario, Voluntario voluntario) {
		Voluntario usuario_atualizar = exibirVoluntarioPorId(id_usuario);

		if (usuario_atualizar == null || usuario_atualizar.getId_usuario() != voluntario.getId_usuario()) {
			return false;
		} else {
			if (VoluntarioDAO.atualizarVoluntario(voluntario))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Voluntario.
	 *
	 * @param voluntario_novo o novo Voluntario a ser cadastrado.
	 * @return o Voluntario cadastrado.
	 */
	public static Voluntario cadastrarVoluntario(Voluntario voluntario_novo) {
		return VoluntarioDAO.cadastrarVoluntario(voluntario_novo);
	}

	/**
	 * Exclui um Voluntario pelo ID.
	 *
	 * @param id_usuario o ID do Usuario a ser excluído.
	 * @return true se o Voluntario foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarVoluntario(int id_usuario) {
		if (validarIdVoluntario(id_usuario)) {
			return VoluntarioDAO.deletarVoluntario(id_usuario);
		} else {
			return false;
		}
	}
}