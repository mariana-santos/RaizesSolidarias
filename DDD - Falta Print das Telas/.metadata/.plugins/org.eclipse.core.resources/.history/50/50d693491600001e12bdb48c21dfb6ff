package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import jakarta.validation.Valid;
import model.Agendamento;
import model.Usuario;

/**
 * Classe de acesso a dados para Agendamento.
 * 
 * Essa classe oferece métodos para manipulação dos dados relacionados aos Agendamentos no banco de dados.
 * Ela estende a classe Repository, que fornece a funcionalidade de conexão com o banco de dados.
 * 
 * 
 * @since 1.0
 * @version 1.0
 * 
 * @see model.Agendamento
 * @see services.AgendamentoService
 * @see controller.AgendamentoResource
 * @see dao.Repository
 * @see model.Voluntario
 * @see model.Receptor
 * 
 * @author Raízes Solidárias
 * 
 */
public class AgendamentoDAO extends Repository {
	
	/**
	 * Retorna uma lista de todos os agendamentos cadastrados no banco de dados.
	 *
	 * @return ArrayList contendo os objetos Agendamento correspondentes aos registros encontrados, ou uma lista vazia se nenhum registro for encontrado.
	 */
	public ArrayList<Agendamento> listarAgendamentos() {
	    String sql = "SELECT a.id_agendamento, a.data_agendamento, a.turno_agendamento, "
	            + "u.id_usuario, u.cpf_usuario, u.nome_usuario, u.email_usuario, u.cel_usuario, u.senha_usuario, u.status_usuario, u.data_registro_usuario "
	            + "FROM agendamento a "
	            + "LEFT JOIN usuario u ON a.id_usuario = u.id_usuario "
	            + "WHERE a.id_agendamento IS NOT NULL";

	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Agendamento> listaAgendamentos = new ArrayList<>();

	    try {
	        ps = getConnection().prepareStatement(sql);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	            Agendamento agendamento = new Agendamento();
	            agendamento.setId_agendamento(rs.getInt("id_agendamento"));
	            agendamento.setData_agendamento(rs.getDate("data_agendamento"));
	            agendamento.setTurno_agendamento(rs.getString("turno_agendamento"));
                
	            Usuario usuario = new Usuario();
                usuario.setId_usuario(rs.getInt("id_usuario"));
                usuario.setCpf_usuario(rs.getString("cpf_usuario"));
                usuario.setNome_usuario(rs.getString("nome_usuario"));
                usuario.setEmail_usuario(rs.getString("email_usuario"));
                usuario.setCel_usuario(rs.getString("cel_usuario"));
                usuario.setSenha_usuario(rs.getString("senha_usuario"));
                usuario.setStatus_usuario(rs.getString("status_usuario"));
                agendamento.setUsuario(usuario);

	            listaAgendamentos.add(agendamento);
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível consultar a listagem da tabela AGENDAMENTO: " + e.getMessage());
	    } finally {
	        if (rs != null) {
	            try {
	                rs.close();
	            } catch (SQLException e) {
	                System.out.println("Erro ao fechar ResultSet: " + e.getMessage());
	            }
	        }
	        if (ps != null) {
	            try {
	                ps.close();
	            } catch (SQLException e) {
	                System.out.println("Erro ao fechar PreparedStatement: " + e.getMessage());
	            }
	        }
	    }

	    return listaAgendamentos;
	}

	/**
	 * Retorna o agendamento correspondente ao ID fornecido.
	 *
	 * @param idAgendamento o ID do agendamento a ser buscado
	 * @return o objeto Agendamento correspondente ao ID fornecido, ou null se nenhum agendamento for encontrado
	 */
	public static Agendamento buscarAgendamentoPorId(int id_agendamento) {
	    String sql = "SELECT a.id_agendamento, a.data_agendamento, a.turno_agendamento, "
	            + "u.id_agendamento, u.cpf_usuario, u.nome_usuario, u.email_usuario, u.cel_usuario, u.senha_usuario, u.status_usuario, u.data_registro_usuario "
	            + "FROM agendamento a "
	            + "LEFT JOIN usuario u ON a.id_agendamento = u.id_agendamento "
	            + "WHERE a.id_agendamento = ?";

	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    Agendamento agendamento = null;

	    try {
	        ps = getConnection().prepareStatement(sql);
	        ps.setInt(1, id_agendamento);
	        rs = ps.executeQuery();

	        if (rs.next()) {
	            agendamento = new Agendamento();
	            agendamento.setId_agendamento(rs.getInt("id_agendamento"));
	            agendamento.setData_agendamento(rs.getDate("data_agendamento"));
	            agendamento.setTurno_agendamento(rs.getString("turno_agendamento"));

                Usuario usuario = new Usuario();
                usuario.setId_usuario(rs.getInt("id_usuario"));
                usuario.setCpf_usuario(rs.getString("cpf_usuario"));
                usuario.setNome_usuario(rs.getString("nome_usuario"));
                usuario.setEmail_usuario(rs.getString("email_usuario"));
                usuario.setCel_usuario(rs.getString("cel_usuario"));
                usuario.setSenha_usuario(rs.getString("senha_usuario"));
                usuario.setStatus_usuario(rs.getString("status_usuario"));

                agendamento.setUsuario(usuario);
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível buscar o agendamento: " + e.getMessage());
	    } finally {
	        if (rs != null) {
	            try {
	                rs.close();
	            } catch (SQLException e) {
	                System.out.println("Erro ao fechar ResultSet: " + e.getMessage());
	            }
	        }
	        if (ps != null) {
	            try {
	                ps.close();
	            } catch (SQLException e) {
	                System.out.println("Erro ao fechar PreparedStatement: " + e.getMessage());
	            }
	        }
	    }

	    return agendamento;
	}

	/**
	 * Atualiza as informações de um agendamento no banco de dados.
	 *
	 * @param agendamento O objeto Agendamento com as informações atualizadas.
	 * @return true se o Agendamento foi atualizado com sucesso, false caso contrário.
	 */
	public static boolean atualizarAgendamento(@Valid Agendamento agendamento) {		
		String sql = "UPDATE agendamento SET data_agendamento = ?, turno_agendamento = ?, id_agendamento = ? WHERE id_agendamento = ?";
		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setDate(1, agendamento.getData_agendamento());
			cs.setString(2, agendamento.getTurno_agendamento());
			cs.setInt(3, agendamento.getUsuario().getId_usuario());
			cs.setInt(4, agendamento.getId_agendamento());
			
			int rowsAffected = cs.executeUpdate();

	        if (rowsAffected > 0) {
	            return true;
	        }

		} catch (SQLException e) {
			System.out.println("Não foi possível atualizar o AGENDAMENTO no banco de dados: " + e.getMessage());
		} finally {
			if (cs != null) {
				try {
					cs.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Callable Statement: " + e.getMessage());
				}
			}
		}

		return false;
	}
	
