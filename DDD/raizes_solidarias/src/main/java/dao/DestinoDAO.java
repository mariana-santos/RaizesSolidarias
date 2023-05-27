package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import jakarta.validation.Valid;
import model.Destino;

/**
 * Classe de acesso a dados para Destino.
 *
 * Essa classe oferece métodos para manipulação dos dados relacionados à tabela Destino no banco de dados.
 * Ela estende a classe Repository, que fornece a funcionalidade de conexão com o banco de dados.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Destino
 * @see services.DestinoService
 * @see controller.DestinoResource
 * @see dao.Repository
 * 
 * @author Raízes Solidárias
 */

public class DestinoDAO extends Repository {
	
	/**
	 * Lista todos os destinos cadastrados no banco de dados.
	 *
	 * @return uma lista de objetos Destino com os destinos cadastrados
	 */
	public ArrayList<Destino> listarDestinos() {
	    String sql = "SELECT * FROM destino ORDER BY id_destino";
	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Destino> listaDestinos = new ArrayList<>();

	    try {
	        ps = getConnection().prepareStatement(sql);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	            Destino destino = new Destino();
	            destino.setId_destino(rs.getInt("id_destino"));
	            destino.setEndereco_destino(rs.getString("endereco_destino"));
	            destino.setResponsavel_destino(rs.getString("responsavel_destino"));
	            destino.setCel_destino(rs.getString("cel_destino"));
	            destino.setQtd_dependentes_destino(rs.getInt("qtd_dependentes_destino"));
	            listaDestinos.add(destino);
	        }

	        if (listaDestinos.isEmpty()) {
	            System.out.println("Não foram encontrados registros na tabela DESTINO do banco de dados");
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível consultar a listagem da tabela DESTINO: " + e.getMessage());
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

	    return listaDestinos;
	}
	
	/**
	 * Busca um destino pelo ID.
	 *
	 * @param id_destino o ID do destino a ser buscado
	 * @return o objeto Destino correspondente ao ID fornecido, ou null se não encontrado
	 */
	public static Destino buscarDestinoPorId(int id_destino) {
		String sql = "SELECT * FROM destino WHERE id_destino = ?";
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_destino);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				Destino destino = new Destino();
				while (rs.next()) {
					destino.setId_destino(rs.getInt("id_destino"));
		            destino.setEndereco_destino(rs.getString("endereco_destino"));
		            destino.setResponsavel_destino(rs.getString("responsavel_destino"));
		            destino.setCel_destino(rs.getString("cel_destino"));
		            destino.setQtd_dependentes_destino(rs.getInt("qtd_dependentes_destino"));
				}

				return destino;

			} else {
				System.out.println(
						"Não foi possível encontrar o id: " + id_destino + " na tabela DESTINO do banco de dados");
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar o DESTINO no banco de dados: " + e.getMessage());
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
	 * Atualiza um destino no banco de dados.
	 *
	 * @param destino o objeto Destino com as informações atualizadas
	 * @return true se o Destino foi atualizado com sucesso, false caso contrário.
	 */
	public static boolean atualizarDestino(@Valid Destino destino) {
		String sql = "UPDATE destino SET endereco_destino = ?, responsavel_destino = ?, cel_destino = ?, qtd_dependentes_destino = ? WHERE id_destino = ?";
		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setString(1, destino.getEndereco_destino());
			cs.setString(2, destino.getResponsavel_destino());
			cs.setString(3, destino.getCel_destino());
			cs.setInt(4, destino.getQtd_dependentes_destino());
			cs.setInt(5, destino.getId_destino());
			
			int rowsAffected = cs.executeUpdate();

	        if (rowsAffected > 0) {
	            return true;
	        }

		} catch (SQLException e) {
			System.out.println("Não foi possível atualizar a DESTINO no banco de dados: " + e.getMessage());
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
	 * Cadastra um novo destino no banco de dados.
	 *
	 * @param destino_novo o objeto Destino a ser cadastrado
	 * @return o objeto Destino cadastrado, ou null se o cadastro não foi bem-sucedido
	 */
	public static Destino cadastrarDestino(@Valid Destino destino_novo) {

		// @formatter:off
		String sql = "BEGIN INSERT INTO destino ("
				+ " id_destino,"
				+ " endereco_destino,"
				+ " responsavel_destino,"
				+ " cel_destino,"
				+ " qtd_dependentes_destino"
				+ ") VALUES ("
				+ " SQ_DESTINO.nextval,"
				+ " ?,"
				+ " ?,"
				+ " ?,"
				+ " ?"
				+ ") "
				+ "RETURNING id_destino INTO ?; END;";
		// @formatter:on

		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setString(1, destino_novo.getEndereco_destino());
			cs.setString(2, destino_novo.getResponsavel_destino());
			cs.setString(3, destino_novo.getCel_destino());
			cs.setInt(4, destino_novo.getQtd_dependentes_destino());
			cs.registerOutParameter(5, java.sql.Types.INTEGER);
			cs.executeUpdate();
			destino_novo.setId_destino(cs.getInt(5));

			return destino_novo;

		} catch (SQLException e) {
			System.out.println("Não foi possível cadastrar novo DESTINO no banco de dados: " + e.getMessage());
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
	 * Deleta um destino do banco de dados pelo ID do destino.
	 *
	 * @param id_destino O ID do destino a ser deletado.
	 * @return true se o destino foi deletado com sucesso, false caso contrário.
	 */
	public static boolean deletarDestino(int id_destino) {

		Destino destino_deletar = null;
		String sql = "DELETE FROM destino WHERE id_destino = ?";
		PreparedStatement ps = null;
		destino_deletar = buscarDestinoPorId(id_destino);

		if (destino_deletar == null) {
			return false;
		}

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_destino);
			ps.executeUpdate();
			return true;

		} catch (SQLException e) {
			System.out.println("Não foi possível deletar o DESTINO no banco de dados: " + e.getMessage());
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