package controller;

import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerResponseContext;
import jakarta.ws.rs.container.ContainerResponseFilter;
import jakarta.ws.rs.ext.Provider;

/**
 * Classe responsável por adicionar cabeçalhos CORS (Cross-Origin Resource Sharing) nas respostas HTTP.
 * 
 * Esta classe implementa a interface ContainerResponseFilter do JAX-RS, permitindo que seja registrada
 * como um provedor (Provider) no framework. Ela adiciona os cabeçalhos necessários para permitir a
 * solicitação de recursos de diferentes origens.
 * 
 * Métodos:
 * - filter: adiciona os cabeçalhos CORS na resposta HTTP.
 * 
 * Exemplo de uso:
 * 
 * CorsFilter filter = new CorsFilter();
 * filter.filter(requestContext, responseContext);
 * 
 * @since 1.0
 * @version 1.0
 * 
 * @see ContainerResponseFilter
 * @see Provider
 * 
 * @author Raízes Solidárias
 * 
 */
@Provider
public class CorsFilter implements ContainerResponseFilter {

    @Override
    public void filter(ContainerRequestContext requestContext, ContainerResponseContext responseContext) {
        responseContext.getHeaders().add("Access-Control-Allow-Origin", "*");
        responseContext.getHeaders().add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
        responseContext.getHeaders().add("Access-Control-Allow-Headers", "origin, content-type, accept");
    }
}