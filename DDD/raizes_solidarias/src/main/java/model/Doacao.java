package model;

import java.sql.Date;
import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa uma Doacao realizada por um doador.
 *
 * A classe Doacao contém informações sobre a Doacao, como o identificador, o doador, a data da Doacao e a quantidade de moedas doadas.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see services.DoacaoService
 * @see dao.DoacaoDAO
 * @see controller.DoacaoResource
 * @see model.Doador
 * 
 * @author Raízes Solidárias
 */
public class Doacao {

	/**
     * O ID da Doacao.
     */
    @NotNull(message = "O ID da Doacao não pode ser nulo.")
    private int id_doacao;

    /**
     * O doador da Doacao.
     */
    @NotNull(message = "O Doador da Doacao não pode ser nulo.")
    private Doador doador;

    /**
     * A data da Doacao.
     */
    @NotNull(message = "A Data da Doacao não pode ser nula.")
    private Date data_doacao;

    /**
     * A quantidade de moedas da Doacao.
     */
    @NotNull(message = "A Quantidade de Moedas da Doacao não pode ser nula.")
    private int qtd_moedas_doacao;

    /**
     * Obtém o ID da Doacao.
     *
     * @return O ID da Doacao.
     */
    public int getId_doacao() {
        return id_doacao;
    }

    /**
     * Define o ID da Doacao.
     *
     * @param id_doacao O ID da Doacao a ser definido.
     */
    public void setId_doacao(int id_doacao) {
        this.id_doacao = id_doacao;
    }

    /**
     * Obtém o doador da Doacao.
     *
     * @return O doador da Doacao.
     */
    public Doador getDoador() {
        return doador;
    }

    /**
     * Define o doador da Doacao.
     *
     * @param doador O doador da Doacao a ser definido.
     */
    public void setDoador(Doador doador) {
        this.doador = doador;
    }

    /**
     * Obtém a data da Doacao.
     *
     * @return A data da Doacao.
     */
    public Date getData_doacao() {
        return data_doacao;
    }

    /**
     * Define a data da Doacao.
     *
     * @param data_doacao A data da Doacao a ser definida.
     */
    public void setData_doacao(Date data_doacao) {
        this.data_doacao = data_doacao;
    }

    /**
     * Obtém a quantidade de moedas da Doacao.
     *
     * @return A quantidade de moedas da Doacao.
     */
    public int getQtd_moedas_doacao() {
        return qtd_moedas_doacao;
    }

    /**
     * Define a quantidade de moedas da Doacao.
     *
     * @param qtd_moedas_doacao A quantidade de moedas da Doacao a ser definida.
     */
    public void setQtd_moedas_doacao(int qtd_moedas_doacao) {
        this.qtd_moedas_doacao = qtd_moedas_doacao;
    }

    /**
     * Construtor padrão da classe Doacao.
     */
    public Doacao() {
        super();
    }

    /**
     * Construtor da classe Doacao.
     *
     * @param id_doacao O ID da Doacao (não pode ser nulo).
     * @param doador O doador da Doacao (não pode ser nulo).
     * @param data_doacao A data da Doacao (não pode ser nula).
     * @param qtd_moedas_doacao A quantidade de moedas da Doacao (não pode ser nula).
     */
    public Doacao(@NotNull(message = "O ID da Doacao não pode ser nulo.") int id_doacao,
                  @NotNull(message = "O Doador da Doacao não pode ser nulo.") Doador doador,
                  @NotNull(message = "A Data da Doacao não pode ser nula.") Date data_doacao,
                  @NotNull(message = "A Quantidade de Moedas da Doacao não pode ser nula.") int qtd_moedas_doacao) {
        super();
        this.id_doacao = id_doacao;
        this.doador = doador;
        this.data_doacao = data_doacao;
        this.qtd_moedas_doacao = qtd_moedas_doacao;
    }

    /**
     * Sobrescrita do método hashCode para comparar objetos da classe Doacao.
     *
     * @return O valor do hashCode calculado para o objeto Doacao.
     */
    @Override
    public int hashCode() {
        return Objects.hash(data_doacao, doador, id_doacao, qtd_moedas_doacao);
    }

    /**
     * Sobrescrita do método equals para comparar objetos da classe Doacao.
     *
     * @param obj O objeto a ser comparado com a Doacao atual.
     * @return true se os objetos forem iguais, false caso contrário.
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Doacao other = (Doacao) obj;
        return Objects.equals(data_doacao, other.data_doacao) && Objects.equals(doador, other.doador)
                && id_doacao == other.id_doacao && qtd_moedas_doacao == other.qtd_moedas_doacao;
    }

    /**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Doacao.
     *
     * @return Uma string representando o objeto Doacao.
     */
    @Override
    public String toString() {
        return "Doacao [id_doacao=" + id_doacao + ", doador=" + doador + ", data_doacao=" + data_doacao
                + ", qtd_moedas_doacao=" + qtd_moedas_doacao + "]";
    }
}