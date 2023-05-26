package model;

import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa a associação entre uma Colheita e um Voluntario.
 * 
 * A classe Colheita_Voluntario contém uma instância de Colheita e uma instância de Voluntario, representando a relação entre uma colheita realizada por um voluntário.
 *
 * @since 1.0
 * @version 1.0
 * 
 * @see services.Colheita_VoluntarioService
 * @see dao.Colheita_VoluntarioDao
 * @see controller.Colheita_VoluntarioResource
 * @see model.Colheita
 * @see model.Voluntario
 * 
 * @author Raízes Solidárias
 * 
 */
public class Colheita_Voluntario {
	 /**
     * Colheita associada ao Voluntario.
     */
	@NotNull(message = "A Colheita da Colheita_Voluntario não pode ser nula.")
	private Colheita colheita;
	
	 /**
     * Voluntario associado a Colheita.
     */
	@NotNull(message = "O Voluntario da Colheita_Voluntario não pode ser nulo.")
	private Voluntario voluntario;

    /**
     * Obtém a Colheita associada à Colheita_Voluntario.
     *
     * @return A Colheita associada à Colheita_Voluntario.
     */
	public Colheita getColheita() {
		return colheita;
	}

    /**
     * Define a Colheita associada à Colheita_Voluntario.
     *
     * @param colheita A Colheita a ser associada à Colheita_Voluntario.
     */
	public void setColheita(Colheita colheita) {
		this.colheita = colheita;
	}

    /**
     * Obtém o Voluntario associado à Colheita_Voluntario.
     *
     * @return O Voluntario associado à Colheita_Voluntario.
     */
	public Voluntario getVoluntario() {
		return voluntario;
	}

    /**
     * Define o Voluntario associado à Colheita_Voluntario.
     *
     * @param voluntario O Voluntario a ser associado à Colheita_Voluntario.
     */
	public void setVoluntario(Voluntario voluntario) {
		this.voluntario = voluntario;
	}

    /**
     * Construtor padrão da classe Colheita_Voluntario.
     */
	public Colheita_Voluntario() {
		super();
	}

    /**
     * Construtor não padrão da classe Colheita_Voluntario.
     *
     * @param colheita A Colheita associada à Colheita_Voluntario (não pode ser nula).
     * @param voluntario O Voluntario associado à Colheita_Voluntario (não pode ser nulo).
     */
	public Colheita_Voluntario(@NotNull(message = "A Colheita da Colheita_Voluntario não pode ser nula.") Colheita colheita,
			@NotNull(message = "O Voluntario da Colheita_Voluntario não pode ser nulo.") Voluntario voluntario) {
		super();
		this.colheita = colheita;
		this.voluntario = voluntario;
	}

    /**
     * Sobrescrita do método hashCode para comparar objetos da classe Colheita_Voluntario.
     *
     * @return O valor do hashCode calculado para o objeto Colheita_Voluntario.
     */
	@Override
	public int hashCode() {
		return Objects.hash(colheita, voluntario);
	}

    /**
     * Sobrescrita do método equals para comparar objetos da classe Colheita_Voluntario.
     *
     * @param obj O objeto a ser comparado com o Colheita_Voluntario atual.
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
		Colheita_Voluntario other = (Colheita_Voluntario) obj;
		return Objects.equals(colheita, other.colheita) && Objects.equals(voluntario, other.voluntario);
	}

    /**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Colheita_Voluntario.
     *
     * @return Uma string representando o objeto Colheita_Voluntario.
     */
	@Override
	public String toString() {
		return "Colheita_Voluntario [colheita=" + colheita + ", voluntario=" + voluntario + "]";
	}
}