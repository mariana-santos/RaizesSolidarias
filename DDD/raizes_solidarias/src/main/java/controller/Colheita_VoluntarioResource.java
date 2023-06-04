package controller;

import java.net.URI;
import java.util.ArrayList;

import dao.Colheita_VoluntarioDAO;
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
import model.Colheita_Voluntario;
import services.Colheita_VoluntarioService;

/**
 * Classe que representa o recurso de Colheita_Voluntario do sistema.
 *
 * Esta classe define as operações CRUD para os Colheita_Voluntarios, incluindo listar, buscar por ID,
 * cadastrar, atualizar e deletar Colheita_Voluntarios.
 * Os Colheita_Voluntarios são registros de voluntarios associados a colheitas e vice-versa.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see dao.Colheita_VoluntarioDAO
 * @see services.Colheita_VoluntarioService
 * @see model.Colheita_Voluntario
 * @author Raízes Solidárias
 */
@Path("/colheita_voluntario")
public class Colheita_VoluntarioResource {
	
	/**
	 * Recupera a lista de Colheita_Voluntarios cadastrados no sistema.
	 *
	 * @return uma resposta contendo a lista de Colheita_Voluntarios em formato JSON.
	 */
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public Response listarColheita_Voluntarios() {
		Colheita_VoluntarioDAO repositorio = new Colheita_VoluntarioDAO();
		ArrayList<Colheita_Voluntario> retorno = repositorio.listarColheita_Voluntarios();
		ResponseBuilder response = Response.ok();
		response.entity(retorno);
		return response.build();
	}
	
	/**
	 * Recupera um Colheita_Voluntario pelo seu ID Colheita e ID Usuario.
	 *
	 * @param id_colheita 	o ID da Colheita a ser buscado.
	 * @param id_usuario	o ID do Voluntario (Usuario) a ser buscado.
	 * @return uma resposta contendo o Colheita_Voluntario em formato JSON.
	 */
	@GET
	@Path("/{id_colheita}/{id_usuario}")
	public Response exibirColheita_VoluntarioPorIds(@PathParam("id_colheita") int id_colheita, @PathParam("id_usuario") int id_usuario) {
		Colheita_Voluntario colheita_voluntario_buscado = Colheita_VoluntarioDAO.buscarColheita_VoluntarioPorIds(id_colheita, id_usuario);

		if (colheita_voluntario_buscado != null) {
			ResponseBuilder response = Response.ok();
			response.entity(colheita_voluntario_buscado);
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível encontrar o COLHEITA_VOLUNTARIO de id_colheita: " + id_colheita + " e id_usuario: " + id_usuario + "\"}");
			return response.build();
		}
	}
	
	/**
	 * Cadastra um novo Colheita_Voluntario no sistema.
	 *
	 * @param colheita_voluntario_novo o objeto Colheita_Voluntario contendo os dados do Colheita_Voluntario a ser cadastrado.
	 * @return uma resposta contendo o Colheita_Voluntario cadastrado em formato JSON.
	 */
	@POST
	@Consumes(MediaType.APPLICATION_JSON)
	public Response cadastrarColheita_Voluntario(@Valid Colheita_Voluntario colheita_voluntario_novo) {
		Colheita_Voluntario resp = Colheita_VoluntarioService.cadastrarColheita_Voluntario(colheita_voluntario_novo);
		final URI colheita_voluntarioUri = UriBuilder.fromResource(Colheita_VoluntarioResource.class).path("/colheita_voluntario/{id}")
				.build(resp);
		ResponseBuilder response = Response.created(colheita_voluntarioUri);
		response.entity(resp);
		return response.build();
	}
	
	/**
	 * Atualiza os dados de um Colheita_Voluntario existente no sistema.
	 *
	 * @param id_usuario_novo	o ID do Voluntario (Usuario) a ser atualizado.
	 * @param id_usuario_antigo	o ID do Voluntario (Usuario) que será atualizado.
	 * @param id_colheita 		o ID da Colheita que será atualizado.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@PUT
	@Path("/{id_colheita}/{id_usuario_antigo}/{id_usuario_novo}")
	@Consumes(MediaType.APPLICATION_JSON)
	public Response atualizarColheita_Voluntario(@PathParam("id_usuario_novo") int id_usuario_novo, @PathParam("id_usuario_antigo") int id_usuario_antigo, @PathParam("id_colheita") int id_colheita) {
		if (Colheita_VoluntarioService.atualizarColheita_Voluntario(id_usuario_novo, id_usuario_antigo, id_colheita)) {
			return Response.ok().build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível atualizar o COLHEITA_VOLUNTARIO de id_colheita: " + id_colheita + " e id_usuario: " + id_usuario_antigo
							+ ". O id da URI e o ID do objeto JSON devem ser iguais e deve existir no banco de dados.\"}");
			return response.build();
		}

	}
	
	/**
	 * Remove um Colheita_Voluntario do sistema.
	 *
	 * @param id_colheita 	o ID da Colheita a ser removido.
	 * @param id_usuario	o ID do Voluntario (Usuario) a ser removido.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@DELETE
	@Path("/{id_colheita}/{id_usuario}")
	public Response deletarColheita_Voluntario(@PathParam("id_colheita") int id_colheita, @PathParam("id_usuario") int id_usuario) {
		if (Colheita_VoluntarioService.deletarColheita_Voluntario(id_colheita, id_usuario)) {
			ResponseBuilder response = Response.noContent();
			return response.build();
		} else {
			System.out.println("Não foi possível remover o COLHEITA_VOLUNTARIO de id_colheita: " + id_colheita + " e id_usuario: " + id_usuario);
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível remover o COLHEITA_VOLUNTARIO de id_colheita: " + id_colheita + " e id_usuario: " + id_usuario + "\"}");
			return response.build();
		}
	}
}
