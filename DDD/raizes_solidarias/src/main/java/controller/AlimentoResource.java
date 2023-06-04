package controller;

import java.net.URI;
import java.util.ArrayList;

import dao.AlimentoDAO;
import jakarta.validation.Valid;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.DELETE;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.PUT;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.core.Response.ResponseBuilder;
import jakarta.ws.rs.core.UriBuilder;
import model.Alimento;
import services.AlimentoService;

/**
 * Classe que representa o recurso de Alimento do sistema.
 *
 * Esta classe define as operações CRUD para os Alimentos, incluindo listar, buscar por ID,
 * cadastrar, atualizar e deletar Alimentos.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see dao.AlimentoDAO
 * @see services.AlimentoService
 * @see model.Alimento
 *
 * @author Raízes Solidárias
 */

@Path("/alimento")
public class AlimentoResource {
	
	/**
	 * Recupera a lista de Alimentos cadastrados no sistema.
	 *
	 * @return uma resposta contendo a lista de Alimentos em formato JSON.
	 */
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public Response listarAlimentos() {
		AlimentoDAO repositorio = new AlimentoDAO();
		ArrayList<Alimento> retorno = repositorio.listarAlimentos();
		ResponseBuilder response = Response.ok();
		response.entity(retorno);
		return response.build();
	}
	
	/**
	 * Recupera um Alimento pelo seu ID.
	 *
	 * @param id_alimento o ID do Alimento a ser buscado.
	 * @return uma resposta contendo o Alimento em formato JSON.
	 */
	@GET
	@Path("/{id}")
	public Response exibirAlimentoPorId(@PathParam("id") int id_alimento) {
		Alimento alimento_buscado = AlimentoDAO.buscarAlimentoPorId(id_alimento);

		if (alimento_buscado != null) {
			ResponseBuilder response = Response.ok();
			response.entity(alimento_buscado);
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível encontrar o ALIMENTO de id_alimento: " + id_alimento+ "\"}");
			return response.build();
		}
	}
	
	/**
	 * Cadastra um novo Alimento no sistema.
	 *
	 * @param alimento_novo o objeto Alimento contendo os dados do Alimento a ser cadastrado.
	 * @return uma resposta contendo o Alimento cadastrado em formato JSON.
	 */
	@POST
	@Consumes(MediaType.APPLICATION_JSON)
	public Response cadastrarAlimento(@Valid Alimento alimento_novo) {
		Alimento resp = AlimentoService.cadastrarAlimento(alimento_novo);
		final URI alimentoUri = UriBuilder.fromResource(AlimentoResource.class).path("/alimento/{id}")
				.build(resp.getId_alimento());
		ResponseBuilder response = Response.created(alimentoUri);
		response.entity(resp);
		return response.build();
	}
	
	/**
	 * Atualiza os dados de um Alimento existente no sistema.
	 *
	 * @param id_alimento o ID do Alimento a ser atualizado.
	 * @param alimento o objeto Alimento contendo os novos dados do Alimento.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@PUT
	@Path("/{id}")
	@Consumes(MediaType.APPLICATION_JSON)
	public Response atualizarAlimento(@PathParam("id") int id_alimento, @Valid Alimento alimento) {
		if (AlimentoService.atualizarAlimento(id_alimento, alimento)) {
			return Response.ok().build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível atualizar o ALIMENTO de id_alimento: " + id_alimento
							+ ". O id da URI e o ID do objeto JSON devem ser iguais e deve existir no banco de dados.\"}");
			return response.build();
		}

	}
	
	/**
	 * Remove um Alimento do sistema.
	 *
	 * @param id_alimento o ID do Alimento a ser removido.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@DELETE
	@Path("/{id}")
	public Response deletarAlimento(@PathParam("id") int id_alimento) {
		if (AlimentoService.deletarAlimento(id_alimento)) {
			ResponseBuilder response = Response.noContent();
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível remover o ALIMENTO de id_alimento: " + id_alimento + "\"}");
			return response.build();
		}
	}
}
