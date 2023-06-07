package model;

import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa as notícias da plataforma.
 *
 * A classe Noticias contém notícias sobre a fome mundial, solicitada pela matéria Responsive Web Development.
 *
 * @since 1.0
 * @version 1.0
 *
 * @author Raízes Solidárias
 */
public class Noticia {

    /**
     * ID da notícia.
     */
    @NotNull(message = "O ID da notícia não pode ser nulo.")
    private int id;

    /**
     * Título da notícia.
     */
    @NotNull(message = "O título da notícia não pode ser nulo.")
    private String titulo;

    /**
     * URL da imagem da notícia.
     */
    @NotNull(message = "A URL da imagem da notícia não pode ser nula.")
    private String imagem;

    /**
     * Resumo da notícia.
     */
    @NotNull(message = "O resumo da notícia não pode ser nulo.")
    private String resumo;

    /**
     * Conteúdo da notícia.
     */
    @NotNull(message = "O conteúdo da notícia não pode ser nulo.")
    private String conteudo;

    /**
     * Obtém o ID da notícia.
     *
     * @return O ID da notícia.
     */
    public int getId() {
        return id;
    }

    /**
     * Define o ID da notícia.
     *
     * @param id O ID da notícia a ser definido.
     */
    public void setId(int id) {
        this.id = id;
    }

    /**
     * Obtém o título da notícia.
     *
     * @return O título da notícia.
     */
    public String getTitulo() {
        return titulo;
    }

    /**
     * Define o título da notícia.
     *
     * @param titulo O título da notícia a ser definido.
     */
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    /**
     * Obtém a URL da imagem da notícia.
     *
     * @return A URL da imagem da notícia.
     */
    public String getImagem() {
        return imagem;
    }

    /**
     * Define a URL da imagem da notícia.
     *
     * @param imagem A URL da imagem da notícia a ser definida.
     */
    public void setImagem(String imagem) {
        this.imagem = imagem;
    }

    /**
     * Obtém o resumo da notícia.
     *
     * @return O resumo da notícia.
     */
    public String getResumo() {
        return resumo;
    }

    /**
     * Define o resumo da notícia.
     *
     * @param resumo O resumo da notícia a ser definido.
     */
    public void setResumo(String resumo) {
        this.resumo = resumo;
    }

    /**
     * Obtém o conteúdo da notícia.
     *
     * @return O conteúdo da notícia.
     */
    public String getConteudo() {
        return conteudo;
    }

    /**
     * Define o conteúdo da notícia.
     *
     * @param conteudo O conteúdo da notícia a ser definido.
     */
    public void setConteudo(String conteudo) {
        this.conteudo = conteudo;
    }
    
    /**
     * Construtor padrão da classe Noticia.
     */
    public Noticia() {
		super();
	}

	/**
     * Construtor da classe Noticia.
     *
     * @param id       O ID da notícia.
     * @param titulo   O título da notícia.
     * @param imagem   A URL da imagem da notícia.
     * @param resumo   O resumo da notícia.
     * @param conteudo O conteúdo da notícia.
     */
    public Noticia(@NotNull(message = "O ID da notícia não pode ser nulo.") int id,
                   @NotNull(message = "O título da notícia não pode ser nulo.") String titulo,
                   @NotNull(message = "A URL da imagem da notícia não pode ser nula.") String imagem,
                   @NotNull(message = "O resumo da notícia não pode ser nulo.") String resumo,
                   @NotNull(message = "O conteúdo da notícia não pode ser nulo.") String conteudo) {
        this.id = id;
        this.titulo = titulo;
        this.imagem = imagem;
        this.resumo = resumo;
        this.conteudo = conteudo;
    }

    /**
     * Sobrescrita do método equals para comparar objetos da classe Noticia.
     *
     * @param o O objeto a ser comparado com a Noticia atual.
     * @return true se os objetos forem iguais, false caso contrário.
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Noticia noticia = (Noticia) o;
        return id == noticia.id &&
                Objects.equals(titulo, noticia.titulo) &&
                Objects.equals(imagem, noticia.imagem) &&
                Objects.equals(resumo, noticia.resumo) &&
                Objects.equals(conteudo, noticia.conteudo);
    }

    /**
     * Sobrescrita do método hashCode para calcular o valor do hashCode do objeto Noticia.
     *
     * @return O valor do hashCode calculado para o objeto Noticia.
     */
    @Override
    public int hashCode() {
        return Objects.hash(id, titulo, imagem, resumo, conteudo);
    }

    /**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Noticia.
     *
     * @return Uma string representando o objeto Noticia.
     */
    @Override
    public String toString() {
        return "Noticia{" +
                "id=" + id +
                ", titulo='" + titulo + '\'' +
                ", imagem='" + imagem + '\'' +
                ", resumo='" + resumo + '\'' +
                ", conteudo='" + conteudo + '\'' +
                '}';
    }
}
