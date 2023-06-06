package model;

import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa a associação entre um Plantio e um Voluntario.
 * 
 * A classe Plantio_Voluntario contém uma instância de Plantio e uma instância de Voluntario, representando a relação entre um plantio realizado por um voluntário.
 *
 * @since 1.0
 * @version 1.0
 * 
 * @see services.Plantio_VoluntarioService
 * @see dao.Plantio_VoluntarioDAO
 * @see controller.Plantio_VoluntarioResource
 * @see model.Plantio
 * @see model.Voluntario
 * 
 * @author Raízes Solidárias
 * 
 */
public class Plantio_Voluntario {
	
	 /**
     * Plantio associado ao Voluntario.
     */
	@NotNull(message = "O Plantio do Plantio_Voluntario não pode ser nulo.")
	private Plantio plantio;
	
	 /**
     * Voluntario associado ao Plantio.
     */
	@NotNull(message = "O Voluntario do Plantio_Voluntario não pode ser nulo.")
	private Voluntario voluntario;

    /**
     * Obtém o Plantio associado ao Plantio_Voluntario.
     *
     * @return O Plantio associado ao Plantio_Voluntario.
     */
	public Plantio getPlantio() {
		return plantio;
	}

    /**
     * Define o Plantio associado ao Plantio_Voluntario.
     *
     * @param plantio O Plantio a ser associado ao Plantio_Voluntario.
     */
	public void setPlantio(Plantio plantio) {
		this.plantio = plantio;
	}

    /**
     * Obtém o Voluntario associado ao Plantio_Voluntario.
     *
     * @return O Voluntario associado ao Plantio_Voluntario.
     */
	public Voluntario getVoluntario() {
		return voluntario;
	}

    /**
     * Define o Voluntario associado ao Plantio_Voluntario.
     *
     * @param voluntario O Voluntario a ser associado ao Plantio_Voluntario.
     */
	public void setVoluntario(Voluntario voluntario) {
		this.voluntario = voluntario;
	}

    /**
     * Construtor padrão da classe Plantio_Voluntario.
     */
	public Plantio_Voluntario() {
		super();
	}

    /**
     * Construtor não padrão da classe Plantio_Voluntario.
     *
     * @param plantio O Plantio associado ao Plantio_Voluntario (não pode ser nulo).
     * @param voluntario O Voluntario associado ao Plantio_Voluntario (não pode ser nulo).
     */
	public Plantio_Voluntario(@NotNull(message = "O Plantio do Plantio_Voluntario não pode ser nulo.") Plantio plantio,
			@NotNull(message = "O Voluntario do Plantio_Voluntario não pode ser nulo.") Voluntario voluntario) {
		super();
		this.plantio = plantio;
		this.voluntario = voluntario;
	}

    /**
     * Sobrescrita do método hashCode para comparar objetos da classe Plantio_Voluntario.
     *
     * @return O valor do hashCode calculado para o objeto Plantio_Voluntario.
     */
	@Override
	public int hashCode() {
		return Objects.hash(plantio, voluntario);
	}

    /**
     * Sobrescrita do método equals para comparar objetos da classe Plantio_Voluntario.
     *
     * @param obj O objeto a ser comparado com o Plantio_Voluntario atual.
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
		Plantio_Voluntario other = (Plantio_Voluntario) obj;
		return Objects.equals(plantio, other.plantio) && Objects.equals(voluntario, other.voluntario);
	}

    /**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Plantio_Voluntario.
     *
     * @return Uma string representando o objeto Plantio_Voluntario.
     */
	@Override
	public String toString() {
		return "Plantio_Voluntario [plantio=" + plantio + ", voluntario=" + voluntario + "]";
	}
}