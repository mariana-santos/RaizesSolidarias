package services;

import dao.DoacaoDAO;
import model.Doacao;

/**
 * Classe de serviços para Doacao.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Doacao
 * @see dao.DoacaoDAO
 * @see controller.DoacaoResource
 * @see model.Doacao
 * 
 * @author Raízes Solidárias
 *
 */
public class DoacaoService {

	/**
	 * Verifica se um Doacao com o ID especificado existe.
	 *
	 * @param id_doacao o ID do Doacao.
	 * @return true se um Doacao com o ID especificado existe, caso contrário, false.
	 */
	public static boolean validarIdDoacao(int id_doacao) {
		return DoacaoDAO.buscarDoacaoPorId(id_doacao) != null;
	}

	/**
	 * Busca e retorna um Doacao pelo ID.
	 *
	 * @param id_doacao o ID do Doacao.
	 * @return o Doacao correspondente ao ID, ou null se não encontrado.
	 */
	public static Doacao exibirDoacaoPorId(int id_doacao) {
		return DoacaoDAO.buscarDoacaoPorId(id_doacao);
	}

	/**
	 * Atualiza um Doacao com as informações fornecidas.
	 *
	 * @param id_doacao o ID do Doacao a ser atualizado.
	 * @param usuario o Doacao com as novas informações.
	 * @return true se o Doacao foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarDoacao(int id_doacao, Doacao doacao) {
		Doacao usuario_atualizar = exibirDoacaoPorId(id_doacao);

		if (usuario_atualizar == null || usuario_atualizar.getId_doacao() != doacao.getId_doacao()) {
			return false;
		} else {
			if (DoacaoDAO.atualizarDoacao(doacao))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Doacao.
	 *
	 * @param doacao_novo o novo Doacao a ser cadastrado.
	 * @return o Doacao cadastrado.
	 */
	public static Doacao cadastrarDoacao(Doacao doacao_novo) {
		return DoacaoDAO.cadastrarDoacao(doacao_novo);
	}

	/**
	 * Exclui um Doacao pelo ID.
	 *
	 * @param id_doacao o ID do Doacao a ser excluído.
	 * @return true se o Doacao foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarDoacao(int id_doacao) {
		if (validarIdDoacao(id_doacao)) {
			return DoacaoDAO.deletarDoacao(id_doacao);
		} else {
			return false;
		}
	}
}