import { useQuery, useMutation } from "react-query"

import Moment from "react-moment";

import './style.css'

import { toast } from 'react-toastify'
import { useState } from "react";
import { useEffect } from "react";

export default function Agendamentos({ id_usuario }) {

    const [agendamentos, setAgendamentos] = useState([])

    const cancelarAgendamento = async (id_agendamento) => {
        const response = await fetch(`http://localhost:8080/agendamento/${id_agendamento}`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            const data = await response.json();
            toast.error('Erro ao cancelar agendamento!')
        }

        else {
            toast.success('Agendamento cancelado com sucesso. Esperamos que consiga agendar novos trabalhos voluntários em breve!')
            setAgendamentos((agendamentos) => agendamentos.filter(item => item.id_agendamento !== id_agendamento));
            console.log(agendamentos)
        }
    };

    const cancelarAgendamentoMutation = useMutation(cancelarAgendamento);

    function handleCancelarAgendamento(e, id_agendamento){
        e.preventDefault()
        cancelarAgendamentoMutation.mutate(id_agendamento)
    }

    const { isLoading: agendLoading, error: agendErro, data: dados } = useQuery('repoAgendamentosData', () =>
        fetch(`http://localhost:8080/agendamento/usuario/${id_usuario}`)
        .then((res) => res.json())
    );

    useEffect(() => {
        if(dados) setAgendamentos(dados)
    }, [dados, agendErro, agendLoading])

    if (agendLoading) return 'Carregando...'

    if (agendErro) return 'Ocorreu um erro: ' + error.message

    return (
        <section className="agendamentos">

            <h3>Meus agendamentos</h3>
            {agendamentos && agendamentos.map((agendamento) =>
                    <div className="agendamento" key={agendamento.id_agendamento}>
                        <div className="row">
                            <p>
                                <strong>Dia: </strong>
                                <Moment format="DD/MM/YYYY" add={{ days: 1 }}>{agendamento.data_agendamento}</Moment>
                            </p>
                            <p><strong>Turno:</strong> {agendamento.turno_agendamento}</p>
                        </div>
                        <button 
                            className="btn btn-tertiary" 
                            onClick={(e) => handleCancelarAgendamento(e, agendamento.id_agendamento)}>
                                Cancelar
                        </button>
                    </div>
                )}
                
            {!agendamentos || agendamentos.length == 0 && <p>Nenhum agendamento encontrado!</p>}
        </section>
    )
}