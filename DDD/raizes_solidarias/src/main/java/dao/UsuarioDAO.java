package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import jakarta.validation.Valid;
import model.Usuario;

/**
 * Classe de acesso a dados para Usuario.
 *
 * Essa classe oferece métodos para manipulação dos dados relacionados à tabela Usuario no banco de dados.
 * Ela estende a classe Repository, que fornece a funcionalidade de conexão com o banco de dados.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Usuario
 * @see services.UsuarioService
 * @see controller.UsuarioResource
 * @see dao.Repository
 * 
 * @author Raízes Solidárias
 */

public class UsuarioDAO extends Repository {
	
	/**
	 * Lista todos os usuários cadastrados no banco de dados.
	 *
	 * @return uma lista de objetos Usuario com os usuários cadastrados
	 */
	public ArrayList<Usuario> listarUsuarios() {
	    String sql = "SELECT * FROM usuario ORDER BY id_usuario";
	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Usuario> listaUsuarios = new ArrayList<>();

	    try {
	        ps = getConnection().prepareStatement(sql);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	            Usuario usuario = new Usuario();
	            usuario.setId_usuario(rs.getInt("id_usuario"));
	            usuario.setCpf_usuario(rs.getString("cpf_usuario"));
	            usuario.setNome_usuario(rs.getString("nome_usuario"));
	            usuario.setEmail_usuario(rs.getString("email_usuario"));
	            usuario.setCel_usuario(rs.getString("cel_usuario"));
	            usuario.setSenha_usuario(rs.getString("senha_usuario"));
	            usuario.setStatus_usuario(rs.getString("status_usuario"));
	            listaUsuarios.add(usuario);
	        }

	        if (listaUsuarios.isEmpty()) {
	            System.out.println("Não foram encontrados registros na tabela USUARIO do banco de dados");
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível consultar a listagem da tabela USUARIO: " + e.getMessage());
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

	    return listaUsuarios;
	}
	
	/**
	 * Busca um usuário pelo ID.
	 *
	 * @param id_usuario o ID do usuário a ser buscado
	 * @return o objeto Usuario correspondente ao ID fornecido, ou null se não encontrado
	 */
	public static Usuario buscarUsuarioPorId(int id_usuario) {
		String sql = "SELECT * FROM usuario WHERE id_usuario = ?";
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_usuario);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				Usuario usuario = new Usuario();
				while (rs.next()) {
					usuario.setId_usuario(rs.getInt("id_usuario"));
					usuario.setCpf_usuario(rs.getString("cpf_usuario"));
					usuario.setNome_usuario(rs.getString("nome_usuario"));
					usuario.setEmail_usuario(rs.getString("email_usuario"));
					usuario.setCel_usuario(rs.getString("cel_usuario"));
					usuario.setSenha_usuario(rs.getString("senha_usuario"));
					usuario.setStatus_usuario(rs.getString("status_usuario"));
				}

				return usuario;

			} else {
				System.out.println(
						"Não foi possível encontrar o id: " + id_usuario + " na tabela USUARIO do banco de dados");
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar o USUARIO no banco de dados: " + e.getMessage());
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
	 * Atualiza um usuário no banco de dados.
	 *
	 * @param usuario o objeto Usuario com as informações atualizadas
	 * @return o objeto Usuario atualizado, ou null se a atualização não foi bem-sucedida
	 */
	public static Usuario atualizarUsuario(@Valid Usuario usuario) {
		String sql = "UPDATE usuario SET cpf_usuario = ?, nome_usuario = ?, email_usuario = ?, cel_usuario = ?, senha_usuario = ?, status_usuario = ? WHERE id_usuario = ?";
		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setString(1, usuario.getCpf_usuario());
			cs.setString(2, usuario.getNome_usuario());
			cs.setString(3, usuario.getEmail_usuario());
			cs.setString(4, usuario.getCel_usuario());
			cs.setString(5, usuario.getSenha_usuario());
			cs.setString(6, usuario.getStatus_usuario());
			cs.setInt(7, usuario.getId_usuario());
			cs.executeUpdate();

			return usuario;

		} catch (SQLException e) {
			System.out.println("Não foi possível atualizar o USUARIO no banco de dados: " + e.getMessage());
		} finally {
			if (cs != null) {
				try {
					cs.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Callable Statement: " + e.getMessage());
				}
			}
		}

		return null;
	}
	
	/**
	 * Cadastra um novo usuário no banco de dados.
	 *
	 * @param usuario_novo o objeto Usuario a ser cadastrado
	 * @return o objeto Usuario cadastrado, ou null se o cadastro não foi bem-sucedido
	 */
	public static Usuario cadastrarUsuario(@Valid Usuario usuario_novo) {

		// @formatter:off
		String sql = "BEGIN INSERT INTO usuario ("
				+ " id_usuario,"
				+ " cpf_usuario,"
				+ " nome_usuario,"
				+ " email_usuario,"
				+ " cel_usuario,"
				+ " senha_usuario,"
				+ " status_usuario"
				+ ") VALUES ("
				+ " SQ_USUARIO.nextval,"
				+ " ?,"
				+ " ?,"
				+ " ?,"
				+ " ?,"
				+ " ?,"
				+ " ?"
				+ ") "
				+ "RETURNING id_usuario INTO ?; END;";
		// @formatter:on

		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setString(1, usuario_novo.getCpf_usuario());
			cs.setString(2, usuario_novo.getNome_usuario());
			cs.setString(3, usuario_novo.getEmail_usuario());
			cs.setString(4, usuario_novo.getCel_usuario());
			cs.setString(5, usuario_novo.getSenha_usuario());
			cs.setString(6, usuario_novo.getStatus_usuario());
			cs.registerOutParameter(7, java.sql.Types.INTEGER);
			cs.executeUpdate();
			usuario_novo.setId_usuario(cs.getInt(7));

			return usuario_novo;

		} catch (SQLException e) {
			System.out.println("Não foi possível cadastrar novo USUARIO no banco de dados: " + e.getMessage());
		} finally {
			if (cs != null) {
				try {
					cs.close();
				} catch (SQLException e) {
					System.out.println("Não foi possível fechar o Callable Statement: " + e.getMessage());
				}
			}
		}

		return null;

	}
	
	/**
	 * Altera o status de um usuário para "excluído" no banco de dados.
	 *
	 * @param id_usuario o ID do usuário a ter o status alterado
	 * @return true se o status foi alterado com sucesso, false caso contrário
	 */
	public boolean deletarUsuario(int id_usuario) {
	    String sql = "UPDATE usuario SET status_usuario = ? WHERE id_usuario = ?";
	    PreparedStatement ps = null;

	    try {
	        ps = getConnection().prepareStatement(sql);
	        ps.setString(1, "Excluído");
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