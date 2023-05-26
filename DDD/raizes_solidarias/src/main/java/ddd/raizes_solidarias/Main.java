package ddd.raizes_solidarias;

import java.io.IOException;
import java.net.URI;

import org.glassfish.grizzly.http.server.HttpServer;
import org.glassfish.jersey.grizzly2.httpserver.GrizzlyHttpServerFactory;
import org.glassfish.jersey.server.ResourceConfig;

import controller.CorsFilter;

/**
 * Classe principal da aplicação Raizes Solidárias.
 * 
 * Esta classe inicia o servidor Grizzly HTTP e expõe os recursos JAX-RS definidos nesta aplicação.
 * 
 * @version 1.0
 * @since 1.0
 * 
 * @author Raízes Solidárias
 * 
 */
public class Main {
    /**
     * URI base em que o servidor Grizzly HTTP irá escutar.
     */
    public static final String BASE_URI = "http://localhost:8080/";

    /**
     * Inicia o servidor Grizzly HTTP expondo os recursos JAX-RS definidos nesta aplicação.
     *
     * @return O servidor Grizzly HTTP.
     */
    public static HttpServer startServer() {
        // Cria uma configuração de recursos que escaneia por recursos e provedores JAX-RS
        // no pacote "controller"
        final ResourceConfig rc = new ResourceConfig().packages("controller");

        // Registra o CorsFilter
        rc.register(CorsFilter.class);

        // Cria e inicia uma nova instância do servidor Grizzly HTTP
        // expondo a aplicação Jersey em BASE_URI
        return GrizzlyHttpServerFactory.createHttpServer(URI.create(BASE_URI), rc);
    }

    /**
     * Método principal.
     *
     * @param args Argumentos de linha de comando.
     * @throws IOException Em caso de erro de entrada/saída.
     */
    public static void main(String[] args) throws IOException {
        final HttpServer server = startServer();
        System.out.println(String.format("Aplicação Jersey iniciada com endpoints disponíveis em %s%nPressione Ctrl-C para pará-la...", BASE_URI));
        System.in.read();
        server.shutdownNow();
    }
}
