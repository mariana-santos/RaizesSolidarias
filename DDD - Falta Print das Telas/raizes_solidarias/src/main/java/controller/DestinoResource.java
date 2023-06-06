package controller;

import java.net.URI;
import java.util.ArrayList;

import dao.DestinoDAO;
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
import model.Destino;
import services.DestinoService;

/**
 * Classe que representa o recurso de Destino do sistema.
 *
 * Esta classe define as operações CRUD para os Destinos, incluindo listar, buscar por ID,
 * cadastrar, atualizar e deletar Destinos.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see dao.DestinoDAO
 * @see services.DestinoService
 * @see model.Destino
 *
 * @author Raízes Solidárias
 */

@Path("/destino")
public class DestinoResource {
	
	/**
	 * Recupera a lista de Destinos cadastrados no sistema.
	 *
	 * @return uma resposta contendo a lista de Destinos em formato JSON.
	 */
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public Response listarDestinos() {
		DestinoDAO repositorio = new DestinoDAO();
		ArrayList<Destino> retorno = repositorio.listarDestinos();
		ResponseBuilder response = Response.ok();
		response.entity(retorno);
		return response.build();
	}
	
	/**
	 * Recupera um Destino pelo seu ID.
	 *
	 * @param id_destino o ID do Destino a ser buscado.
	 * @return uma resposta contendo o Destino em formato JSON.
	 */
	@GET
	@Path("/{id}")
	public Response exibirDestinoPorId(@PathParam("id") int id_destino) {
		Destino destino_buscado = DestinoDAO.buscarDestinoPorId(id_destino);

		if (destino_buscado != null) {
			ResponseBuilder response = Response.ok();
			response.entity(destino_buscado);
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível encontrar o DESTINO de id_destino: " + id_destino + "\"}");
			return response.build();
		}
	}
	
	/**
	 * Cadastra um novo Destino no sistema.
	 *
	 * @param destino_novo o objeto Destino contendo os dados do Destino a ser cadastrado.
	 * @return uma resposta contendo o Destino cadastrado em formato JSON.
	 */
	@POST
	@Consumes(MediaType.APPLICATION_JSON)
	public Response cadastrarDestino(@Valid Destino destino_novo) {
		Destino resp = DestinoService.cadastrarDestino(destino_novo);
		final URI destinoUri = UriBuilder.fromResource(DestinoResource.class).path("/destino/{id}")
				.build(resp.getId_destino());
		ResponseBuilder response = Response.created(destinoUri);
		response.entity(resp);
		return response.build();
	}
	
	/**
	 * Atualiza os dados de um Destino existente no sistema.
	 *
	 * @param id_destino o ID do Destino a ser atualizado.
	 * @param destino o objeto Destino contendo os novos dados do Destino.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@PUT
	@Path("/{id}")
	@Consumes(MediaType.APPLICATION_JSON)
	public Response atualizarDestino(@PathParam("id") int id_destino, @Valid Destino destino) {
		if (DestinoService.atualizarDestino(id_destino, destino)) {
			return Response.ok().build();
		} else {
			return Response.status(404)
					.entity("{\"error\": \"Não foi possível atualizar o DESTINO de id_destino: " + id_destino
							+ ". O id da URI e o ID do objeto JSON devem ser iguais e deve existir no banco de dados.\"}")
					.build();
		}

	}
	
	/**
	 * Remove um Destino do sistema.
	 *
	 * @param id_destino o ID do Destino a ser removido.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@DELETE
	@Path("/{id}")
	public Response deletarDestino(@PathParam("id") int id_destino) {
		if (DestinoService.deletarDestino(id_destino)) {
			ResponseBuilder response = Response.noContent();
			return response.build();
		} else {
			System.out.println("Não foi possível remover o DESTINO: " + id_destino);
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível remover o DESTINO de id_destino: " + id_destino + "\"}");
			return response.build();
		}
	}
}
