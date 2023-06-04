package controller;

import java.net.URI;
import java.util.ArrayList;

import dao.ReceptorDAO;
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
import model.Receptor;
import services.ReceptorService;

@Path("/receptor")
public class ReceptorResource {

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response listarReceptores() {
        ReceptorDAO repositorio = new ReceptorDAO();
        ArrayList<Receptor> retorno = repositorio.listarReceptores();
        ResponseBuilder response = Response.ok();
        response.entity(retorno);
        return response.build();
    }

    @GET
    @Path("/{id}")
    public Response exibirReceptorPorId(@PathParam("id") int id_usuario) {
        Receptor receptor_buscado = ReceptorDAO.buscarReceptorPorId(id_usuario);

        if (receptor_buscado != null) {
            ResponseBuilder response = Response.ok();
            response.entity(receptor_buscado);
            return response.build();
        } else {
            ResponseBuilder response = Response.status(404)
                    .entity("{\"error\": \"Não foi possível encontrar o RECEPTOR de id_usuario: " + id_usuario + "\"}");
            return response.build();
        }
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response cadastrarReceptor(@Valid Receptor receptor_novo) {
        Receptor resp = ReceptorService.cadastrarReceptor(receptor_novo);
        final URI receptorUri = UriBuilder.fromResource(ReceptorResource.class).path("/receptor/{id}")
                .build(resp.getId_usuario());
        ResponseBuilder response = Response.created(receptorUri);
        response.entity(resp);
        return response.build();
    }

    @PUT
    @Path("/{id}")
    @Consumes(MediaType.APPLICATION_JSON)
    public Response atualizarReceptor(@PathParam("id") int id_usuario, @Valid Receptor receptor) {
        if (ReceptorService.atualizarReceptor(id_usuario, receptor)) {
            return Response.ok().build();
        } else {
            ResponseBuilder response = Response.status(404)
                    .entity("{\"error\": \"Não foi possível atualizar o RECEPTOR de id_usuario: " + id_usuario
                            + ". O id da URI e o ID do objeto JSON devem ser iguais e deve existir no banco de dados.\"}");
            return response.build();
        }
    }

    @DELETE
    @Path("/{id}")
    public Response deletarReceptor(@PathParam("id") int id_usuario) {
        if (ReceptorService.deletarReceptor(id_usuario)) {
            ResponseBuilder response = Response.noContent();
            return response.build();
        } else {
            System.out.println("Não foi possível remover o RECEPTOR: " + id_usuario);
            ResponseBuilder response = Response.status(404)
                    .entity("{\"error\": \"Não foi possível remover o RECEPTOR de id_usuario: " + id_usuario + "\"}");
            return response.build();
        }
    }

    @POST
    @Path("/login")
    @Consumes(MediaType.APPLICATION_JSON)
    public Response validarLoginReceptor(Receptor receptorLogin) {
        String email_usuario = receptorLogin.getEmail_usuario();
        String senha_usuario = receptorLogin.getSenha_usuario();

        try {
            Receptor receptor_logado = ReceptorService.validarLoginReceptor(email_usuario, senha_usuario);

            if (receptor_logado != null) {
                ResponseBuilder response = Response.ok();
                response.entity(receptor_logado);
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
