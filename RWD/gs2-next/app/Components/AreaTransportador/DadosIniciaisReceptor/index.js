import { validaCampo, validaNumber } from "../../../utils/validacao"

import { useQuery, useMutation } from 'react-query'

import { PatternFormat } from "react-number-format"

import { toast } from "react-toastify"

import Campo from "../../Campo"
import { GiWeight } from "react-icons/gi"

import { useEffect, useState } from "react"

export default function DadosIniciaisReceptor({ setTela, setReceptor }) {

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

    const cadastrarReceptor = async (dados_receptor) => {
        console.log(dados_receptor)
        const response = await fetch('http://localhost:8080/receptor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_receptor),
        });

        if (!response.ok) toast.error('Erro ao cadastrar dados!')
        
        else {
            const data = await response.json();
            sessionStorage.setItem('receptor', JSON.stringify(data));
            toast.success('Dados cadastrados com sucesso!')
            setTela('inicio')
            setReceptor(data)
        }
    };

    const cadastrarReceptorMutation = useMutation(cadastrarReceptor);

    function handleCadastrarReceptor(e) {
        e.preventDefault()


        if(validaCampo(carga, setErrorCarga) && validaCampo(cep, setErrorCep) &&
           validaCampo(logradouro, setErrorLogradouro) && validaNumber(numero, setErrorNumero)){

                const cep_formatado = cep.replace('-', '')
                fetch(`http://localhost:8080/endereco/${cep_formatado}/${numero}`)
                .then(resp => resp.json())
                .then(data => {
                    console.log(data)
                    setEndereco(data.endereco)
                })
                .catch((error) => {
                    console.log(error)
                    toast.error('Endereço inválido! Por favor, digite novamente')
                    setCep('')
                    setLogradouro('')
                    setComplemento('')
                });

                const usuario = JSON.parse(sessionStorage.getItem("usuario"));
                const usuario_receptor = {
                    ...usuario,
                    carga_receptor: carga,
                    endereco_receptor: endereco
                }

                console.log(usuario_receptor)
                cadastrarReceptorMutation.mutate(usuario_receptor)
        }
    }

    return (
        <div className="novo-transportador">
            <h3>Dados iniciais: </h3>

            <p>Endereço:</p>
            <small>É importante que seu endereço seja na cidade de <strong>São Paulo</strong>, que é onde nossa horta é realizada e os destinos de entrega estão localizados</small>

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

            <p>Capacidade de carga do veículo (em kg):</p>
            <Campo
                type="number"
                icon={<GiWeight />}
                value={carga}
                onChange={(e) => setCarga(e.target.value)}
                min={1}
                errorMsg={errorCarga}
            />

            <button type="submit" className="btn" onClick={(e) => handleCadastrarReceptor(e)}>Salvar</button>
        </div>
    )
}