package model;

import java.sql.Date;
import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa uma colheita.
 * 
 * A classe Colheita contém informações sobre a colheita, como o ID, a data e a descrição.
 *
 * @since 1.0
 * @version 1.0
 * 
 * @see services.ColheitaService
 * @see dao.ColheitaDAO
 * @see controller.ColheitaResource
 * 
 * @author Raízes Solidárias
 */
public class Colheita {
	
	/**
     * ID da colheita.
     */
	@NotNull(message = "O ID da Colheita não pode ser nulo.")
	private int id_colheita;
	
	/**
     * Data da colheita.
     */
	@NotNull(message = "A Data da Colheita não pode ser nula.")
	private Date data_colheita;
	
	/**
     * Descrição da colheita.
     */
	@NotNull(message = "A Descrição da Colheita não pode ser nula.")
	private String descricao_colheita;

    /**
     * Obtém o ID da colheita.
     *
     * @return O ID da colheita.
     */
	public int getId_colheita() {
		return id_colheita;
	}

    /**
     * Define o ID da colheita.
     *
     * @param id_colheita O ID da colheita a ser definido.
     */
	public void setId_colheita(int id_colheita) {
		this.id_colheita = id_colheita;
	}

    /**
     * Obtém a data da colheita.
     *
     * @return A data da colheita.
     */
	public Date getData_colheita() {
		return data_colheita;
	}

    /**
     * Define a data da colheita.
     *
     * @param data_colheita A data da colheita a ser definida.
     */
	public void setData_colheita(Date data_colheita) {
		this.data_colheita = data_colheita;
	}

    /**
     * Obtém a descrição da colheita.
     *
     * @return A descrição da colheita.
     */
	public String getDescricao_colheita() {
		return descricao_colheita;
	}

    /**
     * Define a descrição da colheita.
     *
     * @param descricao_colheita A descrição da colheita a ser definida.
     */
	public void setDescricao_colheita(String descricao_colheita) {
		this.descricao_colheita = descricao_colheita;
	}

    /**
     * Construtor padrão da classe Colheita.
     */
	public Colheita() {
		super();
	}

    /**
     * Construtor não padrão da classe Colheita.
     *
     * @param id_colheita O ID da colheita (não pode ser nulo).
     * @param data_colheita A data da colheita (não pode ser nula).
     * @param descricao_colheita A descrição da colheita (não pode ser nula).
     */
	public Colheita(@NotNull(message = "O ID da Colheita não pode ser nulo.") int id_colheita,
			@NotNull(message = "A Data da Colheita não pode ser nula.") Date data_colheita,
			@NotNull(message = "A Descrição da Colheita não pode ser nula.") String descricao_colheita) {
		super();
		this.id_colheita = id_colheita;
		this.data_colheita = data_colheita;
		this.descricao_colheita = descricao_colheita;
	}

    /**
     * Sobrescrita do método hashCode para comparar objetos da classe Colheita.
     *
     * @return O valor do hashCode calculado para o objeto Colheita.
     */
	@Override
	public int hashCode() {
		return Objects.hash(data_colheita, descricao_colheita, id_colheita);
	}

    /**
     * Sobrescrita do método equals para comparar objetos da classe Colheita.
     *
     * @param obj O objeto a ser comparado com a Colheita atual.
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
		Colheita other = (Colheita) obj;
		return Objects.equals(data_colheita, other.data_colheita)
				&& Objects.equals(descricao_colheita, other.descricao_colheita) && id_colheita == other.id_colheita;
	}

    /**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Colheita.
     *
     * @return Uma string representando o objeto Colheita.
     */
	@Override
	public String toString() {
		return "Colheita [id_colheita=" + id_colheita + ", data_colheita=" + data_colheita + ", descricao_colheita="
				+ descricao_colheita + "]";
	}
}