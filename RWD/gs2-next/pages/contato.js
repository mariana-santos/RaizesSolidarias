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

import '../app/styles/form.css'

import { validaCampo, validaEmail } from '../app/utils/validacao'

export default function Login() {

  const [email, setEmail] = useState('')
  const [errorEmail, setErrorEmail] = useState(null)

  const [nome, setNome] = useState('')
  const [errorNome, setErrorNome] = useState(null)

  const [mensagem, setMensagem] = useState('')
  const [errorMensagem, setErrorMensagem] = useState(null)

  function handleSubmit(e) {
    e.preventDefault();

    if (validaEmail(email, setErrorEmail) && validaCampo(nome, setErrorNome) && validaCampo(mensagem, setErrorMensagem)) {

      toast.success('Obrigado por entrar em contato! Em breve te retornaremos')

      //Limpando os dados
      setEmail('')
      setNome('')
      setMensagem('')
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
          <h2>Fale conosco</h2>
          <small>Para nos enviar alguma mensagem, por favor insira seus dados.</small>

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
            label="Nome"
            id="nome"
            placeholder="Digite seu nome"
            type="text"
            errorMsg={errorNome}
            value={nome}
            onChange={e => setNome(e.target.value)}
          />

          <Campo
            label="Mensagem"
            id="mensagem"
            placeholder="Digite sua mensagem"
            type="text"
            errorMsg={errorMensagem}
            value={mensagem}
            onChange={e => setMensagem(e.target.value)}
          />

          <button type="submit" className="btn btn_primary arrow">Enviar mensagem</button>

        </form>

      </main>

      <Footer />
    </div>
  )
}
