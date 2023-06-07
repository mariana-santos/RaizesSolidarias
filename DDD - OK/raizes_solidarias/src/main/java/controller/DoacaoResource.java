package controller;

import java.net.URI;
import java.util.ArrayList;

import dao.DoacaoDAO;
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
import model.Doacao;
import services.DoacaoService;

/**
 * Classe que representa o recurso de Doacao do sistema.
 *
 * Esta classe define as operações CRUD para os Doacoes, incluindo listar, buscar por ID,
 * cadastrar, atualizar e deletar Doacoes.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see dao.DoacaoDAO
 * @see services.DoacaoService
 * @see model.Doacao
 *
 * @author Raízes Solidárias
 */

@Path("/doacao")
public class DoacaoResource {
	
	/**
	 * Recupera a lista de Doacoes cadastrados no sistema.
	 *
	 * @return uma resposta contendo a lista de Doacoes em formato JSON.
	 */
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public Response listarDoacoes() {
		DoacaoDAO repositorio = new DoacaoDAO();
		ArrayList<Doacao> retorno = repositorio.listarDoacoes();
		ResponseBuilder response = Response.ok();
		response.entity(retorno);
		return response.build();
	}
	
	/**
	 * Recupera um Doacao pelo seu ID.
	 *
	 * @param id_doacao o ID do Doacao a ser buscado.
	 * @return uma resposta contendo o Doacao em formato JSON.
	 */
	@GET
	@Path("/{id}")
	public Response exibirDoacaoPorId(@PathParam("id") int id_doacao) {
		Doacao doacao_buscado = DoacaoDAO.buscarDoacaoPorId(id_doacao);

		if (doacao_buscado != null) {
			ResponseBuilder response = Response.ok();
			response.entity(doacao_buscado);
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível encontrar o DOACAO de id_doacao: " + id_doacao + "\"}");
			return response.build();
		}
	}
	
	/**
	 * Cadastra um novo Doacao no sistema.
	 *
	 * @param doacao_novo o objeto Doacao contendo os dados do Doacao a ser cadastrado.
	 * @return uma resposta contendo o Doacao cadastrado em formato JSON.
	 */
	@POST
	@Consumes(MediaType.APPLICATION_JSON)
	public Response cadastrarDoacao(@Valid Doacao doacao_novo) {
		Doacao resp = DoacaoService.cadastrarDoacao(doacao_novo);
		final URI doacaoUri = UriBuilder.fromResource(DoacaoResource.class).path("/doacao/{id}")
				.build(resp.getId_doacao());
		ResponseBuilder response = Response.created(doacaoUri);
		response.entity(resp);
		return response.build();
	}
	
	/**
	 * Atualiza os dados de um Doacao existente no sistema.
	 *
	 * @param id_doacao o ID do Doacao a ser atualizado.
	 * @param doacao o objeto Doacao contendo os novos dados do Doacao.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@PUT
	@Path("/{id}")
	@Consumes(MediaType.APPLICATION_JSON)
	public Response atualizarDoacao(@PathParam("id") int id_doacao, @Valid Doacao doacao) {
		if (DoacaoService.atualizarDoacao(id_doacao, doacao)) {
			return Response.ok().build();
		} else {
			return Response.status(404)
					.entity("{\"error\": \"Não foi possível atualizar o DOACAO de id_doacao: " + id_doacao
							+ ". O id da URI e o ID do objeto JSON devem ser iguais e deve existir no banco de dados.\"}")
					.build();
		}

	}
	
	/**
	 * Remove um Doacao do sistema.
	 *
	 * @param id_doacao o ID do Doacao a ser removido.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@DELETE
	@Path("/{id}")
	public Response deletarDoacao(@PathParam("id") int id_doacao) {
		if (DoacaoService.deletarDoacao(id_doacao)) {
			ResponseBuilder response = Response.noContent();
			return response.build();
		} else {
			System.out.println("Não foi possível remover o DOACAO: " + id_doacao);
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível remover o DOACAO de id_doacao: " + id_doacao + "\"}");
			return response.build();
		}
	}
}
