package controller;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import services.ViaCepService;

/**
 * Classe que representa a API do ViaCep no sistema.
 *
 * Esta classe representa a chamada da API externa do ViaCep, retornando os dados do endereço de acordo com o CEP.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see ViaCepService
 *
 * @author Raízes Solidárias
 */
@Path("/endereco")
public class ViaCepResource {
   
	/**
	 * Recupera os dados do CEP da API externa do ViaCep.
	 *
	 * @param cep O CEP a ser pesquisado
	 * @return uma resposta contendo os dados do CEP em formato JSON.
	 */
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
