package controller;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import services.ViaCepService;

@Path("/endereco")
public class ViaCepResource {
   
    @GET
    @Path("/{cep}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response getEnderecoByCep(@PathParam("cep") String cep) {
        ViaCepService viaCepService = new ViaCepService();
        String endereco = null;
       
        try {
            endereco = viaCepService.getEndereco(cep);
        } catch (Exception e) {
            e.printStackTrace();
            return Response.serverError().build();
        }
       
        return Response.ok(endereco).build();
    }
}
