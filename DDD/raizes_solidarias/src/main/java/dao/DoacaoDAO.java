package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import jakarta.validation.Valid;
import model.Doacao;

/**
 * Classe de acesso a dados para Doacao.
 *
 * Essa classe oferece métodos para manipulação dos dados relacionados à tabela Doacao no banco de dados.
 * Ela estende a classe Repository, que fornece a funcionalidade de conexão com o banco de dados.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Doacao
 * @see services.DoacaoService
 * @see controller.DoacaoResource
 * @see dao.Repository
 * @see model.Doador
 * 
 * @author Raízes Solidárias
 */

public class DoacaoDAO extends Repository {
	
	/**
	 * Lista todas as doações cadastrados no banco de dados.
	 *
	 * @return uma lista de objetos Doacao com as doações cadastrados
	 */
	public ArrayList<Doacao> listarDoacoes() {
	    String sql = "SELECT * FROM doacao ORDER BY id_doacao";
	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Doacao> listaDoacoes = new ArrayList<>();

	    try {
	        ps = getConnection().prepareStatement(sql);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	            Doacao doacao = new Doacao();
	            doacao.setId_doacao(rs.getInt("id_doacao"));
	            doacao.setCpf_doacao(rs.getString("cpf_doacao"));
	            doacao.setNome_doacao(rs.getString("nome_doacao"));
	            doacao.setEmail_doacao(rs.getString("email_doacao"));
	            doacao.setCel_doacao(rs.getString("cel_doacao"));
	            doacao.setSenha_doacao(rs.getString("senha_doacao"));
	            doacao.setStatus_doacao(rs.getString("status_doacao"));
	            listaDoacoes.add(doacao);
	        }

	        if (listaDoacoes.isEmpty()) {
	            System.out.println("Não foram encontrados registros na tabela DOACAO do banco de dados");
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível consultar a listagem da tabela DOACAO: " + e.getMessage());
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

	    return listaDoacoes;
	}
	
	/**
	 * Busca um usuário pelo ID.
	 *
	 * @param id_doacao o ID do usuário a ser buscado
	 * @return o objeto Doacao correspondente ao ID fornecido, ou null se não encontrado
	 */
	public static Doacao buscarDoacaoPorId(int id_doacao) {
		String sql = "SELECT * FROM doacao WHERE id_doacao = ?";
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_doacao);
			rs = ps.executeQuery();

			if (rs.isBeforeFirst()) {
				Doacao doacao = new Doacao();
				while (rs.next()) {
					doacao.setId_doacao(rs.getInt("id_doacao"));
					doacao.setCpf_doacao(rs.getString("cpf_doacao"));
					doacao.setNome_doacao(rs.getString("nome_doacao"));
					doacao.setEmail_doacao(rs.getString("email_doacao"));
					doacao.setCel_doacao(rs.getString("cel_doacao"));
					doacao.setSenha_doacao(rs.getString("senha_doacao"));
					doacao.setStatus_doacao(rs.getString("status_doacao"));
				}

				return doacao;

			} else {
				System.out.println(
						"Não foi possível encontrar o id: " + id_doacao + " na tabela DOACAO do banco de dados");
			}

		} catch (SQLException e) {
			System.out.println("Não foi possível consultar o DOACAO no banco de dados: " + e.getMessage());
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
	 * @param doacao o objeto Doacao com as informações atualizadas
	 * @return o objeto Doacao atualizado, ou null se a atualização não foi bem-sucedida
	 */
	public static Doacao atualizarDoacao(@Valid Doacao doacao) {
		String sql = "UPDATE doacao SET cpf_doacao = ?, nome_doacao = ?, email_doacao = ?, cel_doacao = ?, senha_doacao = ?, status_doacao = ? WHERE id_doacao = ?";
		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setString(1, doacao.getCpf_doacao());
			cs.setString(2, doacao.getNome_doacao());
			cs.setString(3, doacao.getEmail_doacao());
			cs.setString(4, doacao.getCel_doacao());
			cs.setString(5, doacao.getSenha_doacao());
			cs.setString(6, doacao.getStatus_doacao());
			cs.setInt(7, doacao.getId_doacao());
			cs.executeUpdate();

			return doacao;

		} catch (SQLException e) {
			System.out.println("Não foi possível atualizar o DOACAO no banco de dados: " + e.getMessage());
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
	 * @param doacao_novo o objeto Doacao a ser cadastrado
	 * @return o objeto Doacao cadastrado, ou null se o cadastro não foi bem-sucedido
	 */
	public static Doacao cadastrarDoacao(@Valid Doacao doacao_novo) {

		// @formatter:off
		String sql = "BEGIN INSERT INTO doacao ("
				+ " id_doacao,"
				+ " cpf_doacao,"
				+ " nome_doacao,"
				+ " email_doacao,"
				+ " cel_doacao,"
				+ " senha_doacao,"
				+ " status_doacao"
				+ ") VALUES ("
				+ " SQ_DOACAO.nextval,"
				+ " ?,"
				+ " ?,"
				+ " ?,"
				+ " ?,"
				+ " ?,"
				+ " ?"
				+ ") "
				+ "RETURNING id_doacao INTO ?; END;";
		// @formatter:on

		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setString(1, doacao_novo.getCpf_doacao());
			cs.setString(2, doacao_novo.getNome_doacao());
			cs.setString(3, doacao_novo.getEmail_doacao());
			cs.setString(4, doacao_novo.getCel_doacao());
			cs.setString(5, doacao_novo.getSenha_doacao());
			cs.setString(6, doacao_novo.getStatus_doacao());
			cs.registerOutParameter(7, java.sql.Types.INTEGER);
			cs.executeUpdate();
			doacao_novo.setId_doacao(cs.getInt(7));

			return doacao_novo;

		} catch (SQLException e) {
			System.out.println("Não foi possível cadastrar novo DOACAO no banco de dados: " + e.getMessage());
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
	 * @param id_doacao o ID do usuário a ter o status alterado
	 * @return true se o status foi alterado com sucesso, false caso contrário
	 */
	public boolean deletarDoacao(int id_doacao) {
	    String sql = "UPDATE doacao SET status_doacao = ? WHERE id_doacao = ?";
	    PreparedStatement ps = null;

	    try {
	        ps = getConnection().prepareStatement(sql);
	        ps.setString(1, "Excluído");
	        ps.setInt(2, id_doacao);
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