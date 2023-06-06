package connection;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

/**
 * Classe com padrão Singleton e Factory que fornece conexão com o banco de dados.
 * 
 * Caso o usuário tenha definido o parâmetro "datasource.drop-delete-table-and-dados" como true,
 * a estrutura do banco de dados será recriada com valores padrão.
 * 
 * @since 1.0
 * @version 1.0
 * 
 * @author Francis
 */
public final class ConnectionFactory {

	private static volatile ConnectionFactory instance;

	private String url;
	private String user;
	private String pass;
	private String driver;

	private volatile Connection conexao;

	/**
	 * Construtor privado.
	 * 
	 * @param url    A URL de conexão com o banco de dados.
	 * @param user   O nome de usuário para autenticação.
	 * @param pass   A senha do usuário para autenticação.
	 * @param driver O nome da classe do driver JDBC.
	 */
	private ConnectionFactory(String url, String user, String pass, String driver) {
		super();
		this.url = url;
		this.user = user;
		this.pass = pass;
		this.driver = driver;
	}

	/**
	 * Retorna a instância única da classe ConnectionFactory.
	 * 
	 * @return A instância única da classe ConnectionFactory.
	 */
	public static ConnectionFactory getInstance() {

		ConnectionFactory result = instance;

		if (result != null) {
			return result;
		}

		Properties prop = new Properties();
		FileInputStream file = null;
		String debugar = "";
		try {
			file = new FileInputStream("./src/main/resource/application.properties");
			prop.load(file);

			String url = prop.getProperty("datasource.url");
			String user = prop.getProperty("datasource.username");
			String pass = prop.getProperty("datasource.password");
			String driver = prop.getProperty("datasource.driver-class-name");
			debugar = prop.getProperty("datasource.debugar");
			file.close();

			if (debugar != null && debugar.equals("true")) {
				System.out.println("\n\n************************  CONNECTION PROPERTIES  **************************\n");
				System.out.println("JDBC URL: " + url);
				System.out.println("USER: " + user);
				System.out.println("PASSWORD: *******");
				System.out.println("DRIVER: " + driver);
			}

			synchronized (ConnectionFactory.class) {
				if (instance == null) {
					instance = new ConnectionFactory(url, user, pass, driver);
				}
				return instance;
			}

		} catch (FileNotFoundException e) {
			System.out.println("Não foi possível encontrar o arquivo de propriedades: " + e.getMessage());
		} catch (IOException e) {
			System.out.println("Não foi possível ler a propriedade: " + e.getMessage());
		} finally {

			if (debugar != null && debugar.equals("true"))
				System.out.println("\n**************************************************************************\n");
		}
		return null;

	}

	/**
	 * Retorna a conexão com o banco de dados.
	 * 
	 * @return A conexão com o banco de dados.
	 * @throws RuntimeException se os parâmetros de conexão não estiverem definidos corretamente.
	 */
	public Connection getConnection() {

		synchronized (Connection.class) {

			try {

				if (this.conexao != null && !this.conexao.isClosed()) {
					return this.conexao;
				}

				if (this.getDriver() == null || this.getDriver().equals("")) {
					System.out.println(
							"\nInforme os dados de conexão no arquivo application.properties [ datasource.driver-class-name ]");
					throw new RuntimeException(
							"Informe os dados de conexão no arquivo application.properties [ datasource.driver-class-name ]");
				}

				if (this.getUrl() == null || this.getUrl().equals("")) {
					System.out.println(
							"\nInforme os dados de conexão no arquivo application.properties [ datasource.url ]");
					throw new RuntimeException(
							"Informe os dados de conexão no arquivo application.properties [ datasource.url ]");
				}

				if (this.getUser() == null || this.getUser().equals("")) {
					System.out.println(
							"\nInforme os dados de conexão no arquivo application.properties [ datasource.username ]");
					throw new RuntimeException(
							"Informe os dados de conexão no arquivo application.properties [ datasource.username ]");
				}

				Class.forName(this.getDriver());

				this.conexao = DriverManager.getConnection(this.getUrl(), this.getUser(), this.getPass());

			} catch (ClassNotFoundException e) {
				System.out.println("Não foi possível encontrar o driver de conexão: " + e.getMessage());
				System.exit(1);
			} catch (SQLException sqle) {
				System.out.println("Erro nos parâmetros da conexão com o banco de dados: " + sqle.getMessage());
				System.exit(1);
			}
			return this.conexao;
		}

	}

	/**
	 * Retorna a URL de conexão com o banco de dados.
	 * 
	 * @return A URL de conexão com o banco de dados.
	 */
	public String getUrl() {
		return url;
	}

	/**
	 * Retorna o nome de usuário para autenticação.
	 * 
	 * @return O nome de usuário para autenticação.
	 */
	public String getUser() {
		return user;
	}

	/**
	 * Retorna a senha do usuário para autenticação.
	 * 
	 * @return A senha do usuário para autenticação.
	 */
	public String getPass() {
		return pass;
	}

	/**
	 * Retorna o nome da classe do driver JDBC.
	 * 
	 * @return O nome da classe do driver JDBC.
	 */
	public String getDriver() {
		return driver;
	}

}
