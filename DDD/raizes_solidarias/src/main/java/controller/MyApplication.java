package controller;

import org.glassfish.jersey.server.ResourceConfig;

/**
 * Classe de configuração da aplicação.
 *
 * Esta classe estende a classe ResourceConfig do Jersey para configurar os recursos da aplicação.
 * Aqui, são definidos o pacote onde os recursos estão localizados e o registro de filtros, como o CorsFilter.
 *
 * Exemplo de uso:
 *
 * MyApplication application = new MyApplication();
 * application.packages("controller");
 * application.register(CorsFilter.class);
 *
 * @since 1.0
 * @version 1.0
 *
 * @see ResourceConfig
 * @see controller.CorsFilter
 * 
 * @author Raízes Solidárias
 */
public class MyApplication extends ResourceConfig {
    
    /**
     * Construtor da classe MyApplication.
     *
     * Configura o pacote onde os recursos estão localizados e registra o CorsFilter.
     */
    public MyApplication() {
        packages("controller");
        register(CorsFilter.class);
    }
}