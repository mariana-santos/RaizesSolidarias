package model;

import java.sql.Date;
import java.util.Objects;

import jakarta.validation.constraints.NotNull;

/**
 * Classe que representa um agendamento de um voluntário ou de um receptor para retirada de carga de alimentos.
 *
 * A classe Agendamento contém informações sobre o ID do agendamento, a data do agendamento, o turno do agendamento (horário) e o usuário relacionado.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see services.AgendamentoService
 * @see dao.AgendamentoDAO
 * @see controller.AgendamentoResource
 * @see model.Usuario
 *
 * @author Raízes Solidárias
 */
public class Agendamento {
	
	/**
     * ID do Agendamento.
     */
    @NotNull(message = "O ID do Agendamento não pode ser nulo.")
    private int id_agendamento;
    
    /**
     * Data do Agendamento.
     */
    @NotNull(message = "A Data do Agendamento não pode ser nula.")
    private Date data_agendamento;

    /**
     * Turno do Agendamento.
     */
    @NotNull(message = "O Turno do Agendamento não pode ser nulo.")
    private String turno_agendamento;

    /**
     * Usuario do Agendamento.
     */
    @NotNull(message = "O Usuário não pode ser nulo.")
    private Usuario usuario;

    /**
     * Obtém o ID do Agendamento.
     *
     * @return O ID do Agendamento.
     */
    public int getId_agendamento() {
        return id_agendamento;
    }

    /**
     * Define o ID do Agendamento.
     *
     * @param id_agendamento O ID do Agendamento a ser definido.
     */
    public void setId_agendamento(int id_agendamento) {
        this.id_agendamento = id_agendamento;
    }

    /**
     * Obtém a data do Agendamento.
     *
     * @return A data do Agendamento.
     */
    public Date getData_agendamento() {
        return data_agendamento;
    }

    /**
     * Define a data do Agendamento.
     *
     * @param data_agendamento A data do Agendamento a ser definida.
     */
    public void setData_agendamento(Date data_agendamento) {
        this.data_agendamento = data_agendamento;
    }

    /**
     * Obtém o turno do Agendamento.
     *
     * @return O turno do Agendamento.
     */
    public String getTurno_agendamento() {
        return turno_agendamento;
    }

    /**
     * Define o turno do Agendamento.
     *
     * @param turno_agendamento O turno do Agendamento a ser definido.
     */
    public void setTurno_agendamento(String turno_agendamento) {
        this.turno_agendamento = turno_agendamento;
    }

    /**
     * Obtém o usuário do Agendamento.
     *
     * @return O usuário do Agendamento.
     */
    public Usuario getUsuario() {
        return usuario;
    }

    /**
     * Define o usuário do Agendamento.
     *
     * @param usuario O usuário do Agendamento a ser definido.
     */
    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    /**
     * Construtor padrão da classe Agendamento.
     */
    public Agendamento() {
        super();
    }

    /**
     * Construtor não padrão da classe Agendamento.
     *
     * @param id_agendamento     O ID do Agendamento (não pode ser nulo).
     * @param data_agendamento   A data do Agendamento (não pode ser nula).
     * @param turno_agendamento  O turno do Agendamento (não pode ser nulo).
     * @param usuario            O usuário do Agendamento (não pode ser nulo).
     */
    public Agendamento(@NotNull(message = "O ID do Agendamento não pode ser nulo.") int id_agendamento,
                       @NotNull(message = "A Data do Agendamento não pode ser nula.") Date data_agendamento,
                       @NotNull(message = "O Turno do Agendamento não pode ser nulo.") String turno_agendamento,
                       @NotNull(message = "O Usuário não pode ser nulo.") Usuario usuario) {
        super();
        this.id_agendamento = id_agendamento;
        this.data_agendamento = data_agendamento;
        this.turno_agendamento = turno_agendamento;
        this.usuario = usuario;
    }

    /**
     * Sobrescrita do método hashCode para comparar objetos da classe Agendamento.
     *
     * @return O valor do hashCode calculado para o objeto Agendamento.
     */
    @Override
    public int hashCode() {
        return Objects.hash(data_agendamento, id_agendamento, turno_agendamento, usuario);
    }

    /**
     * Sobrescrita do método equals para comparar objetos da classe Agendamento.
     *
     * @param obj O objeto a ser comparado com o Agendamento atual.
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
        Agendamento other = (Agendamento) obj;
        return Objects.equals(data_agendamento, other.data_agendamento) && id_agendamento == other.id_agendamento
                && Objects.equals(turno_agendamento, other.turno_agendamento)
                && Objects.equals(usuario, other.usuario);
    }

    /**
     * Sobrescrita do método toString para retornar uma representação textual do objeto Agendamento.
     *
     * @return Uma string representando o objeto Agendamento.
     */
    @Override
    public String toString() {
        return "Agendamento [id_agendamento=" + id_agendamento + ", data_agendamento=" + data_agendamento
                + ", turno_agendamento=" + turno_agendamento + ", usuario=" + usuario + "]";
    }
}
