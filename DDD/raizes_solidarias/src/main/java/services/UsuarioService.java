package services;

import dao.UsuarioDAO;
import model.Usuario;

/**
 * Classe de serviços para Usuario.
 *
 * @since 1.0
 * @version 1.0
 *
 * @see model.Usuario
 * @see dao.UsuarioDAO
 * @see controller.UsuarioResource
 * @see model.Doador
 * @see model.Receptor
 * @see model.Voluntario
 * 
 * @author Raízes Solidárias
 *
 */
public class UsuarioService {

	/**
	 * Verifica se um Usuario com o ID especificado existe.
	 *
	 * @param id_usuario o ID do Usuario
	 * @return true se um Usuario com o ID especificado existe, caso contrário, false
	 */
	public static boolean validarIdUsuario(int id_usuario) {
		return UsuarioDAO.buscarUsuarioPorId(id_usuario) != null;
	}

	/**
	 * Busca e retorna um Usuario pelo ID.
	 *
	 * @param id_usuario o ID do Usuario
	 * @return o Usuario correspondente ao ID, ou null se não encontrado
	 */
	public static Usuario exibirUsuarioPorId(int id_usuario) {
		return UsuarioDAO.buscarUsuarioPorId(id_usuario);
	}

	/**
	 * Atualiza um Usuario com as informações fornecidas.
	 *
	 * @param id_usuario o ID do Usuario a ser atualizado
	 * @param usuario o Usuario com as novas informações
	 * @return true se o Usuario foi atualizado com sucesso, caso contrário, false.
	 */
	public static boolean atualizarUsuario(int id_usuario, Usuario usuario) {
		Usuario usuario_atualizar = exibirUsuarioPorId(id_usuario);

		if (usuario_atualizar == null || usuario_atualizar.getId_usuario() != usuario.getId_usuario()) {
			return false;
		} else {
			if (UsuarioDAO.atualizarUsuario(usuario))
				return true;
			
			else
				return false;
		}
	}

	/**
	 * Cadastra um novo Usuario.
	 *
	 * @param usuario_novo o novo Usuario a ser cadastrado.
	 * @return o Usuario cadastrado.
	 */
	public static Usuario cadastrarUsuario(Usuario usuario_novo) {
		return UsuarioDAO.cadastrarUsuario(usuario_novo);
	}

	/**
	 * Exclui um Usuario pelo ID.
	 *
	 * @param id_usuario o ID do Usuario a ser excluído.
	 * @return true se o Usuario foi excluído com sucesso, caso contrário, false.
	 */
	public static boolean deletarUsuario(int id_usuario) {
		if (validarIdUsuario(id_usuario)) {
			return UsuarioDAO.deletarUsuario(id_usuario);
		} else {
			return false;
		}
	}
}