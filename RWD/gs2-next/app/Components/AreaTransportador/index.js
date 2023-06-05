import { useEffect, useState } from "react"

// import Campo from "../Campo"

import '../../styles/form.css'

import './style.css'

import { Accordion, AccordionSummary, AccordionDetails, } from "@mui/material"

import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

import Campo from "../Campo"
import { GiWeight } from "react-icons/gi"

import { ToastContainer, toast } from "react-toastify"

import 'react-toastify/dist/ReactToastify.css';
import { PatternFormat } from "react-number-format"

import { MdOutlineKeyboardArrowDown } from 'react-icons/md'
import { validaCampo, validaNumber } from "../../utils/validacao"

import { useQuery, useMutation } from 'react-query'

export default function AreaTransportador() {

    const [carga, setCarga] = useState(1);
    const [errorCarga, setErrorCarga] = useState(null);

    const [cep, setCep] = useState('');
    const [errorCep, setErrorCep] = useState(null);

    const cidade = useState('São Paulo');

    const [logradouro, setLogradouro] = useState('')
    const [errorLogradouro, setErrorLogradouro] = useState(null)

    const [numero, setNumero] = useState('')
    const [errorNumero, setErrorNumero] = useState(null)

    const [complemento, setComplemento] = useState('')

    const [endereco, setEndereco] = useState(null)

    const [receptor, setReceptor] = useState(null)

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

    useEffect(() => {
        // const usuario = typeof window !== 'undefined' ? JSON.parse(sessionStorage.getItem("usuario")) : null;
        setReceptor(JSON.parse(sessionStorage.getItem("receptor")))
    }, [])

    useEffect(() => {
        if (numero.length == 8){
            
        }
            
    }, [numero])

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
            // TODO: Mostrar menuzinho pra ele escolher agendamentos e destinos
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

                cadastrarReceptorMutation.mutate(usuario_receptor)
        }
    }

    const destinos = [
        {
            id_destino: 1,
            endereco_destino: 'Rua Hipódromo, 720 CEP: 030.51-000',
            responsavel_destino: 'Bruna Menegatti Vienna',
            cel_destino: '(11) 95252-6565',
            qtd_dependentes_destino: 5
        },
        {
            id_destino: 2,
            endereco_destino: 'Rua Armando Mamede Júnior, 149A CEP: 081.50-070 ',
            responsavel_destino: 'Bruna Menegatti Vienna',
            cel_destino: '(11) 95252-6565',
            qtd_dependentes_destino: 2
        }
    ]

    

    return (

        
        <form id="transporte">
            <ToastContainer
                position="bottom-right"
                autoClose={2000}
                closeOnClick
                pauseOnHover
            />

            <div className="heading">
                <h2>Área do transportador</h2>
                <small>Bem vindo(a) à área do transportador! Aqui você pode cadastrar os dados do seu veículo e das colheitas disponíveis para entrega.</small>
            </div>

            <div className="row-body">

                <div className="transporte">

                    {/* Se a tabela transporte ainda não existir pra esse usuário, vai ser mostrado esse bloco pra cadastrar os dados iniciais da tabela */}
                    {(receptor) ?
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
                        :
                        <div>
                        <h3>Destinos transportados atualmente: </h3>
                        <small>Esses são os destinos que você já transportou anteriormente. Clique em um deles para mais informações</small>

                        <div className="row destinos">
                            {destinos.map((destino) => {
                                return (
                                    <Accordion className="destino">
                                        <AccordionSummary expandIcon={<MdOutlineKeyboardArrowDown />} className="resumo">
                                            <p>
                                                <strong>Destino #{("00" + destino.id_destino).slice(-4)}: </strong>
                                                <small>{destino.endereco_destino}</small>
                                            </p>
                                        </AccordionSummary>

                                        <AccordionDetails className="detalhes">
                                            <p><strong>Endereço: </strong>{destino.endereco_destino}</p>
                                            <p><strong>Responsável: </strong>{destino.responsavel_destino}</p>
                                            <p><strong>Contato: </strong>{destino.cel_destino}</p>
                                            <p><strong>Quantidade de dependentes: </strong>{destino.qtd_dependentes_destino}</p>

                                            <button className="btn">Entrar em contato</button>
                                        </AccordionDetails>
                                    </Accordion>
                                )
                            })}
                        </div>

                        <h3>Destinos disponíveis: </h3>
                        <small>Esses são os disponíveis para receber os alimentos da nossa horta. Clique em um deles para mais informações e adicionar aos seus destinos.</small>

                        <div className="row destinos">
                            {destinos.map((destino) => {
                                return (
                                    <Accordion className="destino">
                                        <AccordionSummary expandIcon={<MdOutlineKeyboardArrowDown />} className="resumo">
                                            <p>
                                                <strong>Destino #{("00" + destino.id_destino).slice(-4)}: </strong>
                                                <small>{destino.endereco_destino}</small>
                                            </p>
                                        </AccordionSummary>

                                        <AccordionDetails className="detalhes">
                                            {/* TODO: Adicionar link do maps: https://www.google.com/maps/search/Rua+Hip%C3%B3dromo,+720+CEP:+030.51-000 */}
                                            <p><strong>Endereço: </strong>{destino.endereco_destino}</p>
                                            <p><strong>Responsável: </strong>{destino.responsavel_destino}</p>
                                            {/* TODO: Adicionar link de contato: https://wa.me/5511952526565?text=Oi%2C+tudo+bem%3F+Quando+posso+levar+os+alimentos+da+Ra%C3%ADzes+Solid%C3%A1rias+no+endere%C3%A7o+cadastrado%3F */}
                                            <p><strong>Contato: </strong> <a href="">{destino.cel_destino}</a></p>
                                            <p><strong>Quantidade de dependentes: </strong>{destino.qtd_dependentes_destino}</p>

                                            <button className="btn">Adicionar aos meus destinos</button>
                                        </AccordionDetails>
                                    </Accordion>
                                )
                            })}
                        </div>
                    </div>
                    }

                </div>
            </div>
        </form>
    )
}