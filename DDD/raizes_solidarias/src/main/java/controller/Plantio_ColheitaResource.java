package controller;

import java.net.URI;
import java.util.ArrayList;

import dao.Plantio_ColheitaDAO;
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
import model.Plantio_Colheita;
import services.Plantio_ColheitaService;

@Path("/plantio_colheita")
public class Plantio_ColheitaResource {

	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public Response listarPlantio_Colheitas() {
		Plantio_ColheitaDAO repositorio = new Plantio_ColheitaDAO();
		ArrayList<Plantio_Colheita> retorno = repositorio.listarPlantio_Colheitas();
		ResponseBuilder response = Response.ok();
		response.entity(retorno);
		return response.build();
	}

	@GET
	@Path("/plantio/{id_plantio}")
	public Response exibirPlantio_ColheitaPorIdPlantio(@PathParam("id_plantio") int id_plantio) {
		Plantio_Colheita plantio_colheita_buscado = Plantio_ColheitaDAO.buscarPlantio_ColheitaPorIdPlantio(id_plantio);

		if (plantio_colheita_buscado != null) {
			ResponseBuilder response = Response.ok();
			response.entity(plantio_colheita_buscado);
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível encontrar o PLANTIO_COLHEITA de id_plantio: " + id_plantio + "\"}");
			return response.build();
		}
	}

	@GET
	@Path("/colheita/{id_colheita}")
	public Response exibirPlantio_ColheitaPorIdColheita(@PathParam("id_colheita") int id_colheita) {
		ArrayList<Plantio_Colheita> plantio_colheita_buscado = Plantio_ColheitaDAO
				.buscarPlantio_ColheitaPorIdColheita(id_colheita);

		if (plantio_colheita_buscado != null) {
			ResponseBuilder response = Response.ok();
			response.entity(plantio_colheita_buscado);
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível encontrar o PLANTIO_COLHEITA de id_colheita: " + id_colheita + "\"}");
			return response.build();
		}
	}

	@GET
	@Path("/{id_plantio}/{id_colheita}")
	public Response exibirPlantio_ColheitaPorIds(@PathParam("id_plantio") int id_plantio,
			@PathParam("id_colheita") int id_colheita) {
		Plantio_Colheita plantio_colheita_buscado = Plantio_ColheitaDAO.buscarPlantio_ColheitaPorIds(id_plantio,
				id_colheita);

		if (plantio_colheita_buscado != null) {
			ResponseBuilder response = Response.ok();
			response.entity(plantio_colheita_buscado);
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404).entity("{\"error\": \"Não foi possível encontrar o PLANTIO_COLHEITA de id_plantio: " + id_plantio + " e id_colheita: " + id_colheita + "\"}");
			return response.build();
		}
	}

	@POST
	@Consumes(MediaType.APPLICATION_JSON)
	public Response cadastrarPlantio_Colheita(@Valid Plantio_Colheita plantio_colheita_novo) {
		Plantio_Colheita resp = Plantio_ColheitaService.cadastrarPlantio_Colheita(plantio_colheita_novo);
		final URI plantio_colheitaUri = UriBuilder.fromResource(Plantio_ColheitaResource.class)
				.path("/plantio_colheita/{id}").build(resp);
		ResponseBuilder response = Response.created(plantio_colheitaUri);
		response.entity(resp);
		return response.build();
	}

	@PUT
	@Path("/{id_colheita}/{id_plantio_antigo}/{id_plantio_novo}")
	@Consumes(MediaType.APPLICATION_JSON)
	public Response atualizarPlantio_Colheita(@PathParam("id_plantio_novo") int id_plantio_novo,
			@PathParam("id_plantio_antigo") int id_plantio_antigo, @PathParam("id_colheita") int id_colheita) {
		if (Plantio_ColheitaService.atualizarPlantio_Colheita(id_plantio_novo, id_plantio_antigo, id_colheita)) {
			return Response.ok().build();
		} else {
			return Response.status(404)
					.entity("{\"error\": \"Não foi possível atualizar o PLANTIO_COLHEITA de id_colheita: " + id_colheita
							+ " e id_plantio: " + id_plantio_antigo
							+ ". O id da URI e o ID do objeto JSON devem ser iguais e deve existir no banco de dados.\"}")
					.build();
		}
	}

	@DELETE
	@Path("/{id_plantio}/{id_colheita}")
	public Response deletarPlantio_Colheita(@PathParam("id_plantio") int id_plantio,
			@PathParam("id_colheita") int id_colheita) {
		if (Plantio_ColheitaService.deletarPlantio_Colheita(id_plantio, id_colheita)) {
			ResponseBuilder response = Response.noContent();
			return response.build();
		} else {
			ResponseBuilder response = Response.status(404)
					.entity("{\"error\": \"Não foi possível remover o PLANTIO_COLHEITA de id_plantio: " + id_plantio
							+ " e id_colheita: " + id_colheita + "\"}");
			return response.build();
		}
	}
}
