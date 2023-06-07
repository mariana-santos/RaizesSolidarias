package dao;

import java.sql.Connection;
import java.sql.SQLException;

import connection.ConnectionFactory;

/**
 * Classe repository.
 * 
 * Todo repositório deve estender esta classe, pois é responsável por estabelecer
 * a conexão com o banco de dados com base nos parâmetros do arquivo
 * application.properties.
 * 
 * @author Francis
 *
 */
public class Repository {

	protected static Connection connection;

	/**
	 * Construtor padrão.
	 */
	public Repository() {
		super();
		getConnection();
	}

	/**
	 * Obtém uma conexão com o banco de dados.
	 * 
	 * @see ConnectionFactory#getInstance()
	 * 
	 * @return A conexão com o banco de dados
	 */
	public static Connection getConnection() {
		try {
			connection = ConnectionFactory.getInstance().getConnection();
			return connection;
		} catch (Exception e) {
			System.out.println("Erro nos parâmetros da conexão com o banco de dados: " + e.getMessage());
		}
		return null;
	}

	/**
	 * Fecha a conexão com o banco de dados.
	 */
	public static void closeConnection() {

		try {
			// Se a conexão não estiver fechada, feche-a
			if (!connection.isClosed()) {
				connection.close();
			}
		} catch (SQLException ex) {
			System.out.println("Erro ao encerrar conexão: " + ex.getMessage());
		}
	}
}
