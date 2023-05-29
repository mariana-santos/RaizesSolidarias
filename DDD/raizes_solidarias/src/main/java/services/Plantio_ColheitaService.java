package services;

import dao.Plantio_ColheitaDAO;
import model.Plantio_Colheita;

/**
 * Classe de serviços para Plantio_Colheita.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Plantio_Colheita
 * @see dao.Plantio_ColheitaDAO
 * @see controller.Plantio_ColheitaResource
 * @see model.Plantio_Colheita
 * @see model.Plantio
 * @see model.Colheita
 * 
 * @author Raízes Solidárias
 *
 */
public class Plantio_ColheitaService {
	
	/**
	 * Verifica se um Plantio_Colheita com os ID's especificados existe.
	 *
	 * @param id_plantio 	o ID do Plantio.
	 * @param id_colheita	o ID da Colheita
	 * @return true se um Plantio_Colheita com os ID's especificados existe, caso contrário, false.
	 */
	public static boolean validarIdsPlantio_Colheita(int id_plantio, int id_colheita) {
		return Plantio_ColheitaDAO.buscarPlantio_ColheitaPorIds(id_plantio, id_colheita) != null;
	}
	
	/**
	 * Busca e retorna um Plantio_Colheita com o ID do Plantio e o ID da Colheita especificados.
	 *
	 * @param id_plantio 	o ID do Plantio.
	 * @param id_colheita  	o ID da Colheita.
	 * @return true se um Plantio_Colheita com o ID do Plantio e ID da Colheita especificados existe, caso contrário, false.
	 */
	public static Plantio_Colheita exibirPlantio_ColheitaPorIds(int id_plantio, int id_colheita) {
		return Plantio_ColheitaDAO.buscarPlantio_ColheitaPorIds(id_plantio, id_colheita);
	}

	/**
	 * Atualiza um Plantio_Colheita com as informações fornecidas.
	 *
	 * @param id_plantio_novo 	o ID do Plantio que será atualizado.
	 * @param id_plantio_antigo o ID do Plantio a ser atualizado.
	 * @param id_colheita		o ID da Colheita a ser atualizada.
	 * @return true se o Plantio_Colheita foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarPlantio_Colheita(int id_plantio_novo, int id_plantio_antigo, int id_colheita) {
		Plantio_Colheita plantio_colheita_atualizar = exibirPlantio_ColheitaPorIds(id_plantio_antigo, id_colheita);

		if (plantio_colheita_atualizar == null || plantio_colheita_atualizar.getColheita().getId_colheita() != id_colheita || plantio_colheita_atualizar.getPlantio().getId_plantio() != id_plantio_antigo) {
			return false;
		} else {
			if (Plantio_ColheitaDAO.atualizarPlantio_Colheita(id_plantio_novo, id_plantio_antigo, id_colheita))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Plantio_Colheita.
	 *
	 * @param plantio_colheita_novo o novo Plantio_Colheita a ser cadastrado.
	 * @return o Plantio_Colheita cadastrado.
	 */
	public static Plantio_Colheita cadastrarPlantio_Colheita(Plantio_Colheita plantio_colheita_novo) {
		return Plantio_ColheitaDAO.cadastrarPlantio_Colheita(plantio_colheita_novo);
	}

	/**
	 * Exclui um Plantio_Colheita pelos ID's do Plantio e da Colheita.
	 *
	 * @param id_plantio 	o ID do Plantio do Plantio_Colheita a ser excluído.
	 * @param id_colheita 	o ID da Colheita do Plantio_Colheita a ser excluído.
	 * @return true se o Plantio_Colheita foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarPlantio_Colheita(int id_plantio, int id_colheita) {
		if (validarIdsPlantio_Colheita(id_plantio, id_colheita)) {
			return Plantio_ColheitaDAO.deletarPlantio_Colheita(id_plantio, id_colheita);
		} else {
			return false;
		}
	}
}