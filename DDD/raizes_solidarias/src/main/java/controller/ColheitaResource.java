package controller;

import java.net.URI;
import java.util.ArrayList;

import dao.ColheitaDAO;
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
import model.Colheita;
import services.ColheitaService;

/**
 * Classe que representa o recurso de Colheita do sistema.
 *
 * Esta classe define as operações CRUD para os Colheitas, incluindo listar, buscar por ID,
 * cadastrar, atualizar e deletar Colheitas.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see dao.ColheitaDAO
 * @see services.ColheitaService
 * @see model.Colheita
 *
 * @author Raízes Solidárias
 */

@Path("/colheita")
public class ColheitaResource {
	
	/**
	 * Recupera a lista de Colheitas cadastrados no sistema.
	 *
	 * @return uma resposta contendo a lista de Colheitas em formato JSON.
	 */
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public Response listarColheitas() {
		ColheitaDAO repositorio = new ColheitaDAO();
		ArrayList<Colheita> retorno = repositorio.listarColheitas();
		ResponseBuilder response = Response.ok();
		response.entity(retorno);
		return response.build();
	}
	
	/**
	 * Recupera uma Colheita pelo seu ID.
	 *
	 * @param id_colheita o ID da Colheita a ser buscado.
	 * @return uma resposta contendo a Colheita em formato JSON.
	 */
	@GET
	@Path("/{id}")
	public Response exibirColheitaPorId(@PathParam("id") int id_colheita) {
		Colheita colheita_buscado = ColheitaDAO.buscarColheitaPorId(id_colheita);

		if (colheita_buscado != null) {
			ResponseBuilder response = Response.ok();
			response.entity(colheita_buscado);
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível encontrar o COLHEITA de id_colheita: " + id_colheita + "\"}");
			return response.build();
		}
	}
	
	/**
	 * Cadastra uma nova Colheita no sistema.
	 *
	 * @param colheita_nova o objeto Colheita contendo os dados da Colheita a ser cadastrada.
	 * @return uma resposta contendo a Colheita cadastrada em formato JSON.
	 */
	@POST
	@Consumes(MediaType.APPLICATION_JSON)
	public Response cadastrarColheita(@Valid Colheita colheita_nova) {
		Colheita resp = ColheitaService.cadastrarColheita(colheita_nova);
		final URI colheitaUri = UriBuilder.fromResource(ColheitaResource.class).path("/colheita/{id}")
				.build(resp.getId_colheita());
		ResponseBuilder response = Response.created(colheitaUri);
		response.entity(resp);
		return response.build();
	}
	
	/**
	 * Atualiza os dados de uma Colheita existente no sistema.
	 *
	 * @param id_colheita o ID da Colheita a ser atualizada.
	 * @param colheita o objeto Colheita contendo os novos dados da Colheita.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@PUT
	@Path("/{id}")
	@Consumes(MediaType.APPLICATION_JSON)
	public Response atualizarColheita(@PathParam("id") int id_colheita, @Valid Colheita colheita) {
		if (ColheitaService.atualizarColheita(id_colheita, colheita)) {
			return Response.ok().build();
		} else {
			return Response.status(404)
					.entity("{\"error\": \"Não foi possível atualizar o COLHEITA de id_colheita: " + id_colheita
							+ ". O id da URI e o ID do objeto JSON devem ser iguais e deve existir no banco de dados.\"}")
					.build();
		}

	}
	
	/**
	 * Remove uma Colheita do sistema.
	 *
	 * @param id_colheita o ID da Colheita a ser removida.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@DELETE
	@Path("/{id}")
	public Response deletarColheita(@PathParam("id") int id_colheita) {
		if (ColheitaService.deletarColheita(id_colheita)) {
			ResponseBuilder response = Response.noContent();
			return response.build();
		} else {
			System.out.println("Não foi possível remover o COLHEITA: " + id_colheita);
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível remover o COLHEITA de id_colheita: " + id_colheita + "\"}");
			return response.build();
		}
	}
}
