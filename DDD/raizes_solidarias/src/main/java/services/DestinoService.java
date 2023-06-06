package services;

import dao.DestinoDAO;
import model.Destino;

/**
 * Classe de serviços para Destino.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Destino
 * @see dao.DestinoDAO
 * @see controller.DestinoResource
 * @see model.Destino
 * 
 * @author Raízes Solidárias
 *
 */
public class DestinoService {

	/**
	 * Verifica se um Destino com o ID especificado existe.
	 *
	 * @param id_destino o ID do Destino.
	 * @return true se um Destino com o ID especificado existe, caso contrário, false.
	 */
	public static boolean validarIdDestino(int id_destino) {
		return DestinoDAO.buscarDestinoPorId(id_destino) != null;
	}

	/**
	 * Busca e retorna um Destino pelo ID.
	 *
	 * @param id_destino o ID do Destino.
	 * @return o Destino correspondente ao ID, ou null se não encontrado.
	 */
	public static Destino exibirDestinoPorId(int id_destino) {
		return DestinoDAO.buscarDestinoPorId(id_destino);
	}

	/**
	 * Atualiza um Destino com as informações fornecidas.
	 *
	 * @param id_destino o ID do Destino a ser atualizado.
	 * @param destino o Destino com as novas informações.
	 * @return true se o Destino foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarDestino(int id_destino, Destino destino) {
		Destino usuario_atualizar = exibirDestinoPorId(id_destino);

		if (usuario_atualizar == null || usuario_atualizar.getId_destino() != destino.getId_destino()) {
			return false;
		} else {
			if (DestinoDAO.atualizarDestino(destino))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Destino.
	 *
	 * @param destino_novo o novo Destino a ser cadastrado.
	 * @return o Destino cadastrado.
	 */
	public static Destino cadastrarDestino(Destino destino_novo) {
		return DestinoDAO.cadastrarDestino(destino_novo);
	}

	/**
	 * Exclui um Destino pelo ID.
	 *
	 * @param id_destino o ID do Destino a ser excluído.
	 * @return true se o Destino foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarDestino(int id_destino) {
		if (validarIdDestino(id_destino)) {
			return DestinoDAO.deletarDestino(id_destino);
		} else {
			return false;
		}
	}
}