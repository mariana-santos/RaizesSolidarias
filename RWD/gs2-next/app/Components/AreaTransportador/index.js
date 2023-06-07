import { useEffect, useState } from "react"

import '../../styles/form.css'

import './style.css'

import DadosIniciaisReceptor from "./DadosIniciaisReceptor"
import Destinos from "./Destinos"

import Agendamentos from "../AreaVoluntario/Agendamentos"
import NovoAgendamento from "../AreaVoluntario/NovoAgendamento"

import Calendar from "react-calendar"
import 'react-calendar/dist/Calendar.css';

import { toast } from "react-toastify"

export default function AreaTransportador() {

    const [receptor, setReceptor] = useState(null)
    const [tela, setTela] = useState('inicio')
    const [subtela, setSubtela] = useState('novo-agendamento')

    const hoje = new Date();
    const amanha = new Date(hoje.getTime() + 24 * 60 * 60 * 1000);
    const [data, setData] = useState(amanha);

    useEffect(() => {
        setReceptor(JSON.parse(sessionStorage.getItem("receptor")))
    }, [])

    function handleData(data) {
        if (subtela == 'novo-agendamento') {
            if (data <= new Date()) toast.error("A data não pode ser hoje ou dias anteriores!")
            else setData(data)
        }
    }

    return (
        <form id="transporte">
            <div className="row-heading"><div className="heading">
                <h2>Área do transportador</h2>
                <small>Bem vindo(a) à área do transportador! Aqui você pode cadastrar os dados do seu veículo e das colheitas disponíveis para entrega.</small>
            </div>

                {tela === 'agendamentos' &&
                    <div className="wrap-btn">
                        <button
                            className="btn"
                            onClick={(e) => {
                                e.preventDefault();
                                setSubtela(subtela == 'novo-agendamento' ? 'agendamentos' : 'novo-agendamento')
                            }}>
                            {subtela == 'novo-agendamento' ? 'Ver meus agendamentos' : 'Novo agendamento'}
                        </button>
                    </div>
                }

            </div>


            <div className="row-body">

                <div className="transporte">

                    {/* Se a tabela transporte ainda não existir pra esse usuário, vai ser mostrado esse bloco pra cadastrar os dados iniciais da tabela */}
                    {(!receptor) ?
                        <DadosIniciaisReceptor setTela={setTela} setReceptor={setReceptor}/>
                        :
                        <div>
                            {tela === 'inicio' ?
                                (<div className="row inicio">
                                    <div className="column">
                                        <img src="/illustr-agendamentos.svg" />
                                        <p>Aqui você poderá gerenciar seus agendamentos para o <strong>transporte das colheitas aos destinos necessitados</strong>.</p>
                                        <button className="btn" onClick={() => setTela('agendamentos')}>Gerenciar agendamentos</button>
                                    </div>
                                    <div className="column">
                                        <img src="/illustr-destinos.svg" />
                                        <p>Nessa tela você poderá e gerenciar os <strong>destinos que você transporta atualmente!</strong> É importante se atentar aos dados dos destinos. </p>
                                        <button className="btn" onClick={() => setTela('destinos')}>Gerenciar destinos de transporte</button>
                                    </div>
                                </div>)
                                : tela === 'destinos' ?
                                    (<Destinos
                                        setTela={setTela}
                                        id_usuario={receptor.id_usuario} />)
                                    :
                                    (<div>
                                        <button className="btn btn-secondary" onClick={() => setTela('inicio')}>
                                            {/* <BsArrowBarLeft /> */}
                                            Voltar
                                        </button>
                                        <div className="row-body">
                                            <Calendar
                                                value={data}
                                                onChange={(data) => handleData(data)}
                                                className="calendario"
                                            />

                                            {subtela == 'novo-agendamento' ?
                                                <NovoAgendamento data={data} /> :
                                                <Agendamentos id_usuario={receptor.id_usuario} />
                                            }

                                        </div>
                                    </div>)}
                        </div>
                    }

                </div>
            </div>
        </form>
    )
}