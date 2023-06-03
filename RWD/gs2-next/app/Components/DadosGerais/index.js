import { useEffect, useState } from "react"

import Campo from "../Campo"

import validator from "validator"

import { HiOutlineEnvelope, HiOutlineIdentification } from 'react-icons/hi2'
import { RiLockPasswordLine } from 'react-icons/ri'
import { RxPerson } from 'react-icons/rx'
import { BsTelephone } from 'react-icons/bs'

import { PatternFormat } from 'react-number-format';

import { useMutation } from 'react-query'

import { toast } from "react-toastify"

import '../../styles/form.css'

export default function DadosGerais() {
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

    const [id, setId] = useState(0)

    useEffect(() => {
        const usuario = typeof window !== 'undefined' ? JSON.parse(sessionStorage.getItem("usuario")) : null;

        //populando os campos do usuário com os valores existentes
        if (usuario) {
            setNome(usuario.nome_usuario);
            setCelular(usuario.cel_usuario);
            setCpf(usuario.cpf_usuario);
            setSenha(usuario.senha_usuario)
            setEmail(usuario.email_usuario)
            setId(usuario.id_usuario)
        }
    }, [])

    const handleAtualizarUsuario = async (dados_usuario) => {
        const response = await fetch(`http://localhost:8080/usuario/${dados_usuario.id_usuario}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_usuario),
        });

        if (!response.ok) {
            toast.error('Erro ao atualizar o usuário');
            throw new Error('Erro ao atualizar o usuário');
        }
    
        sessionStorage.setItem('usuario', JSON.stringify(dados_usuario));
        toast.success('Sucesso ao atualizar os dados!');
    };

    const { mutate } = useMutation(handleAtualizarUsuario);

    function handleSubmit(e) {
        e.preventDefault();

        if (validaCampo(nome, setErrorNome) && validaEmail() && validaCampo(celular, setErrorCel)
            && validaCampo(cpf, setErrorCpf) && validaSenha()) {

            const dados_usuario = {
                cel_usuario: celular,
                cpf_usuario: cpf,
                email_usuario: email,
                id_usuario: id,
                nome_usuario: nome,
                senha_usuario: senha,
                status_usuario: 'Ativo'
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

    function validaCampo(campo, setError) {
        //função pra validar se o campo tá vazio ou _ (vindos do patternFormat)
        if (!validator.isEmpty(campo) && !campo.includes('_')) {
            setError(null)
            return true
        }

        //se cair aqui o campo tá vazio
        setError('Campo obrigatório!')
        return false
    }

    return (
        <form onSubmit={handleSubmit}>

            <h2>Olá, {nome.split(' ')[0]}!</h2>
            <small>Esses são seus dados de cadastro</small>

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
                    value={celular}
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
                temMask
            >
                <PatternFormat
                    format="###.###.###-##"
                    allowEmptyFormatting mask="_"
                    value={cpf}
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

            {/* TODO: ADICIONAR OS CAMPOS DE ENDEREÇO CASO ESSE USUARIO SEJA UM TRANSPORTADOR */}

            <button type="submit" className="btn btn_primary arrow">Salvar</button>

        </form>
    )
}