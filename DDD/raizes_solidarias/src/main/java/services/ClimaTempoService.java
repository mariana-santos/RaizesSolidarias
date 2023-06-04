package services;

import java.io.IOException;
import org.apache.http.HttpEntity;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

public class ClimaTempoService {

    private static final String API_KEY = "529d5a6f2eccf6a11d012c995797a521";

    public String getPrevisaoTempoSaoPaulo() throws ClientProtocolException, IOException {

        String previsaoTempo = null;

        HttpGet request = new HttpGet(
                "https://apiadvisor.climatempo.com.br/api/v1/weather/locale/3477/current?token=" + API_KEY);

        try (CloseableHttpClient httpClient = HttpClientBuilder.create().build();
                CloseableHttpResponse response = httpClient.execute(request)) {

            HttpEntity entity = response.getEntity();

            if (entity != null) {

                String result = EntityUtils.toString(entity);

                previsaoTempo = result;
            }
        }

        return previsaoTempo;
    }
}
