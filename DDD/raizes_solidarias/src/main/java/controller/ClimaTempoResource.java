package controller;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import services.ClimaTempoService;

/**
 * Classe que representa a API do ClimaTempo no sistema.
 *
 * Esta classe representa a chamada da API externa do ClimaTempo, retornando os dados do tempo na cidade de São Paulo.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see ClimaTempoService
 *
 * @author Raízes Solidárias
 */
@Path("/tempo")
public class ClimaTempoResource {
	
	/**
	 * Recupera os dados do Tempo da API externa do ClimaTempo.
	 *
	 * @return uma resposta contendo os dados do tempo em formato JSON.
	 */
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
