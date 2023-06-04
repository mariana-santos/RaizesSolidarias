package controller;

import java.net.URI;
import java.util.ArrayList;

import dao.Plantio_VoluntarioDAO;
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
import model.Plantio_Voluntario;
import services.Plantio_VoluntarioService;

@Path("/plantio_voluntario")
public class Plantio_VoluntarioResource {

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response listarPlantio_Voluntarios() {
        Plantio_VoluntarioDAO repositorio = new Plantio_VoluntarioDAO();
        ArrayList<Plantio_Voluntario> retorno = repositorio.listarPlantio_Voluntarios();
        ResponseBuilder response = Response.ok();
        response.entity(retorno);
        return response.build();
    }

    @GET
    @Path("/plantio/{id_plantio}")
    public Response exibirPlantio_VoluntarioPorIdPlantio(@PathParam("id_plantio") int id_plantio) {
        ArrayList<Plantio_Voluntario> plantio_voluntario_buscado = Plantio_VoluntarioDAO
                .buscarPlantio_VoluntarioPorIdPlantio(id_plantio);

        if (plantio_voluntario_buscado != null) {
            ResponseBuilder response = Response.ok();
            response.entity(plantio_voluntario_buscado);
            return response.build();
        } else {
            ResponseBuilder response = Response.status(404)
                    .entity("{\"error\": \"Não foi possível encontrar o PLANTIO_VOLUNTARIO de id_plantio: "
                            + id_plantio + "\"}");
            return response.build();
        }
    }

    @GET
    @Path("/voluntario/{id_usuario}")
    public Response exibirPlantio_VoluntarioPorIdUsuario(@PathParam("id_usuario") int id_usuario) {
        ArrayList<Plantio_Voluntario> plantio_voluntario_buscado = Plantio_VoluntarioDAO
                .buscarPlantio_VoluntarioPorIdUsuario(id_usuario);

        if (plantio_voluntario_buscado != null) {
            ResponseBuilder response = Response.ok();
            response.entity(plantio_voluntario_buscado);
            return response.build();
        } else {
            ResponseBuilder response = Response.status(404)
                    .entity("{\"error\": \"Não foi possível encontrar o PLANTIO_VOLUNTARIO de id_usuario: "
                            + id_usuario + "\"}");
            return response.build();
        }
    }

    @GET
    @Path("/{id_plantio}/{id_usuario}")
    public Response exibirPlantio_VoluntarioPorIds(@PathParam("id_plantio") int id_plantio,
            @PathParam("id_usuario") int id_usuario) {
        Plantio_Voluntario plantio_voluntario_buscado = Plantio_VoluntarioDAO.buscarPlantio_VoluntarioPorIds(
                id_plantio, id_usuario);

        if (plantio_voluntario_buscado != null) {
            ResponseBuilder response = Response.ok();
            response.entity(plantio_voluntario_buscado);
            return response.build();
        } else {
            ResponseBuilder response = Response.status(404).entity("{\"error\": \"Não foi possível encontrar o PLANTIO_VOLUNTARIO de id_plantio: "
                    + id_plantio + " e id_usuario: " + id_usuario + "\"}");
            return response.build();
        }
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastrarPlantio_Voluntario(@Valid Plantio_Voluntario plantio_voluntario_novo) {
        Plantio_Voluntario resp = Plantio_VoluntarioService
                .cadastrarPlantio_Voluntario(plantio_voluntario_novo);
        final URI plantio_voluntarioUri = UriBuilder.fromResource(Plantio_VoluntarioResource.class)
                .path("/plantio_voluntario/{id}").build(resp);
        ResponseBuilder response = Response.created(plantio_voluntarioUri);
        response.entity(resp);
        return response.build();
    }

    @PUT
    @Path("/{id_plantio_antigo}-{id_usuario_antigo}/{id_plantio_novo}-{id_usuario_novo}")
    @Consumes(MediaType.APPLICATION_JSON)
    public Response atualizarPlantio_Voluntario(@PathParam("id_plantio_novo") int id_plantio_novo,
            @PathParam("id_plantio_antigo") int id_plantio_antigo,
            @PathParam("id_usuario_novo") int id_usuario_novo,
            @PathParam("id_usuario_antigo") int id_usuario_antigo) {
        if (Plantio_VoluntarioService.atualizarPlantio_Voluntario(id_plantio_novo, id_plantio_antigo,
                id_usuario_novo, id_usuario_antigo)) {
            return Response.ok().build();
        } else {
            return Response.status(404)
                    .entity("{\"error\": \"Não foi possível atualizar o PLANTIO_VOLUNTARIO de id_plantio: "
                            + id_plantio_antigo + " e id_usuario: " + id_usuario_antigo
                            + ". O id da URI e o ID do objeto JSON devem ser iguais e deve existir no banco de dados.\"}")
                    .build();
        }

    }

    @DELETE
    @Path("/{id_plantio}/{id_usuario}")
    public Response deletarPlantio_Voluntario(@PathParam("id_plantio") int id_plantio,
            @PathParam("id_usuario") int id_usuario) {
        if (Plantio_VoluntarioService.deletarPlantio_Voluntario(id_plantio, id_usuario)) {
            ResponseBuilder response = Response.noContent();
            return response.build();
        } else {
            System.out.println(
                    "Não foi possível remover o PLANTIO_VOLUNTARIO de id_plantio: " + id_plantio + " e id_usuario: "
                            + id_usuario);
            ResponseBuilder response = Response.status(404)
                    .entity("{\"error\": \"Não foi possível remover o PLANTIO_VOLUNTARIO de id_plantio: " + id_plantio
                            + " e id_usuario: " + id_usuario + "\"}");
            return response.build();
        }
    }
}