	/**
	 * Cadastra um novo agendamento no banco de dados.
	 *
	 * @param agendamento_novo O objeto Agendamento contendo as informações do novo agendamento.
	 * @return O objeto Agendamento cadastrado, ou null se o cadastro falhar.
	 */
	public static Agendamento cadastrarAgendamento(@Valid Agendamento agendamento_novo) {

	// @formatter:off
    String sql_usuario = "BEGIN INSERT INTO agendamento ("
            + " id_agendamento,"
            + " data_agendamento,"
            + " turno_agendamento,"
			+ " id_agendamento"
            + ") VALUES ("
            + " SQ_AGENDAMENTO.nextval,"
			+ " ?,"
			+ " ?,"
			+ " ?"
			+ ") "
            + "RETURNING id_agendamento INTO ?; END;";
    // @formatter:on

		CallableStatement cs_usuario = null;

		try {
			cs_usuario = getConnection().prepareCall(sql_usuario);
			cs_usuario.setDate(1, agendamento_novo.getData_agendamento());
			cs_usuario.setString(2, agendamento_novo.getTurno_agendamento());
			cs_usuario.setInt(3, agendamento_novo.getUsuario().getId_usuario());
			cs_usuario.registerOutParameter(4, java.sql.Types.INTEGER);
			cs_usuario.executeUpdate();
			agendamento_novo.setId_agendamento(cs_usuario.getInt(4));
		} catch (SQLException e) {
			System.out.println("Não foi possível cadastrar novo AGENDAMENTO no banco de dados: " + e.getMessage());
			return null;
		} finally {
			if (cs_usuario != null) {
				try {
					cs_usuario.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Callable Statement: " + e.getMessage());
				}
			}
		}

	// @formatter:off
    String sql_agendamento = "INSERT INTO agendamento ("
            + " id_agendamento,"
    		+ " data_agendamento,"
            + " id_usuario"
            + ") VALUES ("
            + " ?,"
            + " ?,"
            + " ?"
            + ") ";
    // @formatter:on

		CallableStatement cs_agendamento = null;

		try {
			cs_agendamento = getConnection().prepareCall(sql_agendamento);
			cs_agendamento.setInt(1, agendamento_novo.getId_agendamento());
			cs_agendamento.setDate(2, agendamento_novo.getData_agendamento());
			cs_agendamento.setInt(3,  agendamento_novo.getUsuario().getId_usuario());
			
			cs_agendamento.executeUpdate();
		} catch (SQLException e) {
			System.out.println("Não foi possível cadastrar novo AGENDAMENTO no banco de dados: " + e.getMessage());
			return null;
		} finally {
			if (cs_agendamento != null) {
				try {
					cs_agendamento.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Callable Statement: " + e.getMessage());
				}
			}
		}

		return agendamento_novo;
	}
	
	/**
	 * Deleta um agendamento do banco de dados pelo ID do agendamento.
	 *
	 * @param id_agendamento O ID do agendamento a ser deletado.
	 * @return true se o agendamento foi deletado com sucesso, false caso contrário.
	 */
	public static boolean deletarAgendamento(int id_agendamento) {

		Agendamento agendamento_deletar = null;
		String sql = "DELETE FROM agendamento WHERE id_agendamento = ?";
		PreparedStatement ps = null;
		agendamento_deletar = buscarAgendamentoPorId(id_agendamento);

		if (agendamento_deletar == null) {
			return false;
		}

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_agendamento);
			ps.executeUpdate();
			return true;

		} catch (SQLException e) {
			System.out.println("Não foi possível deletar o AGENDAMENTO no banco de dados: " + e.getMessage());
		} finally {
			if (ps != null) {
				try {
					ps.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Prepared Statement: " + e.getMessage());
				}
			}
		}

		return false;
	}
}