package controller;

import java.net.URI;
import java.util.ArrayList;

import dao.Receptor_DestinoDAO;
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
import model.Receptor_Destino;
import services.Receptor_DestinoService;

@Path("/receptor_destino")
public class Receptor_DestinoResource {

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response listarReceptor_Destinos() {
        Receptor_DestinoDAO repositorio = new Receptor_DestinoDAO();
        ArrayList<Receptor_Destino> retorno = repositorio.listarReceptor_Destinos();
        ResponseBuilder response = Response.ok();
        response.entity(retorno);
        return response.build();
    }

    @GET
    @Path("/receptor/{id_usuario}")
    public Response exibirReceptor_DestinoPorIdUsuario(@PathParam("id_usuario") int id_usuario) {
        ArrayList<Receptor_Destino> receptor_destino_buscado = Receptor_DestinoDAO
                .buscarReceptor_DestinoPorIdUsuario(id_usuario);

        if (receptor_destino_buscado != null) {
            ResponseBuilder response = Response.ok();
            response.entity(receptor_destino_buscado);
            return response.build();
        } else {
            ResponseBuilder response = Response.status(404)
                    .entity("{\"error\": \"Não foi possível encontrar o RECEPTOR_DESTINO de id_usuario: " + id_usuario
                            + "\"}");
            return response.build();
        }
    }

    @GET
    @Path("/destino/{id_destino}")
    public Response exibirReceptor_DestinoPorIdDestino(@PathParam("id_destino") int id_destino) {
        ArrayList<Receptor_Destino> receptor_destino_buscado = Receptor_DestinoDAO
                .buscarReceptor_DestinoPorIdDestino(id_destino);

        if (receptor_destino_buscado != null) {
            ResponseBuilder response = Response.ok();
            response.entity(receptor_destino_buscado);
            return response.build();
        } else {
            ResponseBuilder response = Response.status(404)
                    .entity("{\"error\": \"Não foi possível encontrar o RECEPTOR_DESTINO de id_destino: " + id_destino
                            + "\"}");
            return response.build();
        }
    }

    @GET
    @Path("/{id_usuario}/{id_destino}")
    public Response exibirReceptor_DestinoPorIds(@PathParam("id_usuario") int id_usuario,
            @PathParam("id_destino") int id_destino) {
        Receptor_Destino receptor_destino_buscado = Receptor_DestinoDAO.buscarReceptor_DestinoPorIds(id_usuario,
                id_destino);

        if (receptor_destino_buscado != null) {
            ResponseBuilder response = Response.ok();
            response.entity(receptor_destino_buscado);
            return response.build();
        } else {
            ResponseBuilder response = Response.status(404).entity("{\"error\": \"Não foi possível encontrar o RECEPTOR_DESTINO de id_usuario: " + id_usuario
                            + " e id_destino: " + id_destino + "\"}");
            return response.build();
        }
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastrarReceptor_Destino(@Valid Receptor_Destino receptor_destino_novo) {
        Receptor_Destino resp = Receptor_DestinoService.cadastrarReceptor_Destino(receptor_destino_novo);
        final URI receptor_destinoUri = UriBuilder.fromResource(Receptor_DestinoResource.class)
                .path("/receptor_destino/{id}").build(resp);
        ResponseBuilder response = Response.created(receptor_destinoUri);
        response.entity(resp);
        return response.build();
    }

    @PUT
    @Path("/{id_destino_antigo}-{id_usuario_antigo}/{id_destino_novo}-{id_usuario_novo}")
    @Consumes(MediaType.APPLICATION_JSON)
    public Response atualizarReceptor_Destino(@PathParam("id_destino_novo") int id_destino_novo,
            @PathParam("id_destino_antigo") int id_destino_antigo, @PathParam("id_usuario_novo") int id_usuario_novo,
            @PathParam("id_usuario_antigo") int id_usuario_antigo) {
        if (Receptor_DestinoService.atualizarReceptor_Destino(id_destino_novo, id_destino_antigo, id_usuario_novo,
                id_usuario_antigo)) {
            return Response.ok().build();
        } else {
            return Response.status(404).entity("{\"error\": \"Não foi possível atualizar o RECEPTOR_DESTINO de id_destino: "
                            + id_destino_antigo + " e id_usuario: " + id_usuario_antigo
                            + ". O id da URI e o ID do objeto JSON devem ser iguais e deve existir no banco de dados.\"}")
                    .build();
        }
    }

    @DELETE
    @Path("/{id_usuario}/{id_destino}")
    public Response deletarReceptor_Destino(@PathParam("id_usuario") int id_usuario,
            @PathParam("id_destino") int id_destino) {
        if (Receptor_DestinoService.deletarReceptor_Destino(id_usuario, id_destino)) {
            ResponseBuilder response = Response.noContent();
            return response.build();
        } else {
            System.out.println(
                    "Não foi possível remover o RECEPTOR_DESTINO de id_usuario: " + id_usuario + " e id_destino: "
                            + id_destino);
            ResponseBuilder response = Response.status(404)
                    .entity("{\"error\": \"Não foi possível remover o RECEPTOR_DESTINO de id_usuario: " + id_usuario
                            + " e id_destino: " + id_destino + "\"}");
            return response.build();
        }
    }
}
