import Menu from '../app/Components/Menu'
import Link from 'next/link'
import Footer from '../app/Components/Footer'
import Campo from '../app/Components/Campo'

import { Raleway } from 'next/font/google'
const font = Raleway({ subsets: ['latin'] })
import { Quicksand } from 'next/font/google'
const fontBody = Quicksand({ subsets: ['latin'] })

import '../app/globals.css'

import validator from "validator";
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import { useState } from 'react'

import { HiOutlineEnvelope } from 'react-icons/hi2'
import { RiLockPasswordLine } from 'react-icons/ri'

import '../app/styles/form.css'

import { useMutation } from 'react-query'

import { useRouter } from 'next/router';

export default function Login() {

  const router = useRouter();

  const [email, setEmail] = useState('')
  const [errorEmail, setErrorEmail] = useState(null)

  const [senha, setSenha] = useState('')
  const [errorSenha, setErrorSenha] = useState(null)

  const handleLogin = async (dados_usuario) => {
    const response = await fetch('http://localhost:8080/usuario/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dados_usuario),
    });

    const data = await response.json();

    console.log(data)

    if (!response.ok || data.error) {
      toast.error(data.error)
      throw new Error('Erro ao fazer login');
    }

    else {
      sessionStorage.setItem('usuario', JSON.stringify(data));

      const responseReceptor = await fetch('http://localhost:8080/receptor/' + data.id_usuario)
      .then(resp => resp.json())
      .then(data => !data.error && sessionStorage.setItem('receptor', JSON.stringify(data)))

      const responseVoluntario = await fetch('http://localhost:8080/voluntario/' + data.id_usuario)
      .then(resp => resp.json())
      .then(data => !data.error && sessionStorage.setItem('voluntario', JSON.stringify(data)))

      const responseDoador = await fetch('http://localhost:8080/doador/' + data.id_usuario)
      .then(resp => resp.json())
      .then(data => !data.error && sessionStorage.setItem('doador', JSON.stringify(data)))

      toast.success('Sucesso no login! Aguarde para ser redirecionado')
      //Limpando os dados
      setEmail('')
      setSenha('')

      router.push('/perfil')
    }

    return data;
  };

  const { mutate } = useMutation(handleLogin);

  function handleSubmit(e) {
    e.preventDefault();

    if (validaEmail() && validaSenha()) {

      const dados_usuario = {
        cel_usuario: '(11) 90000-0000)',
        cpf_usuario: "000.000.000-00",
        email_usuario: email,
        id_usuario: 1,
        nome_usuario: '',
        senha_usuario: senha,
        status_usuario: 'Ativo',
      };

      mutate(dados_usuario)
    }
  }

  function validaEmail() {

    //se for válido e não for vazio retorna true e remove o erro
    if (email !== '' && email !== null && validator.isEmail(email)) {
      setErrorEmail(null)
      return true
    }

    //se cair aqui tem algo errado e entram as validações especificas
    else {
      if (email === '' || email === null || email === undefined) {
        setErrorEmail('Email é obrigatório!')
        return false
      }

      if (!validator.isEmail(email)) {
        setErrorEmail('Email inválido!')
        return false
      }
    }

  }

  function validaSenha() {
    if (senha !== '' && senha !== null) {
      setErrorSenha(null)
      return true
    }
    else {
      setErrorSenha('Senha é obrigatória!')
      return false
    }
  }

  return (
    <div className={fontBody.className}>
      <Menu />
      <main className='form-wrapper' id='login'>

        <ToastContainer
          position="bottom-right"
          autoClose={2000}
          closeOnClick
          pauseOnHover
        />

        <form onSubmit={handleSubmit}>
          <h2>Bem vindo de volta!</h2>
          <small>Para continuar, por favor insira seus dados.</small>

          <Campo
            label="Email"
            id="email"
            placeholder="Digite seu email"
            type="email"
            icon={<HiOutlineEnvelope />}
            errorMsg={errorEmail}
            value={email}
            onChange={e => setEmail(e.target.value)}
          />

          <Campo
            label="Senha"
            id="senha"
            placeholder="Digite sua senha"
            type="password"
            icon={<RiLockPasswordLine />}
            errorMsg={errorSenha}
            value={senha}
            onChange={e => setSenha(e.target.value)}
          />

          <button type="submit" className="btn btn_primary arrow">Entrar</button>

          <Link className="outros_links" href="/cadastro">Ainda não possui conta? <strong>clique aqui</strong></Link>

        </form>

      </main>

      <Footer />
    </div>
  )
}
