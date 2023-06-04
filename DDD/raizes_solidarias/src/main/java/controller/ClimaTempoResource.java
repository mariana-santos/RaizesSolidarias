package controller;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import services.ClimaTempoService;

@Path("/tempo")
public class ClimaTempoResource {

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response getPrevisaoTempoSaoPaulo() {
        ClimaTempoService climaTempoService = new ClimaTempoService();
        String previsaoTempo = null;

        try {
            previsaoTempo = climaTempoService.getPrevisaoTempoSaoPaulo();
        } catch (Exception e) {
            e.printStackTrace();
            return Response.serverError().build();
        }

        return Response.ok(previsaoTempo).build();
    }
}
