package model;

import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa a associação entre um Receptor e um Destino.
 * 
 * A classe Receptor_Destino contém uma instância de Receptor e uma instância de Destino, representando a relação entre um receptor que transporta uma carga para um determinado destino.
 *
 * @since 1.0
 * @version 1.0
 * 
 * @see services.Receptor_DestinoService
 * @see dao.Receptor_DestinoDAO
 * @see controller.Receptor_DestinoResource
 * @see model.Receptor
 * @see model.Destino
 * 
 * @author Raízes Solidárias
 * 
 */
public class Receptor_Destino {
	
	 /**
     * Receptor associado ao Destino.
     */
	@NotNull(message = "O Receptor do Receptor_Destino não pode ser nulo.")
	private Receptor receptor;
	
	 /**
     * Destino associado ao Receptor.
     */
	@NotNull(message = "O Destino do Receptor_Destino não pode ser nulo.")
	private Destino destino;
	
	/**
     * Obtém o Receptor associado ao Receptor_Destino.
     *
     * @return O Receptor associado ao Receptor_Destino.
     */
	public Receptor getReceptor() {
		return receptor;
	}
	
	/**
     * Define o Receptor associado ao Receptor_Destino.
     *
     * @param receptor O Receptor a ser associado ao Receptor_Destino.
     */
	public void setReceptor(Receptor receptor) {
		this.receptor = receptor;
	}
	
	/**
     * Obtém o Destino associado ao Receptor_Destino.
     *
     * @return O Destino associado ao Receptor_Destino.
     */
	public Destino getDestino() {
		return destino;
	}
	
	/**
     * Define o Destino associado ao Receptor_Destino.
     *
     * @param destino O Destino a ser associado ao Receptor_Destino.
     */
	public void setDestino(Destino destino) {
		this.destino = destino;
	}
	
	/**
     * Construtor padrão da classe Receptor_Destino.
     */
	public Receptor_Destino() {
		super();
	}
	
	/**
     * Construtor não padrão da classe Receptor_Destino.
     *
     * @param receptor O Receptor associado ao Receptor_Destino (não pode ser nulo).
     * @param destino O Destino associado ao Receptor_Destino (não pode ser nulo).
     */
	public Receptor_Destino(@NotNull(message = "O Receptor do Receptor_Destino não pode ser nulo.") Receptor receptor,
			@NotNull(message = "O Destino do Receptor_Destino não pode ser nulo.") Destino destino) {
		super();
		this.receptor = receptor;
		this.destino = destino;
	}
	
	/**
     * Sobrescrita do método hashCode para comparar objetos da classe Receptor_Destino.
     *
     * @return O valor do hashCode calculado para o objeto Receptor_Destino.
     */
	@Override
	public int hashCode() {
		return Objects.hash(destino, receptor);
	}
	
	/**
     * Sobrescrita do método equals para comparar objetos da classe Receptor_Destino.
     *
     * @param obj O objeto a ser comparado com o Receptor_Destino atual.
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
		Receptor_Destino other = (Receptor_Destino) obj;
		return Objects.equals(destino, other.destino) && Objects.equals(receptor, other.receptor);
	}
	
	/**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Receptor_Destino.
     *
     * @return Uma string representando o objeto Receptor_Destino.
     */
	@Override
	public String toString() {
		return "Receptor_Destino [receptor=" + receptor + ", destino=" + destino + "]";
	}
}