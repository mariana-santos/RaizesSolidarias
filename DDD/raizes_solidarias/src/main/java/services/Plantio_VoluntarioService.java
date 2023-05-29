package services;

import dao.Plantio_VoluntarioDAO;
import model.Plantio_Voluntario;

/**
 * Classe de serviços para Plantio_Voluntario.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Plantio_Voluntario
 * @see dao.Plantio_VoluntarioDAO
 * @see controller.Plantio_VoluntarioResource
 * @see model.Plantio_Voluntario
 * @see model.Plantio
 * @see model.Voluntario
 * 
 * @author Raízes Solidárias
 *
 */
public class Plantio_VoluntarioService {
	
	/**
	 * Verifica se um Plantio_Voluntario com os ID's especificados existe.
	 *
	 * @param id_plantio 	o ID do Plantio.
	 * @param id_usuario	o ID do Voluntario (Usuario)
	 * @return true se um Plantio_Voluntario com os ID's especificados existe, caso contrário, false.
	 */
	public static boolean validarIdsPlantio_Voluntario(int id_plantio, int id_usuario) {
		return Plantio_VoluntarioDAO.buscarPlantio_VoluntarioPorIds(id_plantio, id_usuario) != null;
	}
	
	/**
	 * Busca e retorna um Plantio_Voluntario com o ID do Plantio e o ID do Voluntario especificados.
	 *
	 * @param id_plantio o ID do Plantio.
	 * @param id_usuario  o ID do Voluntario (Usuario).
	 * @return true se um Plantio_Voluntario com o ID do Plantio e ID do Voluntario (Usuario) especificados existe, caso contrário, false.
	 */
	public static Plantio_Voluntario exibirPlantio_VoluntarioPorIds(int id_plantio, int id_usuario) {
		return Plantio_VoluntarioDAO.buscarPlantio_VoluntarioPorIds(id_plantio, id_usuario);
	}

	/**
	 * Atualiza um Plantio_Voluntario com as informações fornecidas.
	 *
	 * @param id_plantio_novo 	o ID do Plantio que será atualizado.
	 * @param id_plantio_antigo o ID do Plantio a ser atualizado.
	 * @param id_usuario_novo	o ID do Voluntario (Usuario) que será atualizado.
	 * @param id_usuario_antigo	o ID do Voluntario (Usuario) a ser atualizado.
	 * @return true se o Plantio_Voluntario foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarPlantio_Voluntario(int id_plantio_novo, int id_plantio_antigo, int id_usuario_novo, int id_usuario_antigo) {
		Plantio_Voluntario plantio_voluntario_atualizar = exibirPlantio_VoluntarioPorIds(id_plantio_antigo, id_usuario_antigo);

		if (plantio_voluntario_atualizar == null || plantio_voluntario_atualizar.getVoluntario().getId_usuario() != id_usuario_antigo || plantio_voluntario_atualizar.getPlantio().getId_plantio() != id_plantio_antigo) {
			return false;
		} else {
			if (Plantio_VoluntarioDAO.atualizarPlantio_Voluntario(id_plantio_novo, id_plantio_antigo, id_usuario_novo, id_usuario_antigo))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Plantio_Voluntario.
	 *
	 * @param plantio_voluntario_novo o novo Plantio_Voluntario a ser cadastrado.
	 * @return o Plantio_Voluntario cadastrado.
	 */
	public static Plantio_Voluntario cadastrarPlantio_Voluntario(Plantio_Voluntario plantio_voluntario_novo) {
		return Plantio_VoluntarioDAO.cadastrarPlantio_Voluntario(plantio_voluntario_novo);
	}

	/**
	 * Exclui um Plantio_Voluntario pelos ID's do Plantio e da Voluntario.
	 *
	 * @param id_plantio 	o ID do Plantio do Plantio_Voluntario a ser excluído.
	 * @param id_usuario 	o ID do Voluntario (Usuario) do Plantio_Voluntario a ser excluído.
	 * @return true se o Plantio_Voluntario foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarPlantio_Voluntario(int id_plantio, int id_usuario) {
		if (validarIdsPlantio_Voluntario(id_plantio, id_usuario)) {
			return Plantio_VoluntarioDAO.deletarPlantio_Voluntario(id_plantio, id_usuario);
		} else {
			return false;
		}
	}
}