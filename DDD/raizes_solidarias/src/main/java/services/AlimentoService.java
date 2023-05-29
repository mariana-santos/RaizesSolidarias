package services;

import dao.AlimentoDAO;
import model.Alimento;

/**
 * Classe de serviços para Alimento.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Alimento
 * @see dao.AlimentoDAO
 * @see controller.AlimentoResource
 * @see model.Alimento
 * 
 * @author Raízes Solidárias
 *
 */
public class AlimentoService {

	/**
	 * Verifica se um Alimento com o ID especificado existe.
	 *
	 * @param id_alimento o ID do Alimento.
	 * @return true se um Alimento com o ID especificado existe, caso contrário, false.
	 */
	public static boolean validarIdAlimento(int id_alimento) {
		return AlimentoDAO.buscarAlimentoPorId(id_alimento) != null;
	}

	/**
	 * Busca e retorna um Alimento pelo ID.
	 *
	 * @param id_alimento o ID do Alimento.
	 * @return o Alimento correspondente ao ID, ou null se não encontrado.
	 */
	public static Alimento exibirAlimentoPorId(int id_alimento) {
		return AlimentoDAO.buscarAlimentoPorId(id_alimento);
	}

	/**
	 * Atualiza um Alimento com as informações fornecidas.
	 *
	 * @param id_alimento o ID do Alimento a ser atualizado.
	 * @param usuario o Alimento com as novas informações.
	 * @return true se o Alimento foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarAlimento(int id_alimento, Alimento alimento) {
		Alimento usuario_atualizar = exibirAlimentoPorId(id_alimento);

		if (usuario_atualizar == null || usuario_atualizar.getId_alimento() != alimento.getId_alimento()) {
			return false;
		} else {
			if (AlimentoDAO.atualizarAlimento(alimento))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Alimento.
	 *
	 * @param alimento_novo o novo Alimento a ser cadastrado.
	 * @return o Alimento cadastrado.
	 */
	public static Alimento cadastrarAlimento(Alimento alimento_novo) {
		return AlimentoDAO.cadastrarAlimento(alimento_novo);
	}

	/**
	 * Exclui um Alimento pelo ID.
	 *
	 * @param id_alimento o ID do Alimento a ser excluído.
	 * @return true se o Alimento foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarAlimento(int id_alimento) {
		if (validarIdAlimento(id_alimento)) {
			return AlimentoDAO.deletarAlimento(id_alimento);
		} else {
			return false;
		}
	}
}