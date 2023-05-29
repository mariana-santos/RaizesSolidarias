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

export default function Login() {

  const [email, setEmail] = useState('')
  const [errorEmail, setErrorEmail] = useState(null)

  const [senha, setSenha] = useState('')
  const [errorSenha, setErrorSenha] = useState(null)

  const [carregando, setCarregando] = useState(false)

  function handleSubmit(e) {

    e.preventDefault();

    if (validaEmail() && validaSenha()) {
      // setCarregando(true)

      // fetch(`http://localhost:8080/InvestiumAPI/rest/usuario/${email}/${senha}`)
      //   .then((resp) => resp.json())
      //   .then((data) => {
      //     setCarregando(false)
      //     if (data.nome && data.email && data.senha) {
      //       toast.success('Usuário autenticado! Aguarde para ser direcionado.')
      //       const dadosString = JSON.stringify(data);
      //       sessionStorage.setItem("dadosUsuario", dadosString);
      //       setUser(data)
      //       setTimeout(() => {
      //         window.location.href = '/perfil'
      //       }, 2000)
      //     } else {
      //       toast.error('Email ou senha incorretos.')
      //     }
      //   })
      //   .catch((error) => {
      //     console.error(error)
      //     setCarregando(false)
      //   });
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

        <form onSubmit={handleSubmit}>
          <h2>Bem vindo de volta!</h2>
          <small>Para continuar, por favor insira seus dados.</small>

          {/* <img src={ilustracao} /> */}

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

          {/* <a className="outros_links" href="#">Esqueceu a senha? <strong>clique aqui</strong></a> */}
          {/* <Link className="outros_links" to="/cadastro">Ainda não possui conta? <strong>clique aqui</strong></Link> */}

        </form>

      </main>

      <Footer />
    </div>
  )
}
