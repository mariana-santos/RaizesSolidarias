import { useState } from "react"

import Campo from "../Campo"

import validator from "validator"

import { HiOutlineEnvelope, HiOutlineIdentification } from 'react-icons/hi2'
import { RiLockPasswordLine } from 'react-icons/ri'
import { RxPerson } from 'react-icons/rx'
import { BsTelephone } from 'react-icons/bs'

import { PatternFormat } from 'react-number-format';

import '../../styles/form.css'

import './style.css'

import { Switch, FormControlLabel } from "@mui/material"

export default function AreaVoluntario() {
    const [nome, setNome] = useState('Mariana Santos')
    const [errorNome, setErrorNome] = useState(null)

    const [email, setEmail] = useState('mariana@gmail.com')
    const [errorEmail, setErrorEmail] = useState(null)

    const [senha, setSenha] = useState('senha123')
    const [errorSenha, setErrorSenha] = useState(null)

    const [cpf, setCpf] = useState('')
    const [errorCpf, setErrorCpf] = useState(null)

    const [celular, setCelular] = useState('(11) 9 5042-6440')
    const [errorCel, setErrorCel] = useState(null)

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
        <form onSubmit={handleSubmit}>
            <div className="row-heading">
                <div className="heading">
                    <h2>Olá, Mariana!</h2>
                    <small>Bem vindo(a) à área de voluntário! Aqui você pode agendar suas visitas para contribuição da nossa horta solidária.</small>
                </div>

                <div className="wrap-switch">
                    <FormControlLabel
                        value="habilitado"
                        control={<Switch color="primary" />}
                        label="Habilitar área do voluntário"
                        labelPlacement="start"
                    />
                </div>
            </div>


            <Campo
                label="Nome"
                id="nome"
                placeholder="Digite seu nome"
                type="text"
                icon={<RxPerson />}
                errorMsg={errorNome}
                value={nome}
                onChange={e => setNome(e.target.value)}
            />

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
                label="Celular"
                id="celular"
                placeholder="Digite seu celular"
                type="text"
                icon={<BsTelephone />}
                errorMsg={errorCel}
                value={celular}
                onChange={e => setCelular(e.target.value)}
                temMask
            >
                <PatternFormat format="(##) 9 #### ####" allowEmptyFormatting mask="_" defaultValue="(11) 9 5042 6440" />
            </Campo>

            <Campo
                label="CPF"
                id="cpf"
                placeholder="Digite seu CPF"
                type="text"
                icon={<HiOutlineIdentification />}
                errorMsg={errorCpf}
                value={cpf}
                temMask
                onChange={e => setCpf(e.target.value)}
            >
                <PatternFormat format="###.###.###-##" allowEmptyFormatting mask="_" />
            </Campo>

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

            <button type="submit" className="btn btn_primary arrow">Salvar</button>

        </form>
    )
}