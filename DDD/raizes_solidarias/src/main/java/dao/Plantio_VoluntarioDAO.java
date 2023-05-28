package dao;

import java.sql.CallableStatement;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import jakarta.validation.Valid;
import model.Alimento;
import model.Voluntario;
import model.Plantio;
import model.Plantio_Voluntario;

/**
 * Classe de acesso a dados para Plantio_Voluntario.
 * 
 * Essa classe oferece métodos para manipulação dos dados relacionados a tabela Plantio_Voluntario no banco de dados.
 * Ela estende a classe Repository, que fornece a funcionalidade de conexão com o banco de dados.
 * 
 * @since 1.0
 * @version 1.0
 * 
 * @see model.Plantio_Voluntario
 * @see services.Plantio_VoluntarioService
 * @see controller.Plantio_VoluntarioResource
 * @see model.Plantio
 * @see model.Voluntario
 * @see dao.Repository
 * 
 * @author Raízes Solidárias
 * 
 */
public class Plantio_VoluntarioDAO extends Repository {
	
	/**
	 * Retorna uma lista de todos os Plantio_Voluntarios cadastrados no banco de dados.
	 *
	 * @return uma lista de Plantio_Voluntarios.
	 */
	public ArrayList<Plantio_Voluntario> listarPlantio_Voluntarios() {
		String sql = "SELECT pv.id_plantio, p.data_plantio, p.espaco_plantio, p.alimento,"
				+ " u.id_usuario, u.cpf_usuario, u.nome_usuario, u.email_usuario, u.cel_usuario, u.senha_usuario, u.status_usuario,"
				+ " v.data_registro_voluntario"
	            + " FROM Plantio_Voluntario pv"
	            + " JOIN Plantio p ON pv.id_plantio = p.id_plantio"
	            + " JOIN Usuario u ON pv.id_usuario = u.id_usuario"
	            + " JOIN Voluntario v ON u.id_usuario = v.id_usuario"
	            + " ORDER BY pv.id_usuario";

	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Plantio_Voluntario> listaPlantio_Voluntarios = new ArrayList<>();

	    try {
	        ps = getConnection().prepareStatement(sql);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	            Plantio_Voluntario plantio_voluntario = new Plantio_Voluntario();

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

	            plantio_voluntario.setPlantio(plantio);

	            Voluntario voluntario = new Voluntario();
	            voluntario.setId_usuario(rs.getInt("id_usuario"));
				voluntario.setCpf_usuario(rs.getString("cpf_usuario"));
				voluntario.setNome_usuario(rs.getString("nome_usuario"));
				voluntario.setEmail_usuario(rs.getString("email_usuario"));
				voluntario.setCel_usuario(rs.getString("cel_usuario"));
				voluntario.setSenha_usuario(rs.getString("senha_usuario"));
				voluntario.setStatus_usuario(rs.getString("status_usuario"));
				voluntario.setData_registro_voluntario(rs.getDate("data_registro_voluntario"));
				
				plantio_voluntario.setVoluntario(voluntario);
				
	            listaPlantio_Voluntarios.add(plantio_voluntario);
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível consultar a listagem da tabela PLANTIO_VOLUNTARIO: " + e.getMessage());
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

	    return listaPlantio_Voluntarios;
	}
	
	/**
	 * Retorna o Plantio_Voluntario cadastrados no banco de dados de acordo com o ID do Plantio.
	 *
	 * @return uma Plantio_Voluntario de acordo com o ID do Plantio.
	 */
	public ArrayList<Plantio_Voluntario> buscarPlantio_VoluntarioPorIdPlantio(int id_plantio) {
		String sql = "SELECT pv.id_plantio, p.data_plantio, p.espaco_plantio, p.alimento,"
				+ " u.id_usuario, u.cpf_usuario, u.nome_usuario, u.email_usuario, u.cel_usuario, u.senha_usuario, u.status_usuario,"
				+ " v.data_registro_voluntario"
	            + " FROM Plantio_Voluntario pv"
	            + " JOIN Plantio p ON pv.id_plantio = p.id_plantio"
	            + " JOIN Usuario u ON pv.id_usuario = u.id_usuario"
	            + " JOIN Voluntario v ON u.id_usuario = v.id_usuario"
	            + " ORDER BY pv.id_usuario"
	            + " WHERE pv.id_plantio = ?";

	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Plantio_Voluntario> listaPlantio_Voluntarios = new ArrayList<>();
	    
	    try {
	        ps = getConnection().prepareStatement(sql);
	        ps.setInt(1, id_plantio);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	        	Plantio_Voluntario plantio_voluntario_buscado = new Plantio_Voluntario();
	        	
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

	            plantio_voluntario_buscado.setPlantio(plantio);

	            Voluntario voluntario = new Voluntario();
	            voluntario.setId_usuario(rs.getInt("id_usuario"));
				voluntario.setCpf_usuario(rs.getString("cpf_usuario"));
				voluntario.setNome_usuario(rs.getString("nome_usuario"));
				voluntario.setEmail_usuario(rs.getString("email_usuario"));
				voluntario.setCel_usuario(rs.getString("cel_usuario"));
				voluntario.setSenha_usuario(rs.getString("senha_usuario"));
				voluntario.setStatus_usuario(rs.getString("status_usuario"));
				voluntario.setData_registro_voluntario(rs.getDate("data_registro_voluntario"));
				
				plantio_voluntario_buscado.setVoluntario(voluntario);
				
				listaPlantio_Voluntarios.add(plantio_voluntario_buscado);
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível buscar o Plantio_Voluntario com o ID do Plantio " + id_plantio + ": " + e.getMessage());
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

	    return listaPlantio_Voluntarios;
	}
	
	/**
	 * Retorna o Plantio_Voluntario cadastrados no banco de dados de acordo com o ID do Voluntario.
	 *
	 * @return uma Plantio_Voluntario de acordo com o ID do Voluntario.
	 */
	public ArrayList<Plantio_Voluntario> buscarPlantio_VoluntarioPorIdUsuario(int id_usuario) {
		String sql = "SELECT pv.id_plantio, p.data_plantio, p.espaco_plantio, p.alimento,"
				+ " u.id_usuario, u.cpf_usuario, u.nome_usuario, u.email_usuario, u.cel_usuario, u.senha_usuario, u.status_usuario,"
				+ " v.data_registro_voluntario"
	            + " FROM Plantio_Voluntario pv"
	            + " JOIN Plantio p ON pv.id_plantio = p.id_plantio"
	            + " JOIN Usuario u ON pv.id_usuario = u.id_usuario"
	            + " JOIN Voluntario v ON u.id_usuario = v.id_usuario"
	            + " ORDER BY pv.id_usuario"
	            + " WHERE pv.id_usuario = ?";

	    PreparedStatement ps = null;
	    ResultSet rs = null;
	    ArrayList<Plantio_Voluntario> listaPlantio_Voluntarios = new ArrayList<>();
	    
	    try {
	        ps = getConnection().prepareStatement(sql);
	        ps.setInt(1, id_usuario);
	        rs = ps.executeQuery();

	        while (rs.next()) {
	        	Plantio_Voluntario plantio_voluntario_buscado = new Plantio_Voluntario();
	        	
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

	            plantio_voluntario_buscado.setPlantio(plantio);

	            Voluntario voluntario = new Voluntario();
	            voluntario.setId_usuario(rs.getInt("id_usuario"));
				voluntario.setCpf_usuario(rs.getString("cpf_usuario"));
				voluntario.setNome_usuario(rs.getString("nome_usuario"));
				voluntario.setEmail_usuario(rs.getString("email_usuario"));
				voluntario.setCel_usuario(rs.getString("cel_usuario"));
				voluntario.setSenha_usuario(rs.getString("senha_usuario"));
				voluntario.setStatus_usuario(rs.getString("status_usuario"));
				voluntario.setData_registro_voluntario(rs.getDate("data_registro_voluntario"));
				
				plantio_voluntario_buscado.setVoluntario(voluntario);
				
				listaPlantio_Voluntarios.add(plantio_voluntario_buscado);
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível buscar o Plantio_Voluntario com o ID do Voluntario " + id_usuario + ": " + e.getMessage());
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

	    return listaPlantio_Voluntarios;
	}
	
	/**
	 * Atualiza um Plantio_Voluntario no banco de dados.
	 *
	 * @param id_plantio		  	o id do plantio a ser atualizado.
	 * @param id_usuario 		o id da voluntario a ser atualizada.
	 * @return true se o Plantio_Voluntario for atualizado com sucesso, false caso contrário
	 */
	public static boolean atualizarPlantio_Voluntario(int id_plantio, int id_usuario) {
		String sql = "UPDATE plantio_voluntario SET id_plantio = ?, id_usuario = ? WHERE id_plantio = ? AND id_usuario = ?";
		CallableStatement cs = null;

		try {
			cs = getConnection().prepareCall(sql);
			cs.setInt(1, id_plantio);
			cs.setInt(2, id_usuario);
			cs.setInt(3, id_plantio);
			cs.setInt(4, id_usuario);

			int rowsAffected = cs.executeUpdate();

	        if (rowsAffected > 0) {
	            return true;
	        }

		} catch (SQLException e) {
			System.out.println("Não foi possível atualizar o PLANTIO_VOLUNTARIO no banco de dados: " + e.getMessage());
			return false;
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
	 * Cadastra um novo Plantio_Voluntario no banco de dados.
	 *
	 * @param plantio_voluntario_novo o novo Plantio_Voluntario a ser cadastrado
	 * @return o Plantio_Voluntario cadastrado ou null se o cadastro falhar
	 */
	public static Plantio_Voluntario cadastrarPlantio_Voluntario(@Valid Plantio_Voluntario plantio_voluntario_novo) {
	    String sql = "INSERT INTO plantio_voluntario ("
	            + "    id_plantio,"
	            + "    id_usuario"
	            + ") VALUES ("
	            + "    ?,"
	            + "    ?"
	            + ")";

	    PreparedStatement ps = null;
	    ResultSet rs = null;

	    try {
	        ps = getConnection().prepareStatement(sql, new String[] {"id_plantio", "id_usuario"});
	        ps.setInt(1, plantio_voluntario_novo.getPlantio().getId_plantio());
	        ps.setInt(2, plantio_voluntario_novo.getVoluntario().getId_usuario());
	        ps.executeUpdate();
	        rs = ps.getGeneratedKeys();
	        if (rs.next()) {
	            plantio_voluntario_novo.getPlantio().setId_plantio(rs.getInt("id_plantio"));
	            plantio_voluntario_novo.getVoluntario().setId_usuario(rs.getInt("id_usuario"));
	        }

	        return plantio_voluntario_novo;
	    } catch (SQLException e) {
	        System.out.println("Não foi possível cadastrar novo PLANTIO_VOLUNTARIO no banco de dados: " + e.getMessage());
	    } finally {
	        if (rs != null) {
	            try {
	                rs.close();
	            } catch (SQLException e) {
	                System.out.println("Não foi possível fechar o ResultSet: " + e.getMessage());
	            }
	        }
	        if (ps != null) {
	            try {
	                ps.close();
	            } catch (SQLException e) {
	                System.out.println("Não foi possível fechar o PreparedStatement: " + e.getMessage());
	            }
	        }
	    }

	    return null;
	}

	/**
	 * Deleta um Plantio_Voluntario do banco de dados.
	 *
	 * @param id_plantio	o id do plantio do Plantio_Voluntario a ser deletado
	 * @param id_usuario 	o id do voluntario do Plantio_Voluntario a ser deletado
	 * @return true se o Plantio_Voluntario for deletado com sucesso, false caso contrário
	 */
	public static boolean deletarPlantio_Voluntario(int id_plantio, int id_usuario) {
	    String sql = "DELETE FROM plantio_voluntario WHERE id_plantio = ? AND id_usuario = ?";
	    PreparedStatement ps = null;

	    try {
	        ps = getConnection().prepareStatement(sql);
	        ps.setInt(1, id_plantio);
	        ps.setInt(2, id_usuario);
	        int rowsAffected = ps.executeUpdate();

	        if (rowsAffected > 0) {
	            return true;
	        }

	    } catch (SQLException e) {
	        System.out.println("Não foi possível deletar o PLANTIO_VOLUNTARIO no banco de dados: " + e.getMessage());
	    } finally {
	        if (ps != null) {
	            try {
	                ps.close();
	            } catch (SQLException e) {
	                System.out.println("Não foi possível fechar o PreparedStatement: " + e.getMessage());
	            }
	        }
	    }

	    return false;
	}
}