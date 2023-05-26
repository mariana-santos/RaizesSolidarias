package model;

import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa um Receptor da plataforma.
 * 
 * Esta classe herda da classe Usuario e contém atributos e métodos específicos para Receptores.
 * Os receptores são usuários registrados no sistema e possuem informações como quantidade de carga e endereço.
 *
 * @since 1.0
 * @version 1.0
 * 
 * @see services.ReceptorService
 * @see dao.ReceptorDao
 * @see controller.ReceptorResource
 * @see model.Usuario
 * 
 * @author Raízes Solidárias
 */ 
public class Receptor extends Usuario {
	
	/**
	 * Quantidade de carga do Receptor.
	 */
	@NotNull(message = "A quantidade de carga do Receptor não pode ser nula.")
	private int carga_receptor;
	
	/**
	 * Endereço do Receptor.
	 */
	@NotNull(message = "O endereço do Receptor não pode ser nulo.")
	private String endereco_receptor;

	/**
	 * Obtém a quantidade de carga do Receptor.
	 * 
	 * @return A quantidade de carga do Receptor.
	 */
	public int getCarga_receptor() {
		return carga_receptor;
	}

	/**
	 * Define a quantidade de carga do Receptor.
	 * 
	 * @param carga_receptor A quantidade de carga do Receptor.
	 */
	public void setCarga_receptor(int carga_receptor) {
		this.carga_receptor = carga_receptor;
	}

	/**
	 * Obtém o endereço do Receptor.
	 * 
	 * @return O endereço do Receptor.
	 */
	public String getEndereco_receptor() {
		return endereco_receptor;
	}

	/**
	 * Define o endereço do Receptor.
	 * 
	 * @param endereco_receptor O endereço do Receptor.
	 */
	public void setEndereco_receptor(String endereco_receptor) {
		this.endereco_receptor = endereco_receptor;
	}

	/**
	 * Construtor padrão da classe Receptor.
	 */
	public Receptor() {
		super();
	}

	/**
	 * Construtor não padrão da classe Receptor.
	 * 
	 * @param id_usuario      O ID do Usuário (não pode ser nulo).
	 * @param cpf_usuario     O CPF do Usuário (não pode ser nulo).
	 * @param nome_usuario    O Nome do Usuário (não pode ser nulo).
	 * @param email_usuario   O Email do Usuário (não pode ser nulo).
	 * @param cel_usuario     O Número de celular do Usuário (não pode ser nulo).
	 * @param senha_usuario   A Senha do Usuário (não pode ser nula).
	 */
	public Receptor(@NotNull(message = "O ID do Usuário não pode ser nulo.") int id_usuario, 
			@NotNull(message = "O CPF do Usuário não pode ser nulo.") String cpf_usuario,
			@NotNull(message = "O Nome do Usuário não pode ser nulo.") String nome_usuario,
			@NotNull(message = "O Email do Usuário não pode ser nulo.") String email_usuario,
			@NotNull(message = "O Celular do Usuário não pode ser nulo.") String cel_usuario,
			@NotNull(message = "A Senha do Usuário não pode ser nula.") String senha_usuario,
			@NotNull(message = "O Status do Usuário não pode ser nulo.") String status_usuario) {
		super(id_usuario, cpf_usuario, nome_usuario, email_usuario, cel_usuario, senha_usuario, status_usuario);
	}

	/**
	 * Construtor não padrão da classe Receptor.
	 * 
	 * @param carga_receptor A quantidade de carga do Receptor.
	 * @param endereco_receptor O endereço do Receptor.
	 */
	public Receptor(@NotNull(message = "A quantidade de carga do Receptor não pode ser nula.") int carga_receptor,
			@NotNull(message = "O endereço do Receptor não pode ser nulo.") String endereco_receptor) {
		super();
		this.carga_receptor = carga_receptor;
		this.endereco_receptor = endereco_receptor;
	}

	/**
     * Sobrescrita do método hashCode para comparar objetos da classe Receptor.
     *
     * @return O valor do hashCode calculado para o objeto Receptor.
     */
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = super.hashCode();
		result = prime * result + Objects.hash(carga_receptor, endereco_receptor);
		return result;
	}

	/**
     * Sobrescrita do método equals para comparar objetos da classe Receptor.
     *
     * @param obj O objeto a ser comparado com o Receptor atual.
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
		Receptor other = (Receptor) obj;
		return carga_receptor == other.carga_receptor && Objects.equals(endereco_receptor, other.endereco_receptor);
	}

	/**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Receptor.
     *
     * @return Uma string representando o objeto Receptor.
     */
	@Override
	public String toString() {
		return "Receptor [carga_receptor=" + carga_receptor + ", endereco_receptor=" + endereco_receptor + "]";
	}
}