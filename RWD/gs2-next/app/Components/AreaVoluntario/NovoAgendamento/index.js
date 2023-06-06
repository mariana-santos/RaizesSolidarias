import Campo from "../../Campo"
import { BsCalendarDate } from "react-icons/bs"
import moment from "moment"

import { useState } from "react";

import { useMutation } from "react-query";

import { toast } from "react-toastify";

export default function NovoAgendamento({ data }) {

    const [turno, setTurno] = useState('Manhã');

    const cadastrarVoluntario = async (dados_voluntario) => {
        const response = await fetch('http://localhost:8080/voluntario', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_voluntario),
        });

        const data = await response.json();

        if (!response.ok || data.error) {
            toast.error(data.error)
            throw new Error('Erro ao cadastrar o doador');
        }
        else sessionStorage.setItem('voluntario', JSON.stringify(data));
    };

    const cadastrarAgendamento = async (dados_agendamento) => {
        const response = await fetch('http://localhost:8080/agendamento', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_agendamento),
        });

        const data = await response.json();

        if (!response.ok || data.error) {
            toast.error('Erro ao adicionar novo agendamento!')
            throw new Error('Erro ao cadastrar o agendamento');
        }
        else toast.success('Agendamento realizado com sucesso! Te vemos em breve pra cuidar da nossa horta solidária :)')
    };

    const cadastrarVoluntarioMutation = useMutation(cadastrarVoluntario);
    const cadastrarAgendamentoMutation = useMutation(cadastrarAgendamento);

    function handleNovoAgendamento(e) {
        e.preventDefault();

        const usuario = JSON.parse(sessionStorage.getItem("usuario"))
        const usuarioVoluntario = JSON.parse(sessionStorage.getItem("voluntario"))

        const dados_agendamento = {
            data_agendamento: moment(data).format('YYYY-MM-DD'),
            id_agendamento: 0,
            turno_agendamento: turno,
            usuario: usuario
        }

        if (!usuarioVoluntario) {
            const usuario_voluntario = {
                ...usuario,
                data_registro_voluntario: moment(new Date()).format('YYYY-MM-DD')
            };

            cadastrarVoluntarioMutation.mutate(usuario_voluntario) 
        } 

        cadastrarAgendamentoMutation.mutate(dados_agendamento)
    }

    return (
        <div className="novo-agendamento">
            <h3>Novo agendamento: </h3>

            <p> Para agendar um novo trabalho voluntário, selecione a data no calendário ao lado:</p>
            <Campo
                type="text"
                icon={<BsCalendarDate />}
                disabled
                value={moment(data).format("DD/MM/YYYY")}
            />

            <p>Selecione o turno: </p>

            <div className="horarios">
                <label className="horario" htmlFor="manha">
                    Manhã
                    <input
                        type="radio"
                        name="turno"
                        value="Manhã"
                        id="manha"
                        defaultChecked
                        onChange={(e) => setTurno(e.target.value)} />
                </label>

                <label className="horario" htmlFor="tarde">
                    Tarde
                    <input
                        type="radio"
                        name="turno"
                        value="Tarde"
                        id="tarde"
                        onChange={(e) => setTurno(e.target.value)} />
                </label>
            </div>


            <button type="submit" className="btn" onClick={(e) => handleNovoAgendamento(e)}>Salvar</button>
        </div>
    )
}