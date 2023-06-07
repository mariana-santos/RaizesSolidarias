package controller;

import java.util.ArrayList;

import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.core.Response.ResponseBuilder;
import model.Noticia;

/**
 * Classe que representa o recurso de Notícia do sistema.
 *
 * Esta classe define e lista as notícias cadastradas no backend (apenas por obrigatoriedade de consumo de API criada para a matéria de Responsive Web Development)
 *
 * @since 1.0
 * @version 1.0
 * @see model.Noticia
 * @author Raízes Solidárias
 */
@Path("/noticia")
public class NoticiaResource {

    /**
     * Recupera a lista de Notícias cadastradas no sistema.
     *
     * @return uma resposta contendo a lista de Notícias em formato JSON.
     */
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response listarNoticias() {
        ArrayList<Noticia> retorno = new ArrayList<Noticia>();

        Noticia nova_noticia_1 = new Noticia();
        nova_noticia_1.setId(1);
        nova_noticia_1.setTitulo("Como as tecnologias inovadoras podem ajudar a alcançar a agricultura sustentável");
        nova_noticia_1.setImagem("https://img.freepik.com/fotos-gratis/agricultura-inteligente-iot-com-fundo-de-arvore-de-plantio-a-mao_53876-124626.jpg?w=1060&t=st=1685202611~exp=1685203211~hmac=33ed9e27e7b36423b7821e456b31319b0a50b258eee79725706da275dc8cfd59");
        nova_noticia_1.setResumo("A agricultura sustentável tem se tornado uma preocupação crescente em todo o mundo devido aos desafios ambientais e às demandas crescentes por alimentos. Nesse contexto, as tecnologias inovadoras têm desempenhado um papel crucial para impulsionar a transformação do setor agrícola, tornando-o mais sustentável e eficiente.\n\nEste artigo explora o impacto das tecnologias inovadoras na agricultura sustentável e destaca algumas das principais áreas em que essas tecnologias estão sendo aplicadas.");
        nova_noticia_1.setConteudo("Primeiramente, como a agricultura de precisão tem revolucionado a forma como os agricultores gerenciam suas terras?\n\nPor meio do uso de sensores, drones e sistemas de informações geográficas (SIG), os agricultores podem monitorar as condições do solo, a saúde das plantas e otimizar a aplicação de insumos agrícolas, como água e fertilizantes. Isso resulta em uma redução significativa do desperdício, maximização do rendimento das colheitas e redução do impacto ambiental.\n\nAlém disso, a automação e a robótica têm desempenhado um papel importante na agricultura sustentável. Os robôs agrícolas podem realizar tarefas como o plantio, a colheita e a aplicação de defensivos de forma mais eficiente e precisa do que os métodos tradicionais. Isso reduz a necessidade de mão de obra intensiva e minimiza o uso de produtos químicos prejudiciais ao meio ambiente.\n\nOutra tecnologia promissora é a utilização de inteligência artificial (IA) e aprendizado de máquina na agricultura. Com algoritmos avançados, os sistemas de IA podem analisar grandes volumes de dados, como padrões climáticos, histórico de colheitas e dados de mercado, para fornecer informações valiosas aos agricultores. Essas informações auxiliam na tomada de decisões mais informadas, permitindo o uso eficiente dos recursos, o planejamento da produção e a adoção de práticas sustentáveis.\n\nPor fim, o uso de tecnologias de sensoriamento remoto, como satélites e imagens de satélite, permite o monitoramento e a detecção de mudanças nas áreas agrícolas em tempo real. Isso é especialmente importante para o manejo sustentável de recursos naturais, como florestas e recursos hídricos. Os agricultores podem identificar áreas de desmatamento, erosão do solo e gerenciar de forma mais eficiente o uso da água.\n\nEm conclusão, as tecnologias inovadoras estão desempenhando um papel vital na busca pela agricultura sustentável. A agricultura de precisão, a automação, a inteligência artificial e o sensoriamento remoto são apenas algumas das tecnologias que estão transformando o setor agrícola. Ao adotar essas inovações, os agricultores podem reduzir o impacto ambiental, aumentar a eficiência e garantir a produção de alimentos de forma sustentável para as gerações futuras.");
        retorno.add(nova_noticia_1);

        Noticia nova_noticia_2 = new Noticia();
        nova_noticia_2.setId(2);
        nova_noticia_2.setTitulo("A importância da distribuição de alimentos e como as tecnologias inovadoras podem auxiliar");
        nova_noticia_2.setImagem("https://img.freepik.com/fotos-gratis/entregador-vestindo-uma-mascara-facial-e-segurando-uma-caixa-com-legumes_1268-14609.jpg?w=996&t=st=1685202693~exp=1685203293~hmac=ef901be096cb635493d34638668c982334d0f3f72f91c47952dd7af27160535e");
        nova_noticia_2.setResumo("A distribuição eficiente de alimentos desempenha um papel fundamental na garantia da segurança alimentar e no combate à fome em todo o mundo. No entanto, muitas vezes, enfrentamos desafios significativos no processo de distribuição, como perdas pós-colheita, desperdício de alimentos e falta de acesso em regiões remotas. Felizmente, as tecnologias inovadoras estão surgindo como soluções promissoras para melhorar a distribuição de alimentos e enfrentar esses desafios.\n\nEste artigo explora a importância da distribuição de alimentos e como as tecnologias inovadoras podem auxiliar nesse processo.");
        nova_noticia_2.setConteudo("Primeiramente, destaca-se o papel da cadeia de suprimentos inteligente, que utiliza tecnologias como Internet das Coisas (IoT), rastreamento por RFID e blockchain para monitorar o fluxo de alimentos desde a produção até o consumidor final. Isso permite a rastreabilidade completa dos alimentos, garantindo a segurança e qualidade dos produtos, além de facilitar a detecção rápida e eficiente de qualquer problema ao longo da cadeia.\n\nAlém disso, as tecnologias de logística avançada, como otimização de rotas, análise preditiva e inteligência artificial, desempenham um papel crucial na melhoria da eficiência da distribuição de alimentos. Essas tecnologias permitem uma melhor gestão dos estoques, redução de custos de transporte, planejamento estratégico de rotas e previsão de demanda. Isso resulta em uma distribuição mais rápida, precisa e econômica dos alimentos, evitando o desperdício e atendendo às necessidades dos consumidores de forma mais eficiente.\n\nOutra área de destaque é o uso de tecnologias inovadoras para enfrentar o desafio da distribuição em regiões remotas ou com infraestrutura precária. O uso de drones e veículos autônomos para entrega de alimentos pode superar as limitações geográficas e reduzir os custos associados ao transporte em áreas de difícil acesso. Além disso, as soluções de energia renovável, como painéis solares e sistemas de armazenamento de energia, podem fornecer energia confiável para instalações de armazenamento e distribuição em regiões com acesso limitado à rede elétrica.\n\nPor fim, as tecnologias inovadoras também estão impulsionando a criação de plataformas de compartilhamento e economia colaborativa, que permitem a redistribuição de alimentos excedentes de restaurantes, supermercados e outras fontes para organizações e comunidades necessitadas. Essas plataformas conectam doadores e receptores de alimentos de forma eficiente, reduzindo o desperdício e fornecendo alimentos nutritivos a pessoas em situação de vulnerabilidade.\n\nEm resumo, a distribuição eficiente de alimentos é crucial para combater a fome e garantir a segurança alimentar. As tecnologias inovadoras desempenham um papel fundamental nesse processo, melhorando a rastreabilidade, a eficiência logística, a acessibilidade em regiões remotas e a redistribuição de alimentos excedentes. Ao adotar essas tecnologias, podemos avançar em direção a um sistema de distribuição de alimentos mais sustentável, eficiente e inclusivo, beneficiando tanto os produtores quanto os consumidores.");
        retorno.add(nova_noticia_2);

        Noticia nova_noticia_3 = new Noticia();
        nova_noticia_3.setId(3);
        nova_noticia_3.setTitulo("Como a Raízes Solidárias consegue ajudar mais de 10 ONGs com sua horta solidária");
        nova_noticia_3.setImagem("https://img.freepik.com/fotos-gratis/mulher-com-um-chapeu-segurando-um-funil-e-trabalhando-em-um-jardim_1157-38529.jpg?w=996&t=st=1685202771~exp=1685203371~hmac=ccc77ab211c88d7cb8d63cd58f94891c8546e97cbe954a7fd1e7d1f178a3b957");
        nova_noticia_3.setResumo("A Raízes Solidárias é uma organização sem fins lucrativos que tem como objetivo combater a fome e promover a segurança alimentar por meio de uma horta solidária. Essa iniciativa inovadora tem impactado positivamente a vida de mais de 10 ONGs parceiras, fornecendo alimentos frescos e saudáveis para pessoas em situação de vulnerabilidade. Saiba mais sobre como a Raízes Solidárias consegue ajudar tantas ONGs com sua horta solidária.");
        nova_noticia_3.setConteudo("A horta solidária da Raízes Solidárias é um projeto que utiliza técnicas de agricultura urbana para o cultivo de alimentos frescos em áreas urbanas. A organização conta com uma equipe de voluntários dedicados que cuidam da horta e realizam todas as etapas do processo, desde o plantio até a colheita dos alimentos.\n\nOs alimentos produzidos na horta são destinados às ONGs parceiras da Raízes Solidárias, que atendem pessoas em situação de vulnerabilidade, como moradores de rua, famílias de baixa renda e crianças em situação de risco. A horta fornece uma variedade de alimentos, incluindo legumes, verduras e ervas frescas, contribuindo para uma alimentação mais saudável e nutritiva para essas pessoas.\n\nA Raízes Solidárias também realiza ações de educação alimentar, promovendo oficinas e palestras sobre a importância de uma alimentação saudável e sustentável. Além disso, a organização busca incentivar a participação da comunidade local, envolvendo moradores e empresas da região nas atividades da horta solidária.\n\nPara viabilizar esse projeto, a Raízes Solidárias conta com parcerias e doações de insumos e recursos. Empresas e indivíduos podem contribuir financeiramente, doar mudas, sementes, fertilizantes e outros materiais necessários para o funcionamento da horta. Essa rede de apoio é fundamental para manter e expandir o impacto da horta solidária.\n\nEm conclusão, a horta solidária da Raízes Solidárias é um exemplo inspirador de como a agricultura urbana pode ser utilizada para combater a fome e promover a segurança alimentar. Ao fornecer alimentos frescos e saudáveis para ONGs parceiras, a organização está impactando positivamente a vida de muitas pessoas em situação de vulnerabilidade. Com o apoio da comunidade e parcerias, a horta solidária da Raízes Solidárias pode continuar crescendo e ajudando ainda mais ONGs e pessoas necessitadas.");
        retorno.add(nova_noticia_3);

        ResponseBuilder response = Response.ok(retorno);
        return response.build();
    }
}
