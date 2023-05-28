package services;

import dao.UsuarioDAO;
import model.Usuario;

/**
 * Classe de serviços para Usuário.
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
	 * Verifica se um Usuário com o ID especificado existe.
	 *
	 * @param id_usuario o ID do Usuário
	 * @return true se um Usuário com o ID especificado existe, caso contrário, false
	 */
	public static boolean validarIdUsuario(int id_usuario) {
		return UsuarioDAO.buscarUsuarioPorId(id_usuario) != null;
	}

	/**
	 * Busca e retorna um Usuário pelo ID.
	 *
	 * @param id_usuario o ID do Usuário
	 * @return o Usuário correspondente ao ID, ou null se não encontrado
	 */
	public static Usuario exibirUsuarioPorId(int id_usuario) {
		return UsuarioDAO.buscarUsuarioPorId(id_usuario);
	}

	/**
	 * Atualiza um Usuário com as informações fornecidas.
	 *
	 * @param id_usuario o ID do Usuário a ser atualizado
	 * @param usuario o Usuário com as novas informações
	 * @return o Usuário atualizado, ou null se o Usuário não existir
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
	 * Cadastra um novo Usuário.
	 *
	 * @param usuario_novo o novo Usuário a ser cadastrado
	 * @return o Usuário cadastrado
	 */
	public static Usuario cadastrarUsuario(Usuario usuario_novo) {
		return UsuarioDAO.cadastrarUsuario(usuario_novo);
	}

	/**
	 * Exclui um Usuário pelo ID.
	 *
	 * @param id_usuario o ID do Usuário a ser excluído
	 * @return true se o Usuário foi excluído com sucesso, caso contrário, false
	 */
	public static boolean deletarUsuario(int id_usuario) {
		if (validarIdUsuario(id_usuario)) {
			return UsuarioDAO.deletarUsuario(id_usuario);
		} else {
			return false;
		}
	}
}