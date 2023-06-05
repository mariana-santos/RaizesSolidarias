import Menu from '../app/Components/Menu'
import Link from 'next/link'
import Footer from '../app/Components/Footer'
import Campo from '../app/Components/Campo'

import { Raleway } from 'next/font/google'
const font = Raleway({ subsets: ['latin'] })
import { Quicksand } from 'next/font/google'
const fontBody = Quicksand({ subsets: ['latin'] })

import '../app/globals.css'

import validator from "validator"
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import { useState } from 'react'

import { HiOutlineEnvelope, HiOutlineIdentification } from 'react-icons/hi2'
import { RiLockPasswordLine } from 'react-icons/ri'
import { RxPerson } from 'react-icons/rx'
import { BsTelephone } from 'react-icons/bs'

import { PatternFormat } from 'react-number-format';

import { useMutation } from 'react-query'

import '../app/styles/form.css'


export default function Cadastro() {

    const [nome, setNome] = useState('')
    const [errorNome, setErrorNome] = useState(null)

    const [email, setEmail] = useState('')
    const [errorEmail, setErrorEmail] = useState(null)

    const [senha, setSenha] = useState('')
    const [errorSenha, setErrorSenha] = useState(null)

    const [cpf, setCpf] = useState('')
    const [errorCpf, setErrorCpf] = useState(null)

    const [celular, setCelular] = useState('')
    const [errorCel, setErrorCel] = useState(null)

    const cadastrarUsuario = async (dados_usuario) => {
        const response = await fetch('http://localhost:8080/usuario', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_usuario),
        });
     
        // TODO: Verificar a razão de não vir response pra mostrar o erro
        const data = await response.json();

        if (!response.ok || data.error) {
            toast.error(response.error)
            throw new Error('Erro ao cadastrar o usuário');
        }
        
        else{
            console.log(data)
            sessionStorage.setItem('usuario', JSON.stringify(data));
            toast.success('Sucesso no cadastro! Aguarde para ser redirecionado')   
    
            //Limpando os dados
            setNome('')
            setCelular('')
            setCpf('')
            setEmail('')
            setCelular('')
            setSenha('') 
    
            setTimeout(() => {
                window.location.href = '/perfil'
            }, 2000)
        }

        return data;
    };

    const { mutate } = useMutation(cadastrarUsuario);

    function handleSubmit(e) {
        e.preventDefault();

        if (validaCampo(nome, setErrorNome) && validaEmail() && validaCampo(celular, setErrorCel)
            && validaCampo(cpf, setErrorCpf) && validaSenha()) {

            const dados_usuario = {
                cel_usuario: celular,
                cpf_usuario: cpf,
                email_usuario: email,
                id_usuario: 11,
                nome_usuario: nome,
                senha_usuario: senha,
                status_usuario: 'Ativo',
            };

            mutate(dados_usuario)
        }
    }

    function validaCampo(campo, setError) {
        console.log(campo.includes('_'), campo)
        //função pra validar se o campo tá vazio ou _ (vindos do patternFormat)
        if (!validator.isEmpty(campo) && !campo.includes('_')) {
            setError(null)
            return true
        }

        //se cair aqui o campo tá vazio
        setError('Campo obrigatório!')
        return false
    }

    function validaEmail() {
        //se for válido e não for vazio retorna true e remove o erro
        if (!validator.isEmpty(email) && validator.isEmail(email)) {
            setErrorEmail(null)
            return true
        }

        //se cair aqui tem algo errado e entram as validações especificas
        else {
            if (validator.isEmpty(email))
                setErrorEmail('Email é obrigatório!')

            if (!validator.isEmail(email))
                setErrorEmail('Email inválido!')

            //Futuramente aqui terá outro if validando se o email é encontrado na nossa base de dados
            return false
        }
    }

    function validaSenha() {
        if (!validator.isEmpty(senha) && validator.isLength(senha, { min: 8 })) {
            setErrorSenha(null)
            return true
        }
        else {
            if (!validator.isLength(senha, { min: 8 }))
                setErrorSenha('Senha muito curta!')

            if (senha == '') {
                setErrorSenha('Senha é obrigatória!')
            }
            return false
        }
    }

    return (
        <div className={fontBody.className}>
            <Menu />
            <main className='form-wrapper' id='login'>

                <form onSubmit={handleSubmit}>
                    <h2>Seja bem vindo!</h2>
                    <small>Para continuar, por favor insira seus dados.</small>

                    {/* <img src={ilustracao} /> */}

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
                        temMask
                    >
                        <PatternFormat
                            format="(##) 9#### ####"
                            allowEmptyFormatting mask="_"
                            onValueChange={(cel) => setCelular(cel.formattedValue)}
                        />
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
                    >
                        <PatternFormat
                            format="###.###.###-##"
                            allowEmptyFormatting mask="_"
                            onValueChange={(cpf) => setCpf(cpf.formattedValue)}
                        />
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

                    <button type="submit" className="btn btn_primary arrow">Cadastrar</button>

                    {/* <a className="outros_links" href="#">Esqueceu a senha? <strong>clique aqui</strong></a> */}
                    <Link className="outros_links" href="/login">Já possui conta? <strong>clique aqui</strong></Link>

                </form>

            </main>

            <Footer />
        </div>
    )
}
