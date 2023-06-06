package model;

import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa a associação entre um Plantio e uma Colheita.
 * 
 * A classe Plantio_Colheita contém uma instância de Plantio e uma instância de Colheita, representando a relação entre um plantio realizado e a colheita posterior.
 *
 * @since 1.0
 * @version 1.0
 * 
 * @see services.Plantio_ColheitaService
 * @see dao.Plantio_ColheitaDAO
 * @see controller.Plantio_ColheitaResource
 * @see model.Plantio
 * @see model.Colheita
 * 
 * @author Raízes Solidárias
 * 
 */
public class Plantio_Colheita {
	
	 /**
     * Plantio associado a Colheita.
     */
	@NotNull(message = "O Plantio da Plantio_Colheita não pode ser nulo.")
	private Plantio plantio;
	
	 /**
     * Colheita associada ao Plantio.
     */
	@NotNull(message = "A Colheita da Plantio_Colheita não pode ser nula.")
	private Colheita colheita;

    /**
     * Obtém o Plantio associado à Plantio_Colheita.
     *
     * @return O Plantio associado à Plantio_Colheita.
     */
	public Plantio getPlantio() {
		return plantio;
	}

    /**
     * Define o Plantio associado à Plantio_Colheita.
     *
     * @param plantio O Plantio a ser associado à Plantio_Colheita.
     */
	public void setPlantio(Plantio plantio) {
		this.plantio = plantio;
	}

    /**
     * Obtém a Colheita associada à Plantio_Colheita.
     *
     * @return A Colheita associada à Plantio_Colheita.
     */
	public Colheita getColheita() {
		return colheita;
	}

    /**
     * Define a Colheita associada à Plantio_Colheita.
     *
     * @param colheita A Colheita a ser associada à Plantio_Colheita.
     */
	public void setColheita(Colheita colheita) {
		this.colheita = colheita;
	}

    /**
     * Construtor padrão da classe Plantio_Colheita.
     */
	public Plantio_Colheita() {
		super();
	}

    /**
     * Construtor não padrão da classe Plantio_Colheita.
     *
     * @param plantio O Plantio associado à Plantio_Colheita (não pode ser nulo).
     * @param colheita A Colheita associada à Plantio_Colheita (não pode ser nula).
     */
	public Plantio_Colheita(@NotNull(message = "O Plantio da Plantio_Colheita não pode ser nulo.") Plantio plantio,
			@NotNull(message = "A Colheita da Plantio_Colheita não pode ser nula.") Colheita colheita) {
		super();
		this.plantio = plantio;
		this.colheita = colheita;
	}

    /**
     * Sobrescrita do método hashCode para comparar objetos da classe Plantio_Colheita.
     *
     * @return O valor do hashCode calculado para o objeto Plantio_Colheita.
     */
	@Override
	public int hashCode() {
		return Objects.hash(colheita, plantio);
	}

    /**
     * Sobrescrita do método equals para comparar objetos da classe Plantio_Colheita.
     *
     * @param obj O objeto a ser comparado com o Plantio_Colheita atual.
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
		Plantio_Colheita other = (Plantio_Colheita) obj;
		return Objects.equals(colheita, other.colheita) && Objects.equals(plantio, other.plantio);
	}

    /**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Plantio_Colheita.
     *
     * @return Uma string representando o objeto Plantio_Colheita.
     */
	@Override
	public String toString() {
		return "Plantio_Colheita [plantio=" + plantio + ", colheita=" + colheita + "]";
	}
}