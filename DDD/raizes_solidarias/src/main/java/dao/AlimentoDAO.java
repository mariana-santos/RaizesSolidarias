package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import jakarta.validation.Valid;
import model.Alimento;

/**
 * Classe de acesso a dados para Alimento.
 *
 * Essa classe oferece métodos para manipulação dos dados relacionados à tabela Alimento no banco de dados.
 * Ela estende a classe Repository, que fornece a funcionalidade de conexão com o banco de dados.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Alimento
 * @see services.AlimentoService
 * @see controller.AlimentoResource
 * @see dao.Repository
 * 
 * @author Raízes Solidárias
 */

public class AlimentoDAO extends Repository {
	
	/**
	 * Lista todos os alimentos cadastrados no banco de dados.
	 *
	 * @return uma lista de objetos Alimento com os alimentos cadastrados
	 */
	public ArrayList<Alimento> listarAlimentos() {
	    String sql = "SELECT * FROM alimento ORDER BY id_alimento";
	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Alimento> listaAlimentos = new ArrayList<>();

	    try {
	        ps = getConnection().prepareStatement(sql);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	            Alimento alimento = new Alimento();
	            alimento.setId_alimento(rs.getInt("id_alimento"));
	            alimento.setNome_alimento(rs.getString("nome_alimento"));
	            alimento.setTempo_colheita(rs.getInt("tempo_colheita"));
	            alimento.setQtd_irrigacao(rs.getInt("qtd_irrigacao"));
	            alimento.setPreco_alimento(rs.getInt("preco_alimento"));
	            alimento.setQtd_alimento(rs.getInt("qtd_alimento"));
	            listaAlimentos.add(alimento);
	        }

	        if (listaAlimentos.isEmpty()) {
	            System.out.println("Não foram encontrados registros na tabela ALIMENTO do banco de dados");
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível consultar a listagem da tabela ALIMENTO: " + e.getMessage());
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

	    return listaAlimentos;
	}
	
	/**
	 * Busca um alimento pelo ID.
	 *
	 * @param id_alimento o ID do alimento a ser buscado
	 * @return o objeto Alimento correspondente ao ID fornecido, ou null se não encontrado
	 */
	public static Alimento buscarAlimentoPorId(int id_alimento) {
		String sql = "SELECT * FROM alimento WHERE id_alimento = ?";
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_alimento);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				Alimento alimento = new Alimento();
				while (rs.next()) {
					alimento.setId_alimento(rs.getInt("id_alimento"));
		            alimento.setNome_alimento(rs.getString("nome_alimento"));
		            alimento.setTempo_colheita(rs.getInt("tempo_colheita"));
		            alimento.setQtd_irrigacao(rs.getInt("qtd_irrigacao"));
		            alimento.setPreco_alimento(rs.getInt("preco_alimento"));
		            alimento.setQtd_alimento(rs.getInt("qtd_alimento"));
				}

				return alimento;

			} else {
				System.out.println(
						"Não foi possível encontrar o id: " + id_alimento + " na tabela ALIMENTO do banco de dados");
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar o ALIMENTO no banco de dados: " + e.getMessage());
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
	 * Atualiza um alimento no banco de dados.
	 *
	 * @param alimento o objeto Alimento com as informações atualizadas
	 * @return o objeto Alimento atualizado, ou null se a atualização não foi bem-sucedida
	 */
	public static boolean atualizarAlimento(@Valid Alimento alimento) {
		String sql = "UPDATE alimento SET nome_alimento = ?, tempo_colheita = ?, qtd_irrigacao = ?, preco_alimento = ?, qtd_alimento = ? WHERE id_alimento = ?";
		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setString(1, alimento.getNome_alimento());
			cs.setInt(2, alimento.getTempo_colheita());
			cs.setInt(3, alimento.getQtd_irrigacao());
			cs.setInt(4, alimento.getPreco_alimento());
			cs.setInt(5, alimento.getQtd_alimento());
			cs.setInt(6, alimento.getId_alimento());
			
			int rowsAffected = cs.executeUpdate();

	        if (rowsAffected > 0) {
	            return true;
	        }

		} catch (SQLException e) {
			System.out.println("Não foi possível atualizar o ALIMENTO no banco de dados: " + e.getMessage());
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
	 * Cadastra um novo alimento no banco de dados.
	 *
	 * @param alimento_novo o objeto Alimento a ser cadastrado
	 * @return o objeto Alimento cadastrado, ou null se o cadastro não foi bem-sucedido
	 */
	public static Alimento cadastrarAlimento(@Valid Alimento alimento_novo) {

		// @formatter:off
		String sql = "BEGIN INSERT INTO alimento ("
				+ " id_alimento,"
				+ " nome_alimento,"
				+ " tempo_colheita,"
				+ " qtd_irrigacao,"
				+ " preco_alimento,"
				+ " qtd_alimento"
				+ ") VALUES ("
				+ " SQ_ALIMENTO.nextval,"
				+ " ?,"
				+ " ?,"
				+ " ?,"
				+ " ?,"
				+ " ?"
				+ ") "
				+ "RETURNING id_alimento INTO ?; END;";
		// @formatter:on

		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setString(1, alimento_novo.getNome_alimento());
			cs.setInt(2, alimento_novo.getTempo_colheita());
			cs.setInt(3, alimento_novo.getQtd_irrigacao());
			cs.setInt(4, alimento_novo.getPreco_alimento());
			cs.setInt(5, alimento_novo.getQtd_alimento());
			cs.setInt(6, alimento_novo.getId_alimento());
			cs.registerOutParameter(6, java.sql.Types.INTEGER);
			cs.executeUpdate();
			alimento_novo.setId_alimento(cs.getInt(6));

			return alimento_novo;

		} catch (SQLException e) {
			System.out.println("Não foi possível cadastrar novo ALIMENTO no banco de dados: " + e.getMessage());
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
	 * Deleta um alimento do banco de dados pelo ID do alimento.
	 *
	 * @param id_alimento O ID do alimento a ser deletado.
	 * @return true se o alimento foi deletado com sucesso, false caso contrário.
	 */
	public static boolean deletarAlimento(int id_alimento) {

		Alimento alimento_deletar = null;
		String sql = "DELETE FROM alimento WHERE id_alimento = ?";
		PreparedStatement ps = null;
		alimento_deletar = buscarAlimentoPorId(id_alimento);

		if (alimento_deletar == null) {
			return false;
		}

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_alimento);
			ps.executeUpdate();
			return true;

		} catch (SQLException e) {
			System.out.println("Não foi possível deletar o ALIMENTO no banco de dados: " + e.getMessage());
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