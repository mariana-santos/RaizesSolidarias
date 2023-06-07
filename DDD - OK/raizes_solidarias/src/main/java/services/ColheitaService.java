package services;

import dao.ColheitaDAO;
import model.Colheita;

/**
 * Classe de serviços para Colheita.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Colheita
 * @see dao.ColheitaDAO
 * @see controller.ColheitaResource
 * @see model.Colheita
 * 
 * @author Raízes Solidárias
 *
 */
public class ColheitaService {

	/**
	 * Verifica se uma Colheita com o ID especificado existe.
	 *
	 * @param id_colheita o ID da Colheita.
	 * @return true se uma Colheita com o ID especificado existe, caso contrário, false.
	 */
	public static boolean validarIdColheita(int id_colheita) {
		return ColheitaDAO.buscarColheitaPorId(id_colheita) != null;
	}

	/**
	 * Busca e retorna uma Colheita pelo ID.
	 *
	 * @param id_colheita o ID da Colheita.
	 * @return a Colheita correspondente ao ID, ou null se não encontrado.
	 */
	public static Colheita exibirColheitaPorId(int id_colheita) {
		return ColheitaDAO.buscarColheitaPorId(id_colheita);
	}

	/**
	 * Atualiza um Colheita com as informações fornecidas.
	 *
	 * @param id_colheita o ID do Colheita a ser atualizado.
	 * @param colheita o Colheita com as novas informações.
	 * @return true se a Colheita foi atualizada com sucesso, caso contrário, false.
	 */
	public static boolean atualizarColheita(int id_colheita, Colheita colheita) {
		Colheita usuario_atualizar = exibirColheitaPorId(id_colheita);

		if (usuario_atualizar == null || usuario_atualizar.getId_colheita() != colheita.getId_colheita()) {
			return false;
		} else {
			if (ColheitaDAO.atualizarColheita(colheita))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra uma nova Colheita.
	 *
	 * @param colheita_nova a nova Colheita a ser cadastrada.
	 * @return a Colheita cadastrada.
	 */
	public static Colheita cadastrarColheita(Colheita colheita_nova) {
		return ColheitaDAO.cadastrarColheita(colheita_nova);
	}

	/**
	 * Exclui um Colheita pelo ID.
	 *
	 * @param id_colheita o ID da Colheita a ser excluída.
	 * @return true se a Colheita foi excluída com sucesso, caso contrário, false.
	 */
	public static boolean deletarColheita(int id_colheita) {
		if (validarIdColheita(id_colheita)) {
			return ColheitaDAO.deletarColheita(id_colheita);
		} else {
			return false;
		}
	}
}