import { useEffect, useState } from "react"

import '../../styles/form.css'

import './style.css'

import { useQuery } from "react-query"

import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

import { toast } from "react-toastify"
import NovoAgendamento from "./NovoAgendamento";
import Agendamentos from "./Agendamentos";

export default function AreaVoluntario() {

    const hoje = new Date();
    const amanha = new Date(hoje.getTime() + 24 * 60 * 60 * 1000);
    const [data, setData] = useState(amanha);

    const [tela, setTela] = useState('novo-agendamento')

    const [id_usuario, setId_usuario] = useState()

    function handleData(data) {
        if(tela == 'novo-agendamento'){
            if (data <= new Date()) toast.error("A data não pode ser hoje ou dias anteriores!")
            else setData(data)
        }   
    }

    useEffect(() => {
        const usuario = JSON.parse(sessionStorage.getItem("usuario"))
        if (usuario) setId_usuario(usuario.id_usuario)
    }, [])


    return (
        <form id="voluntario">
            <div className="row-heading">
                <div className="heading">
                    <h2>Área do voluntário</h2>
                    <small>Bem vindo(a) à área do voluntário! Aqui você pode agendar suas visitas para contribuição da nossa horta solidária.</small>
                </div>

                <div className="wrap-btn">
                    <button 
                        className="btn" 
                        onClick={(e) => {
                                    e.preventDefault();
                                    setTela(tela == 'novo-agendamento' ? 'agendamentos' : 'novo-agendamento')}
                                }>
                            {tela == 'novo-agendamento' ? 'Ver meus agendamentos' : 'Novo agendamento'}
                    </button>
                </div>
            </div>

            <div className="row-body">
                <Calendar
                    value={data}
                    onChange={(data) => handleData(data)}
                    className="calendario"
                />

                { tela == 'novo-agendamento' ? 
                    <NovoAgendamento data={data} /> :
                    <Agendamentos id_usuario={id_usuario} />
                }

            </div>
        </form>
    )
}