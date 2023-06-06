package controller;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

/**
 * Classe que representa o endpoint raiz do sistema.
 * 
 * Esta classe define o endpoint raiz ("/") e o método para retornar uma mensagem simples.
 * O método é anotado com as respectivas anotações JAX-RS para mapeamento de URLs e definição do tipo de mídia.
 * 
 * Métodos:
 * - getIt: retorna uma mensagem de boas-vindas.
 * 
 * Exemplo de uso:
 * 
 * Index index = new Index();
 * String message = index.getIt();
 * 
 * @since 1.0
 * @version 1.0
 * 
 * @author Raízes Solidárias
 * 
 */
@Path("/")
public class Index {

    /**
     * Retorna uma mensagem de boas-vindas.
     *
     * @return A mensagem "Raízes Solidárias!" como uma string simples.
     */
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String getIt() {
        return "Raízes Solidárias!";
    }
}