package model;

import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa um Destino a ser levada a carga de alimentos.
 * 
 * A classe Destino contém informações do destino, como o seu id, endereço, pessoa responsável por receber a carga, celular de contato e quantidade de dependentes.
 *
 * @since 1.0
 * @version 1.0
 * 
 * @see services.DestinoService
 * @see dao.DestinoDao
 * @see controller.DestinoResource
 * @see model.Receptor
 * 
 * @author Raízes Solidárias
 */
public class Destino {
	
	/**
     * ID do Destino.
     */
	@NotNull(message = "O ID do Destino não pode ser nulo.")
	private int id_destino;
	
	/**
     * Endereço do Destino.
     */
	@NotNull(message = "O Endereço do Destino não pode ser nulo.")
	private String endereco_destino;
	
	/**
     * Responsável pelo recebimento da carga no Destino.
     */
	@NotNull(message = "O Responsável do Destino não pode ser nulo.")
	private String responsavel_destino;
	
	/**
     * Celular do Destino.
     */
	@NotNull(message = "O Celular do Destino não pode ser nulo.")
	private String cel_destino;
	
	/**
     * Quantidade de dependentes do Destino.
     */
	@NotNull(message = "A Quantidade de Dependentes do Destino não pode ser nulo.")
	private int qtd_dependentes_destino;

	/**
     * Obtém o ID do Destino.
     *
     * @return O ID do Destino.
     */
	public int getId_destino() {
		return id_destino;
	}

	/**
     * Define o ID do Destino.
     *
     * @param id_destino O ID do Destino a ser definido.
     */
	public void setId_destino(int id_destino) {
		this.id_destino = id_destino;
	}

	/**
     * Obtém o endereço do Destino.
     *
     * @return O endereço do Destino.
     */
	public String getEndereco_destino() {
		return endereco_destino;
	}

	/**
     * Define o endereço do Destino.
     *
     * @param endereco_destino O endereço do Destino a ser definido.
     */
	public void setEndereco_destino(String endereco_destino) {
		this.endereco_destino = endereco_destino;
	}

	/**
     * Obtém o responsável pelo recebimento da carga no Destino.
     *
     * @return O responsável pelo recebimento da carga no Destino.
     */
	public String getResponsavel_destino() {
		return responsavel_destino;
	}

	/**
     * Define o responsável pelo recebimento da carga no Destino.
     *
     * @param responsavel_destino O responsável pelo recebimento da carga no Destino a ser definido.
     */
	public void setResponsavel_destino(String responsavel_destino) {
		this.responsavel_destino = responsavel_destino;
	}

	/**
     * Obtém o celular do Destino.
     *
     * @return O celular do Destino.
     */
	public String getCel_destino() {
		return cel_destino;
	}

	/**
     * Define o celular do Destino.
     *
     * @param cel_destino O celular do Destino a ser definido.
     */
	public void setCel_destino(String cel_destino) {
		this.cel_destino = cel_destino;
	}

	/**
     * Obtém a quantidade de dependentes do Destino.
     *
     * @return A quantidade de dependentes do Destino.
     */
	public int getQtd_dependentes_destino() {
		return qtd_dependentes_destino;
	}

	/**
     * Define a quantidade de dependentes do Destino.
     *
     * @param qtd_dependentes_destino A quantidade de dependentes do Destino a ser definida.
     */
	public void setQtd_dependentes_destino(int qtd_dependentes_destino) {
		this.qtd_dependentes_destino = qtd_dependentes_destino;
	}

	/**
     * Construtor padrão da classe Destino.
     */
	public Destino() {
		super();
	}

	/**
     * Construtor não padrão da classe Destino.
     *
     * @param id_destino O ID do Destino (não pode ser nulo).
     * @param endereco_destino O endereço do Destino (não pode ser nulo).
     * @param responsavel_destino O responsável pelo recebimento da carga no Destino (não pode ser nulo).
     * @param cel_destino O celular do Destino (não pode ser nulo).
     * @param qtd_dependentes_destino A quantidade de dependentes do Destino (não pode ser nulo).
     */
	public Destino(@NotNull(message = "O ID do Destino não pode ser nulo.") int id_destino,
			@NotNull(message = "O Endereço do Destino não pode ser nulo.") String endereco_destino,
			@NotNull(message = "O Responsável do Destino não pode ser nulo.") String responsavel_destino,
			@NotNull(message = "O Celular do Destino não pode ser nulo.") String cel_destino,
			@NotNull(message = "A Quantidade de Dependentes do Destino não pode ser nulo.") int qtd_dependentes_destino) {
		super();
		this.id_destino = id_destino;
		this.endereco_destino = endereco_destino;
		this.responsavel_destino = responsavel_destino;
		this.cel_destino = cel_destino;
		this.qtd_dependentes_destino = qtd_dependentes_destino;
	}

	/**
     * Sobrescrita do método hashCode para comparar objetos da classe Destino.
     *
     * @return O valor do hashCode calculado para o objeto Destino.
     */
	@Override
	public int hashCode() {
		return Objects.hash(cel_destino, endereco_destino, id_destino, qtd_dependentes_destino, responsavel_destino);
	}

	/**
     * Sobrescrita do método equals para comparar objetos da classe Destino.
     *
     * @param obj O objeto a ser comparado com o Destino atual.
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
		Destino other = (Destino) obj;
		return Objects.equals(cel_destino, other.cel_destino)
				&& Objects.equals(endereco_destino, other.endereco_destino) && id_destino == other.id_destino
				&& qtd_dependentes_destino == other.qtd_dependentes_destino
				&& Objects.equals(responsavel_destino, other.responsavel_destino);
	}

	/**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Destino.
     *
     * @return Uma string representando o objeto Destino.
     */
	@Override
	public String toString() {
		return "Destino [id_destino=" + id_destino + ", endereco_destino=" + endereco_destino + ", responsavel_destino="
				+ responsavel_destino + ", cel_destino=" + cel_destino + ", qtd_dependentes_destino="
				+ qtd_dependentes_destino + "]";
	}
}