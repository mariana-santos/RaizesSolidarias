import { useEffect, useState } from "react"

// import Campo from "../Campo"

import validator from "validator"

import '../../styles/form.css'

import './style.css'

import { Switch, FormControlLabel, Accordion, AccordionSummary, AccordionDetails, } from "@mui/material"

import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

import Campo from "../Campo"
import { GiWeight } from "react-icons/gi"

import { ToastContainer, toast } from "react-toastify"

import 'react-toastify/dist/ReactToastify.css';
import { PatternFormat } from "react-number-format"

import { MdOutlineKeyboardArrowDown } from 'react-icons/md'

export default function AreaTransportador() {

    const [carregando, setCarregando] = useState(false)

    const [carga, setCarga] = useState(1);

    const [cep, setCep] = useState('');
    const cidade = useState('São Paulo');
    const [logradouro, setLogradouro] = useState('')
    const [numero, setNumero] = useState('')
    const [complemento, setComplemento] = useState('')

    useEffect(() => {
        if (cep.length == 8) {
            const cep_formatado = cep.replace('-', '')
            fetch(`https://viacep.com.br/ws/${cep_formatado}/json/`)
                .then(resp => resp.json())
                .then(data => {
                    console.log(data)
                    setLogradouro(data.logradouro)
                    setComplemento(data.complemento)
                })
                .catch((error) => {
                    console.error(error)
                });
        }
    }, [cep])

    function handleSubmit(e) {

        e.preventDefault();

        // if (validaEmail() && validaSenha()) {
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
        // }

        // console.log(data)
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
        <form onSubmit={handleSubmit} id="transporte">
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
                    {false ? (
                        <div className="novo-agendamento">
                            <h3>Dados iniciais: </h3>

                            <p>Endereço:</p>
                            <small>É importante que seu endereço seja na cidade de <strong>São Paulo</strong>, que é onde nossa horta é realizada</small>

                            <Campo
                                type="text"
                                value={cep}
                                label="CEP"
                                placeholder="Digite seu CEP"
                                temMask
                            >
                                <PatternFormat
                                    format="##.###-###"
                                    allowEmptyFormatting mask="_"
                                    onValueChange={(cep) => setCep(cep.value)}
                                />
                            </Campo>

                            <Campo
                                type="text"
                                value={logradouro}
                                onChange={(e) => setLogradouro(e.target.value)}
                                label="Logradouro (rua)"
                                placeholder="Digite seu logradouro"
                            />

                            <Campo
                                type="text"
                                value={numero}
                                onChange={(e) => setNumero(e.target.value)}
                                label="Número"
                                placeholder="Digite seu número"
                            />

                            <Campo
                                type="text"
                                value={complemento}
                                onChange={(e) => setComplemento(e.target.value)}
                                label="Complemento"
                                placeholder="Digite seu complemento"
                            />

                            <p>Capacidade de carga do veículo:</p>
                            <Campo
                                type="number"
                                icon={<GiWeight />}
                                value={carga}
                                onChange={(e) => setCarga(e.target.value)}
                                min={1}
                            />

                            <button type="submit" className="btn">Salvar</button>
                        </div>
                    ) : (
                        <div>
                            <h3>Destinos transportados atualmente: </h3>
                            <small>Esses são os destinos que você já transportou anteriormente. Clique em um deles para mais informações</small>

                            <div className="row destinos">
                                {destinos.map((destino) => {
                                    return(
                                        <Accordion className="destino">
                                            <AccordionSummary expandIcon={<MdOutlineKeyboardArrowDown />} className="resumo">
                                                <p>
                                                    <strong>Destino #{ ("00" + destino.id_destino).slice(-4) }: </strong>
                                                    <small>{destino.endereco_destino}</small>
                                                </p>
                                            </AccordionSummary>

                                            <AccordionDetails className="detalhes">
                                                <p><strong>Endereço: </strong>{ destino.endereco_destino }</p>
                                                <p><strong>Responsável: </strong>{ destino.responsavel_destino }</p>
                                                <p><strong>Contato: </strong>{ destino.cel_destino }</p>
                                                <p><strong>Quantidade de dependentes: </strong>{ destino.qtd_dependentes_destino }</p>

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
                                    return(
                                        <Accordion className="destino">
                                            <AccordionSummary expandIcon={<MdOutlineKeyboardArrowDown />} className="resumo">
                                                <p>
                                                    <strong>Destino #{ ("00" + destino.id_destino).slice(-4) }: </strong>
                                                    <small>{destino.endereco_destino}</small>
                                                </p>
                                            </AccordionSummary>

                                            <AccordionDetails className="detalhes">
                                                {/* TODO: Adicionar link do maps: https://www.google.com/maps/search/Rua+Hip%C3%B3dromo,+720+CEP:+030.51-000 */}
                                                <p><strong>Endereço: </strong>{ destino.endereco_destino }</p>
                                                <p><strong>Responsável: </strong>{ destino.responsavel_destino }</p>
                                                {/* TODO: Adicionar link de contato: https://wa.me/5511952526565?text=Oi%2C+tudo+bem%3F+Quando+posso+levar+os+alimentos+da+Ra%C3%ADzes+Solid%C3%A1rias+no+endere%C3%A7o+cadastrado%3F */}
                                                <p><strong>Contato: </strong> <a href="">{ destino.cel_destino }</a></p>
                                                <p><strong>Quantidade de dependentes: </strong>{ destino.qtd_dependentes_destino }</p>

                                                <button className="btn">Adicionar aos meus destinos</button>
                                            </AccordionDetails>
                                        </Accordion>
                                    )
                                })}
                            </div>
                        </div>
                    )}


                </div>
            </div>
        </form>
    )
}