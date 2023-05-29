package services;

import dao.Receptor_DestinoDAO;
import model.Receptor_Destino;

/**
 * Classe de serviços para Receptor_Destino.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Receptor_Destino
 * @see dao.Receptor_DestinoDAO
 * @see controller.Receptor_DestinoResource
 * @see model.Receptor_Destino
 * @see model.Receptor
 * @see model.Destino
 * 
 * @author Raízes Solidárias
 *
 */
public class Receptor_DestinoService {
	
	/**
	 * Verifica se um Receptor_Destino com os ID's especificados existe.
	 *
	 * @param id_usuario 	o ID do Receptor (Usuario).
	 * @param id_destino	o ID do Destino
	 * @return true se um Receptor_Destino com os ID's especificados existe, caso contrário, false.
	 */
	public static boolean validarIdsReceptor_Destino(int id_usuario, int id_destino) {
		return Receptor_DestinoDAO.buscarReceptor_DestinoPorIds(id_usuario, id_destino) != null;
	}
	
	/**
	 * Busca e retorna um Receptor_Destino com o ID do Receptor e o ID do Destino especificados.
	 *
	 * @param id_usuario 	o ID do Receptor (Usuario).
	 * @param id_destino  	o ID do Destino.
	 * @return true se um Receptor_Destino com o ID do Receptor e ID do Destino especificados existe, caso contrário, false.
	 */
	public static Receptor_Destino exibirReceptor_DestinoPorIds(int id_usuario, int id_destino) {
		return Receptor_DestinoDAO.buscarReceptor_DestinoPorIds(id_usuario, id_destino);
	}

	/**
	 * Atualiza um Receptor_Destino com as informações fornecidas.
	 *
	 * @param id_usuario_novo 	o ID do Receptor que será atualizado.
	 * @param id_usuario_antigo o ID do Receptor a ser atualizado.
	 * @param id_destino_novo	o ID do Destino que será atualizado.
	 * @param id_destino_antigo	o ID do Destino a ser atualizado.
	 * @return true se o Receptor_Destino foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarReceptor_Destino(int id_usuario_novo, int id_usuario_antigo, int id_destino_novo, int id_destino_antigo) {
		Receptor_Destino receptor_destino_atualizar = exibirReceptor_DestinoPorIds(id_usuario_antigo, id_destino_antigo);

		if (receptor_destino_atualizar == null || receptor_destino_atualizar.getDestino().getId_destino() != id_destino_antigo || receptor_destino_atualizar.getReceptor().getId_usuario() != id_usuario_antigo) {
			return false;
		} else {
			if (Receptor_DestinoDAO.atualizarReceptor_Destino(id_usuario_novo, id_usuario_antigo, id_destino_novo, id_destino_antigo))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Receptor_Destino.
	 *
	 * @param receptor_destino_novo o novo Receptor_Destino a ser cadastrado.
	 * @return o Receptor_Destino cadastrado.
	 */
	public static Receptor_Destino cadastrarReceptor_Destino(Receptor_Destino receptor_destino_novo) {
		return Receptor_DestinoDAO.cadastrarReceptor_Destino(receptor_destino_novo);
	}

	/**
	 * Exclui um Receptor_Destino pelos ID's do Receptor e do Destino.
	 *
	 * @param id_usuario 	o ID do Receptor do Receptor_Destino a ser excluído.
	 * @param id_destino	o ID do Destino do Receptor_Destino a ser excluído.
	 * @return true se o Receptor_Destino foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarReceptor_Destino(int id_usuario, int id_destino) {
		if (validarIdsReceptor_Destino(id_usuario, id_destino)) {
			return Receptor_DestinoDAO.deletarReceptor_Destino(id_usuario, id_destino);
		} else {
			return false;
		}
	}
}