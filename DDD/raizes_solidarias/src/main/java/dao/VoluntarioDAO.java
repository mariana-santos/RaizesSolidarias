package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

import jakarta.validation.Valid;
import model.Voluntario;

/**
 * Classe de acesso a dados para Voluntario.
 * 
 * Essa classe oferece métodos para manipulação dos dados relacionados aos Voluntarios no banco de dados.
 * Ela estende a classe Repository, que fornece a funcionalidade de conexão com o banco de dados.
 * 
 * 
 * @since 1.0
 * @version 1.0
 * 
 * @see model.Voluntario
 * @see services.VoluntarioService
 * @see controller.VoluntarioResource
 * @see dao.Repository
 * @see model.Usuario
 * 
 * @author Raízes Solidárias
 * 
 */
public class VoluntarioDAO extends Repository {
	
	/**
	 * Retorna uma lista de todos os voluntarios cadastrados no banco de dados.
	 *
	 * @return ArrayList contendo os objetos Voluntario correspondentes aos registros encontrados, ou uma lista vazia se nenhum registro for encontrado.
	 */
	public ArrayList<Voluntario> listarVoluntarios() {
		String sql = "SELECT usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario, usuario.cel_usuario, usuario.senha_usuario, usuario.status_usuario, voluntario.data_registro_voluntario FROM usuario INNER JOIN voluntario ON usuario.id_usuario = voluntario.id_usuario ORDER BY voluntario.id_usuario";
		PreparedStatement ps = null;
		ResultSet rs = null;
		ArrayList<Voluntario> listaVoluntarios = new ArrayList<>();

		try {

			ps = getConnection().prepareStatement(sql);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				while (rs.next()) {
					Voluntario voluntario = new Voluntario();
					voluntario.setId_usuario(rs.getInt("id_usuario"));
					voluntario.setCpf_usuario(rs.getString("cpf_usuario"));
					voluntario.setNome_usuario(rs.getString("nome_usuario"));
					voluntario.setEmail_usuario(rs.getString("email_usuario"));
					voluntario.setCel_usuario(rs.getString("cel_usuario"));
					voluntario.setSenha_usuario(rs.getString("senha_usuario"));
					voluntario.setStatus_usuario(rs.getString("status_usuario"));
					voluntario.setData_registro_voluntario(rs.getDate("data_registro_voluntario"));
					
					listaVoluntarios.add(voluntario);
				}
			} else {
				System.out.println("Não foi possível encontrar registros na tabela VOLUNTARIO do banco de dados");
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar a listagem da tabela VOLUNTARIO: " + e.getMessage());
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

	    return listaVoluntarios;
	}
	
	/**
	 * Busca um voluntario no banco de dados pelo ID do usuário.
	 *
	 * @param id_usuario O ID do usuário do voluntario a ser buscado.
	 * @return O objeto Voluntario correspondente ao registro encontrado, ou null se nenhum registro for encontrado.
	 */
	public static Voluntario buscarVoluntarioPorId(int id_usuario) {
		String sql = "SELECT usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario, usuario.cel_usuario, usuario.senha_usuario, usuario.status_usuario, voluntario.data_registro_voluntario FROM usuario INNER JOIN voluntario ON usuario.id_usuario = voluntario.id_usuario WHERE voluntario.id_usuario = ?";
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_usuario);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				Voluntario voluntario = new Voluntario();
				while (rs.next()) {
					voluntario.setId_usuario(rs.getInt("id_usuario"));
					voluntario.setCpf_usuario(rs.getString("cpf_usuario"));
					voluntario.setNome_usuario(rs.getString("nome_usuario"));
					voluntario.setEmail_usuario(rs.getString("email_usuario"));
					voluntario.setCel_usuario(rs.getString("cel_usuario"));
					voluntario.setSenha_usuario(rs.getString("senha_usuario"));
					voluntario.setStatus_usuario(rs.getString("status_usuario"));
					voluntario.setData_registro_voluntario(rs.getDate("data_registro_voluntario"));
				}

				return voluntario;

			} else {
				System.out.println(
						"Não foi possível encontrar o id: " + id_usuario + " na tabela VOLUNTARIO do banco de dados");
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar o VOLUNTARIO no banco de dados: " + e.getMessage());
		} finally {
			if (ps != null) {
				try {
					ps.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Prepared Statement: " + e.getMessage());
				}
			}

			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Result Set: " + e.getMessage());
				}
			}
		}

		return null;
	}
	
	/**
	 * Busca um voluntario no banco de dados pelo email do usuário.
	 *
	 * @param email_usuario O email do usuário do voluntario a ser buscado.
	 * @return O objeto Voluntario correspondente ao registro encontrado, ou null se nenhum registro for encontrado.
	 */
	public static Voluntario buscarVoluntarioPorEmail(String email_usuario) {
		String sql = "SELECT usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario, usuario.cel_usuario, usuario.senha_usuario, usuario.status_usuario, voluntario.data_registro_voluntario FROM usuario INNER JOIN voluntario ON usuario.id_usuario = voluntario.id_usuario WHERE UPPER(usuario.email_usuario) = UPPER(?)";
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setString(1, email_usuario);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				Voluntario voluntario = new Voluntario();
				while (rs.next()) {
					voluntario.setId_usuario(rs.getInt("id_usuario"));
					voluntario.setCpf_usuario(rs.getString("cpf_usuario"));
					voluntario.setNome_usuario(rs.getString("nome_usuario"));
					voluntario.setEmail_usuario(rs.getString("email_usuario"));
					voluntario.setCel_usuario(rs.getString("cel_usuario"));
					voluntario.setSenha_usuario(rs.getString("senha_usuario"));
					voluntario.setStatus_usuario(rs.getString("status_usuario"));
					voluntario.setData_registro_voluntario(rs.getDate("data_registro_voluntario"));
				}

				return voluntario;

			} else {
				System.out.println("Não foi possível encontrar o email: " + email_usuario + " na tabela VOLUNTARIO do banco de dados");
				return null;
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar o VOLUNTARIO no banco de dados: " + e.getMessage());
			return null;
		} finally {
			if (ps != null) {
				try {
					ps.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Prepared Statement: " + e.getMessage());
				}
			}

			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Result Set: " + e.getMessage());
				}
			}
		}
	}
	
	/**
	 * Atualiza as informações de um voluntario no banco de dados.
	 *
	 * @param voluntario O objeto Voluntario com as informações atualizadas.
	 * @return true se o Voluntario foi atualizado com sucesso, false caso contrário.
	 */
	public static boolean atualizarVoluntario(@Valid Voluntario voluntario) {
		String sql = "UPDATE voluntario SET data_registro_voluntario = ? WHERE id_usuario = ?";
		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setDate(1, voluntario.getData_registro_voluntario());
			cs.setInt(2, voluntario.getId_usuario());
			
			int rowsAffected = cs.executeUpdate();

	        if (rowsAffected > 0) {
	            return true;
	        }

		} catch (SQLException e) {
			System.out.println("Não foi possível atualizar o VOLUNTARIO no banco de dados: " + e.getMessage());
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
	 * Cadastra um novo voluntario no banco de dados.
	 *
	 * @param voluntario_novo O objeto Voluntario contendo as informações do novo voluntario.
	 * @return O objeto Voluntario cadastrado, ou null se o cadastro falhar.
	 */
	public static Voluntario cadastrarVoluntario(@Valid Voluntario voluntario_novo) {

	// @formatter:off
    String sql_voluntario = "INSERT INTO voluntario ("
            + " id_usuario,"
    		+ " data_registro_voluntario"
            + ") VALUES ("
            + " ?,"
            + " ?"
            + ") ";
    // @formatter:on

		CallableStatement cs_voluntario = null;

		try {
			cs_voluntario = getConnection().prepareCall(sql_voluntario);
			cs_voluntario.setInt(1, voluntario_novo.getId_usuario());
			
			SimpleDateFormat formatar = new SimpleDateFormat("yyyy/MM/dd");
			String timeStamp = formatar.format(new Date());
			try {
			    java.util.Date data_registro = formatar.parse(timeStamp);
			    long millis = data_registro.getTime();
			    java.sql.Date sqlDate = new java.sql.Date(millis);
			    cs_voluntario.setDate(2, sqlDate);
			} catch (ParseException e) {
			    e.printStackTrace();
			}
			
			cs_voluntario.executeUpdate();
		} catch (SQLException e) {
			System.out.println("Não foi possível cadastrar novo VOLUNTARIO no banco de dados: " + e.getMessage());
			return null;
		} finally {
			if (cs_voluntario != null) {
				try {
					cs_voluntario.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Callable Statement: " + e.getMessage());
				}
			}
		}

		return voluntario_novo;
	}
	
	/**
	 * Altera o status de um usuário para "excluído" no banco de dados.
	 *
	 * @param id_usuario o ID do usuário a ter o status alterado
	 * @return true se o status foi alterado com sucesso, false caso contrário
	 */
	public static boolean deletarVoluntario(int id_usuario) {
	    String sql = "UPDATE usuario SET status_usuario = ? WHERE id_usuario = ?";
	    PreparedStatement ps = null;

	    try {
	        ps = getConnection().prepareStatement(sql);
	        ps.setString(1, "Inativo");
	        ps.setInt(2, id_usuario);
	        int rowsAffected = ps.executeUpdate();
	        
	        return rowsAffected > 0;

	    } catch (SQLException e) {
	        System.out.println("Não foi possível alterar o status do usuário no banco de dados: " + e.getMessage());
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