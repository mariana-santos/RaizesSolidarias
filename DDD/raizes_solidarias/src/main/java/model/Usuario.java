package model;

import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa um Usuario da plataforma, podendo ser um Doador, Receptor ou Voluntário.
 * 
 * A Classe Usuario contém informações sobre o Usuario, como o id, cpf, nome, email, celular e senha.
 *
 * @since 1.0
 * @version 1.0
 * 
 * @see services.UsuarioService
 * @see dao.UsuarioDao
 * @see controller.UsuarioResource
 * @see model.Doador
 * @see model.Receptor
 * @see model.Voluntario
 * 
 * @author Raízes Solidárias
 */
public class Usuario {

    /**
     * ID do Usuario.
     */
	@NotNull(message = "O ID do Usuario não pode ser nulo.")
    protected int id_usuario;

    /**
     * CPF do Usuario.
     */
    @NotNull(message = "O CPF do Usuario não pode ser nulo.")
    protected String cpf_usuario;

    /**
     * Nome do Usuario.
     */
    @NotNull(message = "O Nome do Usuario não pode ser nulo.")
    protected String nome_usuario;

    /**
     * Email do Usuario.
     */
    @NotNull(message = "O Email do Usuario não pode ser nulo.")
    protected String email_usuario;

    /**
     * Celular do Usuario.
     */
    @NotNull(message = "O Celular do Usuario não pode ser nulo.")
    protected String cel_usuario;

    /**
     * Senha do Usuario.
     */
    @NotNull(message = "A Senha do Usuario não pode ser nula.")
    protected String senha_usuario;
    
    /**
     * Status do Usuario.
     */
    @NotNull(message = "O Status do Usuario não pode ser nulo.")
    protected String status_usuario;

    /**
     * Obtém o ID do Usuario.
     *
     * @return O ID do Usuario.
     */
    public int getId_usuario() {
        return id_usuario;
    }

    /**
     * Define o ID do Usuario.
     *
     * @param id_usuario O ID do Usuario a ser definido.
     */
    public void setId_usuario(int id_usuario) {
        this.id_usuario = id_usuario;
    }

    /**
     * Obtém o CPF do Usuario.
     *
     * @return O CPF do Usuario.
     */
    public String getCpf_usuario() {
        return cpf_usuario;
    }

    /**
     * Define o CPF do Usuario.
     *
     * @param cpf_usuario O CPF do Usuario a ser definido.
     */
    public void setCpf_usuario(String cpf_usuario) {
        this.cpf_usuario = cpf_usuario;
    }

    /**
     * Obtém o nome do Usuario.
     *
     * @return O nome do Usuario.
     */
    public String getNome_usuario() {
        return nome_usuario;
    }

    /**
     * Define o nome do Usuario.
     *
     * @param nome_usuario O nome do Usuario a ser definido.
     */
    public void setNome_usuario(String nome_usuario) {
        this.nome_usuario = nome_usuario;
    }

    /**
     * Obtém o email do Usuario.
     *
     * @return O email do Usuario.
     */
    public String getEmail_usuario() {
        return email_usuario;
    }

    /**
     * Define o email do Usuario.
     *
     * @param email_usuario O email do Usuario a ser definido.
     */
    public void setEmail_usuario(String email_usuario) {
        this.email_usuario = email_usuario;
    }

    /**
     * Obtém o celular do Usuario.
     *
     * @return O celular do Usuario.
     */
    public String getCel_usuario() {
        return cel_usuario;
    }

    /**
     * Define o celular do Usuario.
     *
     * @param cel_usuario O celular do Usuario a ser definido.
     */
    public void setCel_usuario(String cel_usuario) {
        this.cel_usuario = cel_usuario;
    }

    /**
     * Obtém a senha do Usuario.
     *
     * @return A senha do Usuario
     */
    public String getSenha_usuario() {
        return senha_usuario;
    }

