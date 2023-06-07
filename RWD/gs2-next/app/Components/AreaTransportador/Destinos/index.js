import { useQuery, useMutation } from 'react-query'

import { useEffect } from 'react';
import { useState } from 'react';
import { toast } from 'react-toastify';
import Destino from './Destino';

export default function Destinos({ setTela, id_usuario }) {

    const [destinosTransportados, setDestinosTransportados] = useState([])
    const [destinosDisponiveis, setDestinosDisponiveis] = useState([])

    const { isLoading: destLoading, error: destErro, data: dados } = useQuery('repoDestinosData', () =>
        fetch('http://localhost:8080/destino').then((res) => res.json())
    );

    useEffect(() => {
        if (!destLoading && !destErro) {
            console.log(dados);
            setDestinosDisponiveis(dados)
            fetch(`http://localhost:8080/receptor_destino/receptor/${id_usuario}`)
                .then((res) => res.json())
                .then((data) => setDestinosTransportados(data));
            console.log(destinosTransportados)
        }
    }, [dados, destErro, destLoading]);

    useEffect(() => {
        if (destinosTransportados.length > 0) {
            const destinosDisponiveis = dados.filter(
                (destino) =>
                    !destinosTransportados.some(
                        (receptor_destino) =>
                            receptor_destino.destino.id_destino === destino.id_destino
                    )
            );

            console.log(dados, destinosTransportados);

            setDestinosDisponiveis(destinosDisponiveis);
        }
    }, [destinosTransportados]);



    if (destLoading) return 'Carregando...'

    if (destErro) return 'Ocorreu um erro: ' + error.message

    return (
        <div>
            <button className="btn btn-secondary" onClick={() => setTela('inicio')}>
                {/* <BsArrowBarLeft /> */}
                Voltar
            </button>

            {destinosTransportados.length > 0 && <>
                <h3>Destinos transportados atualmente: </h3>
                <small>Esses são os destinos que você já transportou anteriormente. Clique em um deles para mais informações</small>
                <div className="row destinos">
                    {destinosTransportados.map((receptor_destino) => {
                        return <Destino
                            destino={receptor_destino.destino}
                            key={receptor_destino.destino.id_destino}
                            setDestinosDisponiveis={setDestinosDisponiveis}
                            setDestinosTransportados={setDestinosTransportados}
                            destinosDisponiveis={destinosDisponiveis}
                            destinosTransportados={destinosTransportados}
                            ehTransportado />
                    })}
                </div></>
            }

            {destinosDisponiveis.length > 0 && <>
                <h3>Destinos disponíveis: </h3>
                <small>Esses são os disponíveis para receber os alimentos da nossa horta. Clique em um deles para mais informações e adicionar aos seus destinos.</small>
                <div className="row destinos">
                    {destinosDisponiveis.map((destino) => {
                        return <Destino
                            destino={destino}
                            key={destino.id_destino}
                            setDestinosDisponiveis={setDestinosDisponiveis}
                            setDestinosTransportados={setDestinosTransportados}
                            destinosDisponiveis={destinosDisponiveis}
                            destinosTransportados={destinosTransportados}
                        />
                    })}
                </div></>
            }
        </div>
    )
}