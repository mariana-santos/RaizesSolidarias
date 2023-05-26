package model;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa um Doador da plataforma.
 * 
 * Esta classe herda da classe Usuario e contém atributos e métodos específicos para Doadores.
 * Os doadores são usuários registrados no sistema e possuem informações como nível e quantidade de moedas.
 *
 * @since 1.0
 * @version 1.0
 * 
 * @see services.DoadorService
 * @see dao.DoadorDao
 * @see controller.DoadorResource
 * @see model.Usuario
 * 
 * @author Raízes Solidárias
 */ 
public class Doador extends Usuario {
	
	/**
	 * Nível do Doador.
	 */
	@NotNull(message = "O nível do Doador não pode ser nulo.")
	private int nivel_doador;
	
	/**
	 * Quantidade de moedas do Doador.
	 */
	private int moedas_doador;
	
	/**
	 * Obtém o nível do Doador.
	 * 
	 * @return O nível do Doador.
	 */
	public int getNivel_doador() {
		return nivel_doador;
	}
	
	/**
	 * Define o nível do Doador.
	 * 
	 * @param nivel_doador O nível do Doador.
	 */
	public void setNivel_doador(int nivel_doador) {
		this.nivel_doador = nivel_doador;
	}
	
	/**
	 * Obtém a quantidade de moedas do Doador.
	 * 
	 * @return A quantidade de moedas do Doador.
	 */
	public int getMoedas_doador() {
		return moedas_doador;
	}
	
	/**
	 * Define a quantidade de moedas do Doador.
	 * 
	 * @param moedas_doador A quantidade de moedas do Doador.
	 */
	public void setMoedas_doador(int moedas_doador) {
		this.moedas_doador = moedas_doador;
	}
	
	/**
	 * Construtor padrão da classe Doador.
	 */
	public Doador() {
		super();
	}
	
	/**
	 * Construtor não padrão da classe Doador.
	 * 
	 * @param id_usuario      O ID do Usuário (não pode ser nulo).
	 * @param cpf_usuario     O CPF do Usuário (não pode ser nulo).
	 * @param nome_usuario    O Nome do Usuário (não pode ser nulo).
	 * @param email_usuario   O Email do Usuário (não pode ser nulo).
	 * @param cel_usuario     O Número de celular do Usuário (não pode ser nulo).
	 * @param senha_usuario   A Senha do Usuário (não pode ser nula).
	 */
	public Doador(@NotNull(message = "O ID do Usuário não pode ser nulo.") int id_usuario, 
			@NotNull(message = "O CPF do Usuário não pode ser nulo.") String cpf_usuario,
			@NotNull(message = "O Nome do Usuário não pode ser nulo.") String nome_usuario,
			@NotNull(message = "O Email do Usuário não pode ser nulo.") String email_usuario,
			@NotNull(message = "O Celular do Usuário não pode ser nulo.") String cel_usuario,
			@NotNull(message = "A senha do Usuário não pode ser nula.") String senha_usuario,
			@NotNull(message = "O Status do Usuário não pode ser nulo.") String status_usuario) {
		super(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario);
	}

	/**
	 * Construtor não padrão da classe Doador.
	 * 
	 * @param nivel_doador O nível do Doador.
	 * @param moedas_doador A quantidade de moedas do Doador.
	 */
	public Doador(@NotNull(message = "O nível do doador não pode ser nulo.") int nivel_doador, int moedas_doador) {
		super();
		this.nivel_doador = nivel_doador;
		this.moedas_doador = moedas_doador;
	}

	/**
     * Sobrescrita do método hashCode para comparar objetos da classe Doador.
     *
     * @return O valor do hashCode calculado para o objeto Doador.
     */
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + moedas_doador;
		result = prime * result + nivel_doador;
		return result;
	}
	
	/**
     * Sobrescrita do método equals para comparar objetos da classe Doador.
     *
     * @param obj O objeto a ser comparado com o Doador atual.
     * @return true se os objetos forem iguais, false caso contrário.
     */
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		Doador other = (Doador) obj;
		if (moedas_doador != other.moedas_doador)
			return false;
		if (nivel_doador != other.nivel_doador)
			return false;
		return true;
	}
	
	/**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Doador.
     *
     * @return Uma string representando o objeto Doador.
     */
	@Override
	public String toString() {
		return "Doador [nivel_doador=" + nivel_doador + ", moedas_doador=" + moedas_doador + "]";
	}
}