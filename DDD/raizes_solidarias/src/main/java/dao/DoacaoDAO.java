package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import jakarta.validation.Valid;
import model.Doacao;
import model.Doador;

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
		String sql = "SELECT doacao.id_doacao, doacao.id_usuario, " +
	             "usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario, usuario.cel_usuario, usuario.senha_usuario, usuario.status_usuario, " +
	             "doador.nivel_doador, doador.moedas_doador, " +
	             "doacao.data_doacao, doacao.qtd_moedas_doacao " +
	             "FROM doacao " +
	             "INNER JOIN doador ON doacao.id_usuario = doador.id_usuario " +
	             "INNER JOIN usuario ON doador.id_usuario = usuario.id_usuario " +
	             "ORDER BY doacao.id_doacao";

	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Doacao> listaDoacoes = new ArrayList<>();

	    try {
	        ps = getConnection().prepareStatement(sql);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	            Doacao doacao = new Doacao();
	            doacao.setId_doacao(rs.getInt("id_doacao"));
	            
	            Doador doador = new Doador();
				doador.setId_usuario(rs.getInt("id_usuario"));
				doador.setCpf_usuario(rs.getString("cpf_usuario"));
				doador.setNome_usuario(rs.getString("nome_usuario"));
				doador.setEmail_usuario(rs.getString("email_usuario"));
				doador.setCel_usuario(rs.getString("cel_usuario"));
				doador.setSenha_usuario(rs.getString("senha_usuario"));
				doador.setStatus_usuario(rs.getString("status_usuario"));
				doador.setNivel_doador(rs.getInt("nivel_doador"));
				doador.setMoedas_doador(rs.getInt("moedas_doador"));
				
				doacao.setDoador(doador);
				
				doacao.setData_doacao(rs.getDate("data_doacao"));
				doacao.setQtd_moedas_doacao(rs.getInt("qtd_moedas_doacao"));
				
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
	 * Busca uma doação pelo ID.
	 *
	 * @param id_doacao o ID da doação a ser buscado
	 * @return o objeto Doacao correspondente ao ID fornecido, ou null se não encontrado
	 */
	public Doacao buscarDoacaoPorId(int id_doacao) {
	    String sql = "SELECT doacao.id_doacao, doacao.id_usuario, " +
	                 "usuario.id_usuario, usuario.cpf_usuario, usuario.nome_usuario, usuario.email_usuario, usuario.cel_usuario, usuario.senha_usuario, usuario.status_usuario, " +
	                 "doador.nivel_doador, doador.moedas_doador, " +
	                 "doacao.data_doacao, doacao.qtd_moedas_doacao " +
	                 "FROM doacao " +
	                 "INNER JOIN doador ON doacao.id_usuario = doador.id_usuario " +
	                 "INNER JOIN usuario ON doador.id_usuario = usuario.id_usuario " +
	                 "WHERE doacao.id_doacao = ?";

	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    Doacao doacao = null;

	    try {
	        ps = getConnection().prepareStatement(sql);
	        ps.setInt(1, id_doacao);
	        rs = ps.executeQuery();

	        if (rs.next()) {
	            doacao = new Doacao();
	            doacao.setId_doacao(rs.getInt("id_doacao"));

	            Doador doador = new Doador();
	            doador.setId_usuario(rs.getInt("id_usuario"));
	            doador.setCpf_usuario(rs.getString("cpf_usuario"));
	            doador.setNome_usuario(rs.getString("nome_usuario"));
	            doador.setEmail_usuario(rs.getString("email_usuario"));
	            doador.setCel_usuario(rs.getString("cel_usuario"));
	            doador.setSenha_usuario(rs.getString("senha_usuario"));
	            doador.setStatus_usuario(rs.getString("status_usuario"));
	            doador.setNivel_doador(rs.getInt("nivel_doador"));
	            doador.setMoedas_doador(rs.getInt("moedas_doador"));

	            doacao.setDoador(doador);
	            
	            doacao.setData_doacao(rs.getDate("data_doacao"));
	            doacao.setQtd_moedas_doacao(rs.getInt("qtd_moedas_doacao"));
	        }

	        if (doacao == null) {
	            System.out.println("Não foi encontrada uma doação com o ID fornecido: " + id_doacao);
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível buscar a doação: " + e.getMessage());
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

	    return doacao;
	}

	// CONTINUAR A PARTIR DAQUI -------------------------------------------------------------------------------
	
	/**
	 * Atualiza um doação no banco de dados.
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
	 * Cadastra um novo doação no banco de dados.
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
	 * Altera o status de um doação para "excluído" no banco de dados.
	 *
	 * @param id_doacao o ID do doação a ter o status alterado
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
	        System.out.println("Não foi possível alterar o status do doação no banco de dados: " + e.getMessage());
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