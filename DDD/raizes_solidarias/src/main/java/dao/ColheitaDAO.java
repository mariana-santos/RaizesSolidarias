package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import jakarta.validation.Valid;
import model.Colheita;

/**
 * Classe de acesso a dados para Colheita.
 *
 * Essa classe oferece métodos para manipulação dos dados relacionados à tabela Colheita no banco de dados.
 * Ela estende a classe Repository, que fornece a funcionalidade de conexão com o banco de dados.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Colheita
 * @see services.ColheitaService
 * @see controller.ColheitaResource
 * @see dao.Repository
 * 
 * @author Raízes Solidárias
 */

public class ColheitaDAO extends Repository {
	
	/**
	 * Lista todos as colheitas cadastrados no banco de dados.
	 *
	 * @return uma lista de objetos Colheita com os colheitas cadastrados
	 */
	public ArrayList<Colheita> listarColheitas() {
	    String sql = "SELECT * FROM colheita ORDER BY id_colheita";
	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Colheita> listaColheitas = new ArrayList<>();

	    try {
	        ps = getConnection().prepareStatement(sql);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	            Colheita colheita = new Colheita();
	            colheita.setId_colheita(rs.getInt("id_colheita"));
	            colheita.setData_colheita(rs.getDate("data_colheita"));
	            colheita.setDescricao_colheita(rs.getString("descricao_colheita"));
	            listaColheitas.add(colheita);
	        }

	        if (listaColheitas.isEmpty()) {
	            System.out.println("Não foram encontrados registros na tabela COLHEITA do banco de dados");
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível consultar a listagem da tabela COLHEITA: " + e.getMessage());
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

	    return listaColheitas;
	}
	
	/**
	 * Busca uma colheita pelo ID.
	 *
	 * @param id_colheita o ID do colheita a ser buscado
	 * @return o objeto Colheita correspondente ao ID fornecido, ou null se não encontrado
	 */
	public static Colheita buscarColheitaPorId(int id_colheita) {
		String sql = "SELECT * FROM colheita WHERE id_colheita = ?";
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_colheita);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				Colheita colheita = new Colheita();
				while (rs.next()) {
					colheita.setId_colheita(rs.getInt("id_colheita"));
		            colheita.setData_colheita(rs.getDate("data_colheita"));
		            colheita.setDescricao_colheita(rs.getString("descricao_colheita"));
				}

				return colheita;

			} else {
				System.out.println(
						"Não foi possível encontrar o id: " + id_colheita + " na tabela COLHEITA do banco de dados");
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar a COLHEITA no banco de dados: " + e.getMessage());
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
	 * Atualiza uma colheita no banco de dados.
	 *
	 * @param colheita o objeto Colheita com as informações atualizadas
	 * @return o objeto Colheita atualizado, ou null se a atualização não foi bem-sucedida
	 */
	public static Colheita atualizarColheita(@Valid Colheita colheita) {
		String sql = "UPDATE colheita SET data_colheita = ?, descricao_colheita = ? WHERE id_colheita = ?";
		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setDate(1, colheita.getData_colheita());
			cs.setString(2, colheita.getDescricao_colheita());
			cs.setInt(3, colheita.getId_colheita());
			cs.executeUpdate();

			return colheita;

		} catch (SQLException e) {
			System.out.println("Não foi possível atualizar a COLHEITA no banco de dados: " + e.getMessage());
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
	 * Cadastra um novo colheita no banco de dados.
	 *
	 * @param colheita_novo o objeto Colheita a ser cadastrado
	 * @return o objeto Colheita cadastrado, ou null se o cadastro não foi bem-sucedido
	 */
	public static Colheita cadastrarColheita(@Valid Colheita colheita_novo) {

		// @formatter:off
		String sql = "BEGIN INSERT INTO colheita ("
				+ " id_colheita,"
				+ " data_colheita,"
				+ " descricao_colheita"
				+ ") VALUES ("
				+ " SQ_COLHEITA.nextval,"
				+ " ?,"
				+ " ?"
				+ ") "
				+ "RETURNING id_colheita INTO ?; END;";
		// @formatter:on

		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setDate(1, colheita_novo.getData_colheita());
			cs.setString(2, colheita_novo.getDescricao_colheita());
			cs.registerOutParameter(3, java.sql.Types.INTEGER);
			cs.executeUpdate();
			colheita_novo.setId_colheita(cs.getInt(3));

			return colheita_novo;

		} catch (SQLException e) {
			System.out.println("Não foi possível cadastrar novo COLHEITA no banco de dados: " + e.getMessage());
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
	 * Deleta uma colheita do banco de dados pelo ID da colheita.
	 *
	 * @param id_colheita O ID da colheita a ser deletada.
	 * @return true se a colheita foi deletada com sucesso, false caso contrário.
	 */
	public boolean deletarColheita(int id_colheita) {

		Colheita colheita_deletar = null;
		String sql = "DELETE FROM colheita WHERE id_colheita = ?";
		PreparedStatement ps = null;
		colheita_deletar = buscarColheitaPorId(id_colheita);

		if (colheita_deletar == null) {
			return false;
		}

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_colheita);
			ps.executeUpdate();
			return true;

		} catch (SQLException e) {
			System.out.println("Não foi possível deletar a COLHEITA no banco de dados: " + e.getMessage());
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