    /**
     * Define a senha do Usuario.
     *
     * @param senha_usuario A senha do Usuario a ser definida.
     */
    public void setSenha_usuario(String senha_usuario) {
        this.senha_usuario = senha_usuario;
    }
    
    /**
     * Obtém o status do Usuario.
     *
     * @return O status do Usuario.
     */
    public String getStatus_usuario() {
        return status_usuario;
    }

    /**
     * Define o status do Usuario.
     *
     * @param status O status do Usuario a ser definido.
     */
    public void setStatus_usuario(String status_usuario) {
        this.status_usuario = status_usuario;
    }
    
    /**
     * Construtor padrão da classe Usuario.
     */
    public Usuario() {
        super();
    }

    /**
     * Construtor não padrão da classe Usuario.
     *
     * @param id_usuario      O ID do Usuario (não pode ser nulo).
     * @param cpf_usuario     O CPF do Usuario (não pode ser nulo).
     * @param nome_usuario    O Nome do Usuario (não pode ser nulo).
     * @param email_usuario   O Email do Usuario (não pode ser nulo).
     * @param cel_usuario     O Número de celular do Usuario (não pode ser nulo).
     * @param senha_usuario   A Senha do Usuario (não pode ser nula).
     * @param status_usuario  O Status do Usuario (não pode ser nulo).
     */
    public Usuario(@NotNull(message = "O ID do Usuario não pode ser nulo.") int id_usuario, 
    		@NotNull(message = "O CPF do Usuario não pode ser nulo.") String cpf_usuario,
            @NotNull(message = "O Nome do Usuario não pode ser nulo.") String nome_usuario,
            @NotNull(message = "O Email do Usuario não pode ser nulo.") String email_usuario,
            @NotNull(message = "O Celular do Usuario não pode ser nulo.") String cel_usuario,
            @NotNull(message = "A Senha do Usuario não pode ser nula.") String senha_usuario,
            @NotNull(message = "O Status do Usuario não pode ser nulo.") String status_usuario) {
        super();
        this.id_usuario = id_usuario;
        this.cpf_usuario = cpf_usuario;
        this.nome_usuario = nome_usuario;
        this.email_usuario = email_usuario;
        this.cel_usuario = cel_usuario;
        this.senha_usuario = senha_usuario;
        this.status_usuario = status_usuario;
    }

    /**
     * Sobrescrita do método hashCode para comparar objetos da classe Usuario.
     *
     * @return O valor do hashCode calculado para o objeto Usuario.
     */
    @Override
    public int hashCode() {
        return Objects.hash(cel_usuario, cpf_usuario, email_usuario, id_usuario, nome_usuario, senha_usuario, status_usuario);
    }

    /**
     * Sobrescrita do método equals para comparar objetos da classe Usuario.
     *
     * @param obj O objeto a ser comparado com o Usuario atual.
     * @return true se os objetos forem iguais, false caso contrário.
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null || getClass() != obj.getClass())
            return false;
        Usuario other = (Usuario) obj;
        return id_usuario == other.id_usuario && Objects.equals(cpf_usuario, other.cpf_usuario)
                && Objects.equals(nome_usuario, other.nome_usuario) && Objects.equals(email_usuario, other.email_usuario)
                && Objects.equals(cel_usuario, other.cel_usuario) && Objects.equals(senha_usuario, other.senha_usuario)
                && Objects.equals(status_usuario, other.status_usuario);
    }

    /**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Usuario.
     *
     * @return Uma string representando o objeto Usuario.
     */
    @Override
    public String toString() {
        return "Usuario [id_usuario=" + id_usuario + ", cpf_usuario=" + cpf_usuario + ", nome_usuario=" + nome_usuario
                + ", email_usuario=" + email_usuario + ", cel_usuario=" + cel_usuario + ", senha_usuario="
                + senha_usuario + ", status_usuario=" + status_usuario + "]";
    }
}