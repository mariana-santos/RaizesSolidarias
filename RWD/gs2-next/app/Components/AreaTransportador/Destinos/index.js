import { useQuery, useMutation } from 'react-query'

import { useEffect } from 'react';
import { useState } from 'react';
import { toast } from 'react-toastify';
import Destino from './Destino';

export default function Destinos({ setTela, id_usuario }) {

    const [destinosTransportados, setDestinosTransportados] = useState([])
    const [destinosDisponiveis, setDestinosDisponiveis] = useState([])

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


    // const { isLoading: destLoading, error: destErro, data: destinos } = useQuery('repoDestinosData', () =>
    //     fetch('http://localhost:8080/destino').then((res) => res.json())
    // );

    
    // const destinos = []

    // useEffect(() => {

    //     if(destinos && destinos.length > 0)
    //         fetch(`/receptor_destino/receptor/${id_usuario}`)
    //         .then((res) => res.json())
    //         .then((data) => setDestinosTransportados(data))
    //         .catch((error) => toast.error('Erro ao buscar destinos!'))

    //         const destinos_disponiveis = destinos.filter(destino =>
    //             !destinos_receptor.some(receptor_destino => receptor_destino.id_destino === destino.id_destino)
    //         );
            
    //         setDestinosDisponiveis(destinos_disponiveis)

    // }, [])

    // if (destLoading) return 'Carregando...'

    // if (destErro) return 'Ocorreu um erro: ' + error.message

    return (
        <div>
            <button className="btn btn-secondary" onClick={() => setTela('inicio')}>
                {/* <BsArrowBarLeft /> */}
                Voltar
            </button>

            <h3>Destinos transportados atualmente: </h3>
            <small>Esses são os destinos que você já transportou anteriormente. Clique em um deles para mais informações</small>
            <div className="row destinos">
                {destinos.map((destino) => {
                    return <Destino 
                                destino={destino} 
                                key={destino.id_destino}
                                ehTransportado />
                })}
            </div>

            <h3>Destinos disponíveis: </h3>
            <small>Esses são os disponíveis para receber os alimentos da nossa horta. Clique em um deles para mais informações e adicionar aos seus destinos.</small>
            <div className="row destinos">
                {destinos.map((destino) => {
                    return <Destino 
                                destino={destino} 
                                key={destino.id_destino}
                            />
                })}
            </div>
        </div>
    )
}