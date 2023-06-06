package ddd.raizes_solidarias;

import jakarta.ws.rs.client.Client;
import jakarta.ws.rs.client.ClientBuilder;
import jakarta.ws.rs.client.WebTarget;

import org.glassfish.grizzly.http.server.HttpServer;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * Classe de teste para a classe MyResource.
 */
public class MyResourceTest {

    private HttpServer server;
    private WebTarget target;

    /**
     * Configuração inicial do ambiente de teste.
     *
     * @throws Exception se ocorrer algum erro durante a configuração do ambiente de teste.
     */
    @BeforeEach
    public void setUp() throws Exception {
        // start the server
        server = Main.startServer();
        // create the client
        Client c = ClientBuilder.newClient();

        // uncomment the following line if you want to enable
        // support for JSON in the client (you also have to uncomment
        // dependency on jersey-media-json module in pom.xml and Main.startServer())
        // --
        // c.configuration().enable(new org.glassfish.jersey.media.json.JsonJaxbFeature());

        target = c.target(Main.BASE_URI);
    }

    /**
     * Finaliza o ambiente de teste.
     *
     * @throws Exception se ocorrer algum erro durante a finalização do ambiente de teste.
     */
    @SuppressWarnings("deprecation")
	@AfterEach
    public void tearDown() throws Exception {
        server.stop();
    }

    /**
     * Testa se a mensagem "Got it!" é enviada na resposta.
     */
    @Test
    public void testGetIt() {
        String responseMsg = target.path("myresource").request().get(String.class);
        assertEquals("Got it!", responseMsg);
    }
}
