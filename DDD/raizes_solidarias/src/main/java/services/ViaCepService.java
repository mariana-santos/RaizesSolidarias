package services;

import java.io.IOException;
import org.apache.http.HttpEntity;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import com.google.gson.Gson;
import com.google.gson.JsonObject;

/**
 * Classe de serviços para API externa do ViaCep.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see controller.ViaCepResource
 * 
 * @author Raízes Solidárias
 *
 */
public class ViaCepService {
   
	/**
	 * Busca os dados do endereço de acordo com o CEP da API externa do ViaCep.
	 *
	 * @param cep o CEP a ser pesquisado.
	 * @return os dados do endereço de acordo com o CEP da API externa do ViaCep.
	 * @throws ClientProtocolException se ocorrer um erro de protocolo na comunicação com a API.
	 * @throws IOException se ocorrer um erro de I/O durante a comunicação com a API.
	 */
    public String getEndereco(String cep, String numero) throws ClientProtocolException, IOException {
       
        String endereco = null;
       
        HttpGet request = new HttpGet("https://viacep.com.br/ws/"+cep+"/json/");
       
        try(CloseableHttpClient httpClient = HttpClientBuilder.create().disableRedirectHandling().build();
               
                CloseableHttpResponse response = httpClient.execute(request)) {
           
            HttpEntity entity = response.getEntity();
           
            if(entity != null) {
               
                String result = EntityUtils.toString(entity);
               
                Gson gson = new Gson();
               
                JsonObject jsonObject = gson.fromJson(result, JsonObject.class);
                
                String logradouro = jsonObject.get("logradouro").getAsString();
                String bairro = jsonObject.get("bairro").getAsString();
                String localidade = jsonObject.get("localidade").getAsString();
                String uf = jsonObject.get("uf").getAsString();
                String cepRetornado = jsonObject.get("cep").getAsString();
                
                endereco = "{\"endereco\": \"" + logradouro + ", " + numero + " - " +  bairro + ", " + localidade + " - " + uf + " - " + cepRetornado + "\"}";
            }
        }
       
        return endereco;
    }
}
