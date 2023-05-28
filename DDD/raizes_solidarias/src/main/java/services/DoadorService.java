package services;

import dao.DoadorDAO;
import model.Doador;

/**
 * Classe de serviços para Doador.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Doador
 * @see dao.DoadorDAO
 * @see controller.DoadorResource
 * @see model.Usuario
 * @see model.Doador
 * 
 * @author Raízes Solidárias
 *
 */
public class DoadorService {

	/**
	 * Verifica se um Doador com o ID especificado existe.
	 *
	 * @param id_usuario o ID do Usuario.
	 * @return true se um Doador com o ID especificado existe, caso contrário, false.
	 */
	public static boolean validarIdDoador(int id_usuario) {
		return DoadorDAO.buscarDoadorPorId(id_usuario) != null;
	}

	/**
	 * Busca e retorna um Doador pelo ID.
	 *
	 * @param id_usuario o ID do Usuario.
	 * @return o Doador correspondente ao ID, ou null se não encontrado.
	 */
	public static Doador exibirDoadorPorId(int id_usuario) {
		return DoadorDAO.buscarDoadorPorId(id_usuario);
	}

	/**
	 * Atualiza um Doador com as informações fornecidas.
	 *
	 * @param id_usuario o ID do Usuario a ser atualizado.
	 * @param usuario o Doador com as novas informações.
	 * @return true se o Doador foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarDoador(int id_usuario, Doador doador) {
		Doador usuario_atualizar = exibirDoadorPorId(id_usuario);

		if (usuario_atualizar == null || usuario_atualizar.getId_usuario() != doador.getId_usuario()) {
			return false;
		} else {
			if (DoadorDAO.atualizarDoador(doador))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Doador.
	 *
	 * @param doador_novo o novo Doador a ser cadastrado.
	 * @return o Doador cadastrado.
	 */
	public static Doador cadastrarDoador(Doador doador_novo) {
		return DoadorDAO.cadastrarDoador(doador_novo);
	}

	/**
	 * Exclui um Doador pelo ID.
	 *
	 * @param id_usuario o ID do Usuario a ser excluído.
	 * @return true se o Doador foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarDoador(int id_usuario) {
		if (validarIdDoador(id_usuario)) {
			return DoadorDAO.deletarDoador(id_usuario);
		} else {
			return false;
		}
	}
}