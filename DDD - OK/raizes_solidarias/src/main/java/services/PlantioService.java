package services;

import java.util.ArrayList;

import dao.PlantioDAO;
import model.Plantio;

/**
 * Classe de serviços para Plantio.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Plantio
 * @see dao.PlantioDAO
 * @see controller.PlantioResource
 * @see model.Plantio
 * 
 * @author Raízes Solidárias
 *
 */
public class PlantioService {

	/**
	 * Verifica se um Plantio com o ID especificado existe.
	 *
	 * @param id_plantio o ID do Plantio.
	 * @return true se um Plantio com o ID especificado existe, caso contrário, false.
	 */
	public static boolean validarIdPlantio(int id_plantio) {
		return PlantioDAO.buscarPlantioPorId(id_plantio) != null;
	}

	/**
	 * Busca e retorna um Plantio pelo ID.
	 *
	 * @param id_plantio o ID do Plantio.
	 * @return o Plantio correspondente ao ID, ou null se não encontrado.
	 */
	public static Plantio exibirPlantioPorId(int id_plantio) {
		return PlantioDAO.buscarPlantioPorId(id_plantio);
	}

	/**
	 * Atualiza um Plantio com as informações fornecidas.
	 *
	 * @param id_plantio o ID do Plantio a ser atualizado.
	 * @param plantio o Plantio com as novas informações.
	 * @return true se o Plantio foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarPlantio(int id_plantio, Plantio plantio) {
		Plantio usuario_atualizar = exibirPlantioPorId(id_plantio);

		if (usuario_atualizar == null || usuario_atualizar.getId_plantio() != plantio.getId_plantio()) {
			return false;
		} else {
			if (PlantioDAO.atualizarPlantio(plantio))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Plantio.
	 *
	 * @param plantio_novo o novo Plantio a ser cadastrado.
	 * @return o Plantio cadastrado.
	 */
	public static Plantio cadastrarPlantio(Plantio plantio_novo) {
		return PlantioDAO.cadastrarPlantio(plantio_novo);
	}
	
	/**
	 * Cadastra novos Plantios.
	 *
	 * @param plantios_novos o ArrayList de novos Plantios a ser cadastrado.
	 * @return o ArrayList de Plantios cadastrado.
	 */
	public static ArrayList<Plantio> cadastrarPlantios(ArrayList<Plantio> plantios_novos) {
		return PlantioDAO.cadastrarPlantios(plantios_novos);
	}

	/**
	 * Exclui um Plantio pelo ID.
	 *
	 * @param id_plantio o ID do Plantio a ser excluído.
	 * @return true se o Plantio foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarPlantio(int id_plantio) {
		if (validarIdPlantio(id_plantio)) {
			return PlantioDAO.deletarPlantio(id_plantio);
		} else {
			return false;
		}
	}
}