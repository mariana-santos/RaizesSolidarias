package model;

import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa um alimento.
 *
 * A classe Alimento contém informações sobre o ID do alimento, o nome do alimento, o tempo de colheita,
 * a quantidade de irrigação, o preço do alimento e a quantidade de alimentos disponíveis.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see services.AlimentoService
 * @see dao.AlimentoDAO
 * @see controller.AlimentoResource
 *
 * @author Raízes Solidárias
 */
public class Alimento {
	
	/**
     * ID do Alimento.
     */
    @NotNull(message = "O ID do Alimento não pode ser nulo.")
    private int id_alimento;
    
    /**
     * Nome do Alimento.
     */
    @NotNull(message = "O Nome do Alimento não pode ser nulo.")
    private String nome_alimento;
    
    /**
     * Tempo de Colheita do Alimento.
     */
    @NotNull(message = "O Tempo de Colheira do Alimento não pode ser nulo.")
    private int tempo_colheita;
    
    /**
     * Quantidade de Irrigação do Alimento.
     */
    @NotNull(message = "A Quantidade de Irrigação do Alimento não pode ser nulo.")
    private int qtd_irrigacao;
    
    /**
     * Preço do Alimento.
     */
    private int preco_alimento;
    
    /**
     * Quantidade Disponível de Sementes do Alimento.
     */
    private int qtd_alimento;

    /**
     * Obtém o ID do alimento.
     *
     * @return O ID do alimento.
     */
    public int getId_alimento() {
        return id_alimento;
    }

    /**
     * Define o ID do alimento.
     *
     * @param id_alimento O ID do alimento a ser definido.
     */
    public void setId_alimento(int id_alimento) {
        this.id_alimento = id_alimento;
    }

    /**
     * Obtém o nome do alimento.
     *
     * @return O nome do alimento.
     */
    public String getNome_alimento() {
        return nome_alimento;
    }

    /**
     * Define o nome do alimento.
     *
     * @param nome_alimento O nome do alimento a ser definido.
     */
    public void setNome_alimento(String nome_alimento) {
        this.nome_alimento = nome_alimento;
    }

    /**
     * Obtém o tempo de colheita do alimento.
     *
     * @return O tempo de colheita do alimento.
     */
    public int getTempo_colheita() {
        return tempo_colheita;
    }

    /**
     * Define o tempo de colheita do alimento.
     *
     * @param tempo_colheita O tempo de colheita do alimento a ser definido.
     */
    public void setTempo_colheita(int tempo_colheita) {
        this.tempo_colheita = tempo_colheita;
    }

    /**
     * Obtém a quantidade de irrigação do alimento.
     *
     * @return A quantidade de irrigação do alimento.
     */
    public int getQtd_irrigacao() {
        return qtd_irrigacao;
    }

    /**
     * Define a quantidade de irrigação do alimento.
     *
     * @param qtd_irrigacao A quantidade de irrigação do alimento a ser definida.
     */
    public void setQtd_irrigacao(int qtd_irrigacao) {
        this.qtd_irrigacao = qtd_irrigacao;
    }

    /**
     * Obtém o preço do alimento.
     *
     * @return O preço do alimento.
     */
    public int getPreco_alimento() {
        return preco_alimento;
    }

    /**
     * Define o preço do alimento.
     *
     * @param preco_alimento O preço do alimento a ser definido.
     */
    public void setPreco_alimento(int preco_alimento) {
        this.preco_alimento = preco_alimento;
    }

    /**
     * Obtém a quantidade de alimentos disponíveis.
     *
     * @return A quantidade de alimentos disponíveis.
     */
    public int getQtd_alimento() {
        return qtd_alimento;
    }

    /**
     * Define a quantidade de alimentos disponíveis.
     *
     * @param qtd_alimento A quantidade de alimentos disponíveis a ser definida.
     */
    public void setQtd_alimento(int qtd_alimento) {
        this.qtd_alimento = qtd_alimento;
    }

    /**
     * Construtor padrão da classe Alimento.
     */
    public Alimento() {
        super();
    }

    /**
     * Construtor não padrão da classe Alimento.
     *
     * @param id_alimento       O ID do alimento (não pode ser nulo).
     * @param nome_alimento     O nome do alimento (não pode ser nulo).
     * @param tempo_colheita    O tempo de colheita do alimento (não pode ser nulo).
     * @param qtd_irrigacao     A quantidade de irrigação do alimento (não pode ser nulo).
     * @param preco_alimento    O preço do alimento.
     * @param qtd_alimento      A quantidade de alimentos disponíveis.
     */
    public Alimento(@NotNull(message = "O ID do Alimento não pode ser nulo.") int id_alimento,
                    @NotNull(message = "O Nome do Alimento não pode ser nulo.") String nome_alimento,
                    @NotNull(message = "O Tempo de Colheira do Alimento não pode ser nulo.") int tempo_colheita,
                    @NotNull(message = "A Quantidade de Irrigação do Alimento não pode ser nulo.") int qtd_irrigacao,
                    int preco_alimento, int qtd_alimento) {
        super();
        this.id_alimento = id_alimento;
        this.nome_alimento = nome_alimento;
        this.tempo_colheita = tempo_colheita;
        this.qtd_irrigacao = qtd_irrigacao;
        this.preco_alimento = preco_alimento;
        this.qtd_alimento = qtd_alimento;
    }

    /**
     * Sobrescrita do método hashCode para comparar objetos da classe Alimento.
     *
     * @return O valor do hashCode calculado para o objeto Alimento.
     */
    @Override
    public int hashCode() {
        return Objects.hash(id_alimento, nome_alimento, preco_alimento, qtd_alimento, qtd_irrigacao, tempo_colheita);
    }

    /**
     * Sobrescrita do método equals para comparar objetos da classe Alimento.
     *
     * @param obj O objeto a ser comparado com o Alimento atual.
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
        Alimento other = (Alimento) obj;
        return id_alimento == other.id_alimento && Objects.equals(nome_alimento, other.nome_alimento)
                && preco_alimento == other.preco_alimento && qtd_alimento == other.qtd_alimento
                && qtd_irrigacao == other.qtd_irrigacao && tempo_colheita == other.tempo_colheita;
    }

    /**
     * Sobrescrita do método toString para representar o objeto Alimento como uma String.
     *
     * @return Uma String que representa o objeto Alimento.
     */
    @Override
    public String toString() {
        return "Alimento [id_alimento=" + id_alimento + ", nome_alimento=" + nome_alimento + ", tempo_colheita="
                + tempo_colheita + ", qtd_irrigacao=" + qtd_irrigacao + ", preco_alimento=" + preco_alimento
                + ", qtd_alimento=" + qtd_alimento + "]";
    }
}