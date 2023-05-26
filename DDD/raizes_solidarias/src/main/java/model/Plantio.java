package model;

import java.sql.Date;
import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa o Plantio de um alimento.
 *
 * A classe Plantio contém informações sobre o ID do plantio, a data do plantio, o espaço que foi utilizado da plantação e o alimento que foi plantado.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see services.PlantioService
 * @see dao.PlantioDao
 * @see controller.PlantioResource
 *
 * @author Raízes Solidárias
 */
public class Plantio {
	
	/**
     * ID do Plantio.
     */
    @NotNull(message = "O ID do Plantio não pode ser nulo.")
    private int id_plantio;
    
    /**
     * Data do Plantio.
     */
    @NotNull(message = "A Data do Plantio não pode ser nula.")
    private Date data_plantio;
    
    /**
     * Espaço utilizado da plantação para o Plantio.
     */
    @NotNull(message = "O Espaço do Plantio não pode ser nulo.")
    private int espaco_plantio;
    
    /**
     * Alimento que foi plantado.
     */
    @NotNull(message = "O Alimento do Plantio não pode ser nulo.")
    private Alimento alimento;

    /**
     * Obtém o ID do plantio.
     *
     * @return O ID do plantio.
     */
    public int getId_plantio() {
        return id_plantio;
    }

    /**
     * Define o ID do plantio.
     *
     * @param id_plantio O ID do plantio a ser definido.
     */
    public void setId_plantio(int id_plantio) {
        this.id_plantio = id_plantio;
    }

    /**
     * Obtém a data do plantio.
     *
     * @return A data do plantio.
     */
    public Date getData_plantio() {
        return data_plantio;
    }

    /**
     * Define a data do plantio.
     *
     * @param data_plantio A data do plantio a ser definida.
     */
    public void setData_plantio(Date data_plantio) {
        this.data_plantio = data_plantio;
    }

    /**
     * Obtém o espaço do plantio.
     *
     * @return O espaço do plantio.
     */
    public int getEspaco_plantio() {
        return espaco_plantio;
    }

    /**
     * Define o espaço do plantio.
     *
     * @param espaco_plantio O espaço do plantio a ser definido.
     */
    public void setEspaco_plantio(int espaco_plantio) {
        this.espaco_plantio = espaco_plantio;
    }

    /**
     * Obtém o alimento do plantio.
     *
     * @return O alimento do plantio.
     */
    public Alimento getAlimento() {
        return alimento;
    }

    /**
     * Define o alimento do plantio.
     *
     * @param alimento O alimento do plantio a ser definido.
     */
    public void setAlimento(Alimento alimento) {
        this.alimento = alimento;
    }

    /**
     * Construtor padrão da classe Plantio.
     */
    public Plantio() {
        super();
    }

    /**
     * Construtor não padrão da classe Plantio.
     *
     * @param id_plantio       O ID do plantio (não pode ser nulo).
     * @param data_plantio     A data do plantio (não pode ser nula).
     * @param espaco_plantio   O espaço do plantio (não pode ser nulo).
     * @param alimento         O alimento do plantio (não pode ser nulo).
     */
    public Plantio(@NotNull(message = "O ID do Plantio não pode ser nulo.") int id_plantio,
                   @NotNull(message = "A Data do Plantio não pode ser nula.") Date data_plantio,
                   @NotNull(message = "O Espaço do Plantio não pode ser nulo.") int espaco_plantio,
                   @NotNull(message = "O Alimento do Plantio não pode ser nulo.") Alimento alimento) {
        super();
        this.id_plantio = id_plantio;
        this.data_plantio = data_plantio;
        this.espaco_plantio = espaco_plantio;
        this.alimento = alimento;
    }

    /**
     * Sobrescrita do método hashCode para gerar o código hash do objeto Plantio.
     *
     * @return O código hash calculado para o objeto Plantio.
     */
    @Override
    public int hashCode() {
        return Objects.hash(alimento, data_plantio, espaco_plantio, id_plantio);
    }

    /**
     * Sobrescrita do método equals para verificar se dois objetos Plantio são iguais.
     *
     * @param obj O objeto a ser comparado com o Plantio atual.
     * @return true se os objetos são iguais, false caso contrário.
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Plantio other = (Plantio) obj;
        return Objects.equals(alimento, other.alimento) && Objects.equals(data_plantio, other.data_plantio)
                && espaco_plantio == other.espaco_plantio && id_plantio == other.id_plantio;
    }

    /**
     * Sobrescrita do método toString para representar o objeto Plantio como uma String.
     *
     * @return Uma String que representa o objeto Plantio.
     */
    @Override
    public String toString() {
        return "Plantio [id_plantio=" + id_plantio + ", data_plantio=" + data_plantio + ", espaco_plantio="
                + espaco_plantio + ", alimento=" + alimento + "]";
    }
}