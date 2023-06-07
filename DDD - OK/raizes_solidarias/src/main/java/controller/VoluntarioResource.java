package controller;

import java.net.URI;
import java.util.ArrayList;

import dao.VoluntarioDAO;
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
import model.Voluntario;
import services.VoluntarioService;

/**
 * Classe que representa o recurso de Voluntario (Usuario) do sistema.
 *
 * Esta classe define as operações CRUD para os Voluntarios, incluindo listar, buscar por ID,
 * cadastrar, atualizar e deletar Voluntarios.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see dao.VoluntarioDAO
 * @see services.VoluntarioService
 * @see model.Voluntario
 * @see model.Usuario
 *
 * @author Raízes Solidárias
 */
@Path("/voluntario")
public class VoluntarioResource {

	/**
	 * Recupera a lista de Voluntarios cadastrados no sistema.
	 *
	 * @return uma resposta contendo a lista de Voluntarios em formato JSON.
	 */
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public Response listarVoluntarios() {
		VoluntarioDAO repositorio = new VoluntarioDAO();
		ArrayList<Voluntario> retorno = repositorio.listarVoluntarios();
		ResponseBuilder response = Response.ok();
		response.entity(retorno);
		return response.build();
	}

	/**
	 * Recupera um Voluntario pelo seu ID.
	 *
	 * @param id_usuario o ID do Voluntario (Usuario) a ser buscado.
	 * @return uma resposta contendo o Voluntario em formato JSON.
	 */
	@GET
	@Path("/{id}")
	public Response exibirVoluntarioPorId(@PathParam("id") int id_usuario) {
		Voluntario voluntario_buscado = VoluntarioDAO.buscarVoluntarioPorId(id_usuario);

		if (voluntario_buscado != null) {
			ResponseBuilder response = Response.ok();
			response.entity(voluntario_buscado);
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível encontrar o VOLUNTARIO de id_usuario: " + id_usuario + "\"}");
			return response.build();
		}
	}

	/**
	 * Cadastra um novo Voluntario no sistema.
	 *
	 * @param voluntario_novo o objeto Voluntario contendo os dados do Voluntario (Usuario) a ser cadastrado.
	 * @return uma resposta contendo o Voluntario cadastrado em formato JSON.
	 */
	@POST
	@Consumes(MediaType.APPLICATION_JSON)
	public Response cadastrarVoluntario(@Valid Voluntario voluntario_novo) {
		Voluntario resp = VoluntarioService.cadastrarVoluntario(voluntario_novo);
		final URI voluntarioUri = UriBuilder.fromResource(VoluntarioResource.class).path("/voluntario/{id}")
				.build(resp.getId_usuario());
		ResponseBuilder response = Response.created(voluntarioUri);
		response.entity(resp);
		return response.build();
	}

	/**
	 * Atualiza os dados de um Voluntario existente no sistema.
	 *
	 * @param id_usuario o ID do Voluntario (Usuario) a ser atualizado.
	 * @param voluntario o objeto Voluntario contendo os novos dados do Voluntario.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@PUT
	@Path("/{id}")
	@Consumes(MediaType.APPLICATION_JSON)
	public Response atualizarVoluntario(@PathParam("id") int id_usuario, @Valid Voluntario voluntario) {
		if (VoluntarioService.atualizarVoluntario(id_usuario, voluntario)) {
			return Response.ok().build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível atualizar o VOLUNTARIO de id_usuario: " + id_usuario
							+ ". O id da URI e o ID do objeto JSON devem ser iguais e deve existir no banco de dados.\"}");
			return response.build();
		}
	}

	/**
	 * Remove um Voluntario do sistema.
	 *
	 * @param id_usuario o ID do Voluntario (Usuario) a ser removido.
	 * @return uma resposta indicando o sucesso ou falha da operação.
	 */
	@DELETE
	@Path("/{id}")
	public Response deletarVoluntario(@PathParam("id") int id_usuario) {
		if (VoluntarioService.deletarVoluntario(id_usuario)) {
			ResponseBuilder response = Response.noContent();
			return response.build();
		} else {
			System.out.println("Não foi possível remover o VOLUNTARIO: " + id_usuario);
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível remover o VOLUNTARIO de id_usuario: " + id_usuario + "\"}");
			return response.build();
		}
	}

	/**
	 * Valida o login de um voluntario.
	 *
	 * @param voluntarioLogin O objeto Voluntario contendo o email e a senha do voluntario a serem validados.
	 * @return A resposta HTTP com o status e o objeto Voluntario logado em caso de sucesso,
	 *         ou uma resposta HTTP de erro com uma mensagem em caso de falha na validação do login.
	 */
	@POST
	@Path("/login")
	@Consumes(MediaType.APPLICATION_JSON)
	public Response validarLoginVoluntario(Voluntario voluntarioLogin) {
		String email_usuario = voluntarioLogin.getEmail_usuario();
		String senha_usuario = voluntarioLogin.getSenha_usuario();

		try {
			Voluntario voluntario_logado = VoluntarioService.validarLoginVoluntario(email_usuario, senha_usuario);

			if (voluntario_logado != null) {
				ResponseBuilder response = Response.ok();
				response.entity(voluntario_logado);
				return response.build();
			} else {
				return Response.status(401).entity("{\"error\": \"Email e/ou senha incorretos.\"}").build();
			}
		} catch (NullPointerException e) {
			e.printStackTrace();
			return Response.status(401).entity("{\"error\": \"Email e/ou senha incorretos.\"}").build();
		}
	}
}
