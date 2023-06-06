package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import jakarta.validation.Valid;
import model.Receptor;

/**
 * Classe de acesso a dados para Receptor.
 * 
 * Essa classe oferece métodos para manipulação dos dados relacionados aos Receptores no banco de dados.
 * Ela estende a classe Repository, que fornece a funcionalidade de conexão com o banco de dados.
 * 
 * 
 * @since 1.0
 * @version 1.0
 * 
 * @see model.Receptor
 * @see services.ReceptorService
 * @see controller.ReceptorResource
 * @see dao.Repository
 * @see model.Usuario
 * 
 * @author Raízes Solidárias
 * 
 */
public class ReceptorDAO extends Repository {
	
	/**
	 * Retorna uma lista de todos os receptores cadastrados no banco de dados.
	 *
	 * @return ArrayList contendo os objetos Receptor correspondentes aos registros encontrados, ou uma lista vazia se nenhum registro for encontrado.
	 */
	public ArrayList<Receptor> listarReceptores() {
		String sql = "SELECT usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario, usuario.cel_usuario, usuario.senha_usuario, usuario.status_usuario, receptor.carga_receptor, receptor.endereco_receptor FROM usuario INNER JOIN receptor ON usuario.id_usuario = receptor.id_usuario ORDER BY receptor.id_usuario";
		PreparedStatement ps = null;
		ResultSet rs = null;
		ArrayList<Receptor> listaReceptores = new ArrayList<>();

		try {

			ps = getConnection().prepareStatement(sql);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				while (rs.next()) {
					Receptor receptor = new Receptor();
					receptor.setId_usuario(rs.getInt("id_usuario"));
					receptor.setCpf_usuario(rs.getString("cpf_usuario"));
					receptor.setNome_usuario(rs.getString("nome_usuario"));
					receptor.setEmail_usuario(rs.getString("email_usuario"));
					receptor.setCel_usuario(rs.getString("cel_usuario"));
					receptor.setSenha_usuario(rs.getString("senha_usuario"));
					receptor.setStatus_usuario(rs.getString("status_usuario"));
					receptor.setCarga_receptor(rs.getInt("carga_receptor"));
					receptor.setEndereco_receptor(rs.getString("endereco_receptor"));
					
					listaReceptores.add(receptor);
				}
			} else {
				System.out.println("Não foi possível encontrar registros na tabela RECEPTOR do banco de dados");
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar a listagem da tabela RECEPTOR: " + e.getMessage());
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

	    return listaReceptores;
	}
	
	/**
	 * Busca um receptor no banco de dados pelo ID do usuário.
	 *
	 * @param id_usuario O ID do usuário do receptor a ser buscado.
	 * @return O objeto Receptor correspondente ao registro encontrado, ou null se nenhum registro for encontrado.
	 */
	public static Receptor buscarReceptorPorId(int id_usuario) {
		String sql = "SELECT usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario, usuario.cel_usuario, usuario.senha_usuario, usuario.status_usuario, receptor.carga_receptor, receptor.endereco_receptor FROM usuario INNER JOIN receptor ON usuario.id_usuario = receptor.id_usuario WHERE receptor.id_usuario = ?";
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_usuario);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				Receptor receptor = new Receptor();
				while (rs.next()) {
					receptor.setId_usuario(rs.getInt("id_usuario"));
					receptor.setCpf_usuario(rs.getString("cpf_usuario"));
					receptor.setNome_usuario(rs.getString("nome_usuario"));
					receptor.setEmail_usuario(rs.getString("email_usuario"));
					receptor.setCel_usuario(rs.getString("cel_usuario"));
					receptor.setSenha_usuario(rs.getString("senha_usuario"));
					receptor.setStatus_usuario(rs.getString("status_usuario"));
					receptor.setCarga_receptor(rs.getInt("carga_receptor"));
					receptor.setEndereco_receptor(rs.getString("endereco_receptor"));
				}

				return receptor;

			} else {
				System.out.println(
						"Não foi possível encontrar o id: " + id_usuario + " na tabela RECEPTOR do banco de dados");
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar o RECEPTOR no banco de dados: " + e.getMessage());
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
	 * Busca um receptor no banco de dados pelo email do usuário.
	 *
	 * @param email_usuario O email do usuário do receptor a ser buscado.
	 * @return O objeto Receptor correspondente ao registro encontrado, ou null se nenhum registro for encontrado.
	 */
	public static Receptor buscarReceptorPorEmail(String email_usuario) {
		String sql = "SELECT usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario, usuario.cel_usuario, usuario.senha_usuario, usuario.status_usuario, receptor.carga_receptor, receptor.endereco_receptor FROM usuario INNER JOIN receptor ON usuario.id_usuario = receptor.id_usuario WHERE UPPER(usuario.email_usuario) = UPPER(?)";
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setString(1, email_usuario);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				Receptor receptor = new Receptor();
				while (rs.next()) {
					receptor.setId_usuario(rs.getInt("id_usuario"));
					receptor.setCpf_usuario(rs.getString("cpf_usuario"));
					receptor.setNome_usuario(rs.getString("nome_usuario"));
					receptor.setEmail_usuario(rs.getString("email_usuario"));
					receptor.setCel_usuario(rs.getString("cel_usuario"));
					receptor.setSenha_usuario(rs.getString("senha_usuario"));
					receptor.setStatus_usuario(rs.getString("status_usuario"));
					receptor.setCarga_receptor(rs.getInt("carga_receptor"));
					receptor.setEndereco_receptor(rs.getString("endereco_receptor"));
				}

				return receptor;

			} else {
				System.out.println("Não foi possível encontrar o email: " + email_usuario + " na tabela RECEPTOR do banco de dados");
				return null;
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar o RECEPTOR no banco de dados: " + e.getMessage());
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
	 * Atualiza as informações de um receptor no banco de dados.
	 *
	 * @param receptor O objeto Receptor com as informações atualizadas.
	 * @return true se o Receptor foi atualizado com sucesso, false caso contrário.
	 */
	public static boolean atualizarReceptor(@Valid Receptor receptor) {
		String sql = "UPDATE receptor SET carga_receptor = ?, endereco_receptor = ? WHERE id_usuario = ?";
		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setInt(1, receptor.getCarga_receptor());
			cs.setString(2, receptor.getEndereco_receptor());
			cs.setInt(3, receptor.getId_usuario());
			
			int rowsAffected = cs.executeUpdate();

	        if (rowsAffected > 0) {
	            return true;
	        }

		} catch (SQLException e) {
			System.out.println("Não foi possível atualizar o RECEPTOR no banco de dados: " + e.getMessage());
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
	 * Cadastra um novo receptor no banco de dados.
	 *
	 * @param receptor_novo O objeto Receptor contendo as informações do novo receptor.
	 * @return O objeto Receptor cadastrado, ou null se o cadastro falhar.
	 */
	public static Receptor cadastrarReceptor(@Valid Receptor receptor_novo) {
		
	// @formatter:off
    String sql_receptor = "INSERT INTO receptor ("
            + " id_usuario,"
    		+ " carga_receptor,"
            + " endereco_receptor"
            + ") VALUES ("
            + " ?,"
            + " ?,"
            + " ?"
            + ") ";
    // @formatter:on

		CallableStatement cs_receptor = null;

		try {
			cs_receptor = getConnection().prepareCall(sql_receptor);
			cs_receptor.setInt(1, receptor_novo.getId_usuario());
			cs_receptor.setInt(2, receptor_novo.getCarga_receptor());
			cs_receptor.setString(3, receptor_novo.getEndereco_receptor());
			cs_receptor.executeUpdate();
		} catch (SQLException e) {
			System.out.println("Não foi possível cadastrar novo RECEPTOR no banco de dados: " + e.getMessage());
			return null;
		} finally {
			if (cs_receptor != null) {
				try {
					cs_receptor.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Callable Statement: " + e.getMessage());
				}
			}
		}

		return receptor_novo;
	}
		
	/**
	 * Altera o status de um usuário para "excluído" no banco de dados.
	 *
	 * @param id_usuario o ID do usuário a ter o status alterado
	 * @return true se o status foi alterado com sucesso, false caso contrário
	 */
	public static boolean deletarReceptor(int id_usuario) {
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