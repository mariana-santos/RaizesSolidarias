package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import jakarta.validation.Valid;
import model.Alimento;
import model.Plantio;

/**
 * Classe de acesso a dados para Plantio.
 *
 * Essa classe oferece métodos para manipulação dos dados relacionados à tabela Plantio no banco de dados.
 * Ela estende a classe Repository, que fornece a funcionalidade de conexão com o banco de dados.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Plantio
 * @see services.PlantioService
 * @see controller.PlantioResource
 * @see dao.Repository
 * 
 * @author Raízes Solidárias
 */

public class PlantioDAO extends Repository {
	
	/**
	 * Lista todos os plantios cadastrados no banco de dados.
	 *
	 * @return uma lista de objetos Plantio com os plantios cadastrados
	 */
	public ArrayList<Plantio> listarPlantios() {
		String sql = "SELECT plantio.id_plantio, plantio.data_plantio, plantio.espaco_plantio, " +
	             "alimento.id_alimento, alimento.nome_alimento, alimento.tempo_colheita, alimento.qtd_irrigacao, alimento.preco_alimento, alimento.qtd_alimento " +
	             "FROM plantio " +
	             "INNER JOIN alimento ON plantio.id_alimento = alimento.id_alimento " +
	             "ORDER BY plantio.id_plantio";

	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Plantio> listaPlantios = new ArrayList<>();

	    try {
	        ps = getConnection().prepareStatement(sql);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	        	Plantio plantio = new Plantio();
	            plantio.setId_plantio(rs.getInt("id_plantio"));
	            plantio.setData_plantio(rs.getDate("data_plantio"));
	            plantio.setEspaco_plantio(rs.getInt("espaco_plantio"));
	            
	            Alimento alimento = new Alimento();
	            alimento.setId_alimento(rs.getInt("id_alimento"));
	            alimento.setNome_alimento(rs.getString("nome_alimento"));
	            alimento.setTempo_colheita(rs.getInt("tempo_colheita"));
	            alimento.setQtd_irrigacao(rs.getInt("qtd_irrigacao"));
	            alimento.setPreco_alimento(rs.getInt("preco_alimento"));
	            alimento.setQtd_alimento(rs.getInt("qtd_alimento"));
	            
	            plantio.setAlimento(alimento);
				
				listaPlantios.add(plantio);
	        }

	        if (listaPlantios.isEmpty()) {
	            System.out.println("Não foram encontrados registros na tabela PLANTIO do banco de dados");
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível consultar a listagem da tabela PLANTIO: " + e.getMessage());
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

	    return listaPlantios;
	}
	
	/**
	 * Busca um plantio pelo ID.
	 *
	 * @param id_plantio o ID do plantio a ser buscado
	 * @return o objeto Plantio correspondente ao ID fornecido, ou null se não encontrado
	 */
	public static Plantio buscarPlantioPorId(int id_plantio) {
		String sql = "SELECT plantio.id_plantio, plantio.data_plantio, plantio.espaco_plantio, " +
	             "alimento.id_alimento, alimento.nome_alimento, alimento.tempo_colheita, alimento.qtd_irrigacao, alimento.preco_alimento, alimento.qtd_alimento " +
	             "FROM plantio " +
	             "INNER JOIN alimento ON plantio.id_alimento = alimento.id_alimento " +
	             "ORDER BY plantio.id_plantio " +
	             "WHERE plantio.id_plantio = ?";

	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    Plantio plantio = null;

	    try {
	        ps = getConnection().prepareStatement(sql);
	        ps.setInt(1, id_plantio);
	        rs = ps.executeQuery();

	        if (rs.next()) {
	        	
	        	plantio = new Plantio();
	            plantio.setId_plantio(rs.getInt("id_plantio"));
	            plantio.setData_plantio(rs.getDate("data_plantio"));
	            plantio.setEspaco_plantio(rs.getInt("espaco_plantio"));
	            
	            Alimento alimento = new Alimento();
	            alimento.setId_alimento(rs.getInt("id_alimento"));
	            alimento.setNome_alimento(rs.getString("nome_alimento"));
	            alimento.setTempo_colheita(rs.getInt("tempo_colheita"));
	            alimento.setQtd_irrigacao(rs.getInt("qtd_irrigacao"));
	            alimento.setPreco_alimento(rs.getInt("preco_alimento"));
	            alimento.setQtd_alimento(rs.getInt("qtd_alimento"));
	            
	            plantio.setAlimento(alimento);
	        }

	        if (plantio == null) {
	            System.out.println("Não foi encontrado um PLANTIO com o ID fornecido: " + id_plantio);
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível buscar o PLANTIO: " + e.getMessage());
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

	    return plantio;
	}
	
	/**
	 * Atualiza um plantio no banco de dados.
	 *
	 * @param plantio o objeto Plantio com as informações atualizadas
	 * @return true se o Plantio foi atualizado com sucesso, false caso contrário.
	 */
	public static boolean atualizarPlantio(@Valid Plantio plantio) {
		String sql = "UPDATE plantio SET data_plantio = ?, espaco_plantio = ?, id_alimento = ? WHERE id_plantio = ?";
		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setDate(1, plantio.getData_plantio());
			cs.setInt(2, plantio.getEspaco_plantio());
			cs.setInt(3, plantio.getAlimento().getId_alimento());
			cs.setInt(4, plantio.getId_plantio());
			
			int rowsAffected = cs.executeUpdate();

	        if (rowsAffected > 0) {
	            return true;
	        }

		} catch (SQLException e) {
			System.out.println("Não foi possível atualizar o PLANTIO no banco de dados: " + e.getMessage());
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
	 * Cadastra um novo plantio no banco de dados.
	 *
	 * @param plantio_novo o objeto Plantio a ser cadastrado
	 * @return o objeto Plantio cadastrado, ou null se o cadastro não foi bem-sucedido
	 */
	public static Plantio cadastrarPlantio(@Valid Plantio plantio_novo) {

		// @formatter:off
		String sql = "BEGIN INSERT INTO plantio ("
				+ " id_plantio,"
				+ " data_plantio,"
				+ " espaco_plantio,"
				+ " id_alimento"
				+ ") VALUES ("
				+ " SQ_PLANTIO.nextval,"
				+ " ?,"
				+ " ?,"
				+ " ?"
				+ ") "
				+ "RETURNING id_plantio INTO ?; END;";
		// @formatter:on

		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setDate(1, plantio_novo.getData_plantio());
			cs.setInt(2, plantio_novo.getEspaco_plantio());
			cs.setInt(3, plantio_novo.getAlimento().getId_alimento());
			cs.registerOutParameter(4, java.sql.Types.INTEGER);
			cs.executeUpdate();
			plantio_novo.setId_plantio(cs.getInt(4));

			return plantio_novo;

		} catch (SQLException e) {
			System.out.println("Não foi possível cadastrar novo PLANTIO no banco de dados: " + e.getMessage());
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
	 * Deleta um plantio do banco de dados pelo ID do plantio.
	 *
	 * @param id_plantio O ID do plantio a ser deletado.
	 * @return true se a plantio foi deletado com sucesso, false caso contrário.
	 */
	public static boolean deletarPlantio(int id_plantio) {

		Plantio plantio_deletar = null;
		String sql = "DELETE FROM plantio WHERE id_plantio = ?";
		PreparedStatement ps = null;
		plantio_deletar = buscarPlantioPorId(id_plantio);

		if (plantio_deletar == null) {
			return false;
		}

		try {
			ps = getConnection().prepareStatement(sql);
			ps.setInt(1, id_plantio);
			ps.executeUpdate();
			return true;

		} catch (SQLException e) {
			System.out.println("Não foi possível deletar o PLANTIO no banco de dados: " + e.getMessage());
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