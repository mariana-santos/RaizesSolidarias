import { useEffect, useState } from "react"

import Campo from "../Campo"

import { HiOutlineEnvelope, HiOutlineIdentification } from 'react-icons/hi2'
import { RiLockPasswordLine } from 'react-icons/ri'
import { RxPerson } from 'react-icons/rx'
import { BsTelephone } from 'react-icons/bs'

import { PatternFormat } from 'react-number-format';

import { useMutation } from 'react-query'

import { toast } from "react-toastify"

import { GiWeight } from "react-icons/gi"

import '../../styles/form.css'

import { validaEmail, validaSenha, validaCampo, validaNumber } from "../../utils/validacao"

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

    const [receptor, setReceptor] = useState(null)

    const [carga, setCarga] = useState(1);
    const [errorCarga, setErrorCarga] = useState(null);

    const [cep, setCep] = useState('');
    const [errorCep, setErrorCep] = useState(null);

    const [logradouro, setLogradouro] = useState('')
    const [errorLogradouro, setErrorLogradouro] = useState(null)

    const [numero, setNumero] = useState('')
    const [errorNumero, setErrorNumero] = useState(null)

    const [complemento, setComplemento] = useState('')

    const [endereco, setEndereco] = useState(null)

    useEffect(() => {
        const usuario = JSON.parse(sessionStorage.getItem("usuario"));

        //populando os campos do usuário com os valores existentes
        if (usuario) {
            setNome(usuario.nome_usuario);
            setCelular(usuario.cel_usuario);
            setCpf(usuario.cpf_usuario);
            setSenha(usuario.senha_usuario)
            setEmail(usuario.email_usuario)
            setId(usuario.id_usuario)
        }

        const dadosReceptor = JSON.parse(sessionStorage.getItem("receptor"));

        //populando os campos do usuário com os valores existentes
        if (dadosReceptor) {
            setReceptor(dadosReceptor)
            setCarga(usuario.carga_usuario);
        }

    }, [])

    useEffect(() => {
        if (cep.length == 8) {
            const cep_formatado = cep.replace('-', '')
            fetch(`https://viacep.com.br/ws/${cep_formatado}/json/`)
                .then(resp => resp.json())
                .then(data => {
                    if (data.localidade !== 'São Paulo') {
                        toast.error('Para transportar os alimentos pros destinos necessitados você precisa residir em São Paulo!')
                        setCep('')
                        setLogradouro('')
                        setComplemento('')
                    }
                    else if (data.localidade === 'São Paulo') {
                        setLogradouro(data.logradouro)
                        setComplemento(data.complemento)
                        setErrorCep(null)
                    }
                })
                .catch(() => {
                    toast.error('CEP inválido! Por favor, digite novamente')
                    setCep('')
                    setLogradouro('')
                    setComplemento('')
                });
        }
    }, [cep])

    const atualizarReceptor = async (dados_receptor) => {
        const response = await fetch('http://localhost:8080/receptor/' + dados_receptor.id_usuario, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_receptor),
        });

        if (!response.ok) toast.error('Erro ao atualizar endereço!')

        else {
            const data = await response.json();
            sessionStorage.setItem('receptor', JSON.stringify(data));
            toast.success('Sucesso ao atualizar endereço!')
        }
    };

    const atualizarReceptorMutation = useMutation(atualizarReceptor);

    function handleAtualizarReceptor() {

        if (validaNumber(carga, setErrorCarga) && validaCampo(cep, setErrorCep) &&
            validaCampo(logradouro, setErrorLogradouro) && validaCampo(numero, setErrorNumero)) {

            const cep_formatado = cep.replace('-', '')
            fetch(`http://localhost:8080/endereco/${cep_formatado}/${numero}`)
                .then(resp => resp.json())
                .then(data => {
                    setEndereco(data.endereco)
                })
                .catch((error) => {
                    console.log(error)
                    toast.error('Endereço inválido! Por favor, digite novamente')
                    setCep('')
                    setLogradouro('')
                    setComplemento('')
                });

            const usuario_receptor = {
                cel_usuario: celular,
                cpf_usuario: cpf,
                email_usuario: email,
                id_usuario: id,
                nome_usuario: nome,
                senha_usuario: senha,
                status_usuario: 'Ativo',
                carga_receptor: carga,
                endereco_receptor: endereco
            }

            atualizarReceptorMutation.mutate(usuario_receptor)
        }
    }

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

    const atualizarUsuarioMutation = useMutation(handleAtualizarUsuario);

    function handleSubmit(e) {
        e.preventDefault();

        if (validaCampo(nome, setErrorNome) && validaEmail(email, setErrorEmail) && validaCampo(celular, setErrorCel)
            && validaCampo(cpf, setErrorCpf) && validaSenha(senha, setErrorSenha)) {

            const dados_usuario = {
                cel_usuario: celular,
                cpf_usuario: cpf,
                email_usuario: email,
                id_usuario: id,
                nome_usuario: nome,
                senha_usuario: senha,
                status_usuario: 'Ativo'
            };

            atualizarUsuarioMutation.mutate(dados_usuario)
            if(receptor) handleAtualizarReceptor()
        }
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

            {receptor &&
                <>
                    <Campo
                        type="text"
                        value={cep}
                        label="CEP"
                        placeholder="Digite seu CEP"
                        temMask
                        errorMsg={errorCep}
                    >
                        <PatternFormat
                            format="##.###-###"
                            allowEmptyFormatting mask="_"
                            value={cep}
                            onValueChange={(cep) => setCep(cep.value)}
                        />
                    </Campo>

                    <Campo
                        type="text"
                        value={logradouro}
                        onChange={(e) => setLogradouro(e.target.value)}
                        label="Logradouro (rua)"
                        placeholder="Digite seu logradouro"
                        errorMsg={errorLogradouro}
                    />

                    <Campo
                        type="text"
                        value={numero}
                        onChange={(e) => setNumero(e.target.value)}
                        label="Número"
                        placeholder="Digite seu número"
                        errorMsg={errorNumero}
                    />

                    <Campo
                        type="text"
                        value={complemento}
                        onChange={(e) => setComplemento(e.target.value)}
                        label="Complemento"
                        placeholder="Digite seu complemento"
                    />

                    <Campo
                        type="number"
                        icon={<GiWeight />}
                        value={carga}
                        onChange={(e) => setCarga(e.target.value)}
                        min={1}
                        label={'Capacidade de carga do veículo (em kg):'}
                        errorMsg={errorCarga}
                    />
                </>}

            <button type="submit" className="btn btn_primary arrow">Salvar</button>

        </form>
    )
}