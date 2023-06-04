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

@Path("/voluntario")
public class VoluntarioResource {

	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public Response listarVoluntarios() {
		VoluntarioDAO repositorio = new VoluntarioDAO();
		ArrayList<Voluntario> retorno = repositorio.listarVoluntarios();
		ResponseBuilder response = Response.ok();
		response.entity(retorno);
		return response.build();
	}

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
