import { useState } from "react"

// import Campo from "../Campo"

import validator from "validator"

import '../../styles/form.css'

import './style.css'

import { useQuery } from "react-query"

import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

import Moment from "react-moment"
import Campo from "../Campo"
import { BsCalendarDate } from "react-icons/bs"

import moment from "moment"
import { toast } from "react-toastify"

export default function AreaVoluntario() {

    const hoje = new Date();
    const amanha = new Date(hoje.getTime() + 24 * 60 * 60 * 1000);
    const [data, setData] = useState(amanha);

    const [turno, setTurno] = useState('Manhã');

    const { isLoading, error, agendamentos } = useQuery('repoData', () =>
        fetch('http://localhost:8080/agendamento').then(res => res.json())
    )

    if (isLoading) return 'Carregando...'

    if (error) return 'Ocorreu um erro: ' + error.message

    function handleSubmit(e) {

        e.preventDefault();

        console.log(data)
    }

    function handleData(data) {
        if (data <= new Date()) {
            handleDataAgendamento()
            // Futuramente esse erro só vai aparecer caso seja um novo agendamento: 
            // ou seja, se o dia selecionado não tiver nenhum agendamento cadastrado 
            // (que é quando o formulário de novo agendamento é mostrado)
            toast.error("A data não pode ser hoje ou dias anteriores!")
        }
        else setData(data)
    }

    function handleDataAgendamento(e){
        if (data <= new Date()) {
            
        }
    }

    function handleSelecaoChange (e) {
        setTurno(e.target.value);
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="row-heading">
                <div className="heading">
                    <h2>Área do voluntário</h2>
                    <small>Bem vindo(a) à área do voluntário! Aqui você pode agendar suas visitas para contribuição da nossa horta solidária.</small>
                </div>
            </div>

            <div className="row-body">

                <Calendar
                    value={data}
                    onChange={(data) => handleData(data)}
                    className="calendario"
                />

                <div className="agendamento">

                    {/* Se tiver um dia selecionado já tiver agendamento, vai ser esse bloco */}
                    <div className="agendamento-existente">
                        <h3>Agendamento no dia selecionado: </h3>
                        <div className="row">
                            <p><strong>Dia:</strong> <Moment format="DD/MM/YYYY">{data}</Moment></p>
                            <p><strong>Turno:</strong> Tarde</p>
                        </div>
                    </div>

                    {/* Esse bloco só aparece se for um dia futuro e ainda não existir nenhum agendamento no dia */}
                    <div className="novo-agendamento">
                        <h3>Novo agendamento: </h3>

                        <p>Selecione a data no calendário ao lado:</p>
                        <Campo 
                            type="text"
                            icon={<BsCalendarDate />}
                            disabled
                            value={moment(data).format("DD/MM/YYYY")}
                            onChange={(e) => handleDataAgendamento(e)}
                        />

                        <p>Selecione o turno: </p>

                        <div className="horarios">
                            <label className="horario" htmlFor="manha">
                                Manhã
                                <input type="radio" name="turno" value="Manhã" id="manha" defaultChecked onChange={handleSelecaoChange} />
                            </label>

                            <label className="horario" htmlFor="tarde">
                                Tarde
                                <input type="radio" name="turno" value="Tarde" id="tarde" onChange={handleSelecaoChange} />
                            </label>
                        </div>

                        
                        <button type="submit" className="btn">Salvar</button>
                    </div>
                    
                </div>
            </div>
        </form>
    )
}