import { useState } from 'react';
import './style.css'

// import { useQuery } from 'react-query'
import { useEffect } from 'react';
import { toast } from 'react-toastify';

import useSound from 'use-sound';

import { useMutation } from 'react-query';

export default function Horta({ novosPlantios, saldo, setSaldo, setAnimation }) {

    // const { isLoading, error, data } = useQuery('repoData', () =>
    //     fetch('http://localhost:8080/alimento').then(res =>
    //         res.json()
    //     )
    // )

    // if (isLoading) return 'Carregando...'

    // if (error) return 'Ocorreu um erro! ' + error.message

    const data = [
        {
            id_plantio: 1,
            data_plantio: 'data',
            espaco_plantio: '',
            alimento:
            {
                id_alimento: 1,
                nome_alimento: "agrião",
                preco_alimento: 5,
                tempo_colheita: 2,
                data_plantio: '22/10/2023',
                qtd_irrigacao: 2
            }
        },
        {
            id_plantio: 2,
            data_plantio: 'data',
            espaco_plantio: '',
            alimento:
            {
                id_alimento: 1,
                nome_alimento: "rucula",
                preco_alimento: 5,
                tempo_colheita: 2,
                data_plantio: '22/10/2023',
                qtd_irrigacao: 2
            }
        },
        {
            id_plantio: 3,
            data_plantio: 'data',
            espaco_plantio: '',
            alimento:
            {
                id_alimento: 1,
                nome_alimento: "batata",
                preco_alimento: 5,
                tempo_colheita: 2,
                data_plantio: '22/10/2023',
                qtd_irrigacao: 2
            }
        },
        {
            id_plantio: 4,
            data_plantio: 'data',
            espaco_plantio: '',
            alimento:
            {
                id_alimento: 1,
                nome_alimento: "cenoura",
                preco_alimento: 5,
                tempo_colheita: 2,
                data_plantio: '22/10/2023',
                qtd_irrigacao: 2
            }
        },
        {
            id_plantio: 5,
            data_plantio: 'data',
            espaco_plantio: '',
            alimento:
            {
                id_alimento: 1,
                nome_alimento: "alface",
                preco_alimento: 5,
                tempo_colheita: 2,
                data_plantio: '22/10/2023',
                qtd_irrigacao: 2
            }
        },
        {
            id_plantio: 6,
            data_plantio: 'data',
            espaco_plantio: '',
            alimento:
            {
                id_alimento: 1,
                nome_alimento: "mandioca",
                preco_alimento: 5,
                tempo_colheita: 2,
                data_plantio: '22/10/2023',
                qtd_irrigacao: 2
            }
        }
    ]

    function handleRegar(e) {
        if (e) e.preventDefault();
        console.log(saldo)
        if (saldo >= 2) {
            setSaldo(saldo - 2);
            setAnimation('shake')
            setTimeout(() => setAnimation(''), 500)
            somSaldo();
        }

        else
            toast.error(
                "Opa! Você não tem moedas o suficiente para regar esse alimento. Por favor, faça uma nova doação para continuar"
            );
    }

    const ultimosPlantios = data.slice(0, 4)
    const [todosPlantios, setTodosPlantios] = useState()

    useEffect(() => {
        setTodosPlantios(ultimosPlantios.concat(novosPlantios))
    }, [novosPlantios])


    const [somSaldo] = useSound(
        '/coins.wav',
        { volume: 0.25 }
    )

    const cadastrarPlantios = async (novosPlantios) => {
        const response = await fetch('http://localhost:8080/doador', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(novosPlantios),
        });

        const data = await response.json();
        console.log(data)

        if (!response.ok || data.error) {
            toast.error(response.error)
            throw new Error('Erro ao cadastrar novos plantios');
        }
        else toast.success('Plantação finalizada com sucesso! Nossos voluntários vão cuidar deles com muito carinho.')
    };

    const atualizarDoador = async (dados_doador) => {
        const response = await fetch(`http://localhost:8080/doador/${dados_doador.id_usuario}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_doador),
        });

        if (!response.ok) {
            toast.error('Erro ao atualizar dados');
            throw new Error('Erro ao atualizar o usuário');
        }
        else {
            sessionStorage.setItem('doador', JSON.stringify(dados_doador));
            // setSaldo(dados_doador.moedas_doador)
        }
    };
    
    const cadastrarPlantiosMutation = useMutation(cadastrarPlantios);
    const atualizarSaldoMutation = useMutation(atualizarDoador);

    function handleFinalizarPlantacao(e) {
        e.preventDefault();

        const usuarioDoador = typeof window !== 'undefined' ? JSON.parse(sessionStorage.getItem("doador")) : null;

        if (novosPlantios.length > 0 && usuarioDoador) {

            const usuario_doador = {
                ...usuarioDoador,
                nivel_doador: 1,
                moedas_doador: saldo
            };

            cadastrarPlantiosMutation(novosPlantios)
            atualizarSaldoMutation(usuario_doador)
        }
    }

    return (
        <section id='horta'>
            <small className='metade'>Os quatro primeiros alimentos são os últimos plantios realizados. Adicione novos alimentos para serem plantados na horta!</small>
            <div className='plantios'>
                {todosPlantios &&
                    todosPlantios.map((plantio => {
                        return (
                            <div
                                key={plantio.id_plantio}
                                className={`plantio ${plantio.alimento.nome_alimento} `}
                            >
                                <div className={`${plantio.alimento.nome_alimento} wrap-icon`}>
                                    <ImagensPlantio nome_alimento={plantio.alimento.nome_alimento} />
                                    <InformacoesPlantio plantio={plantio} />
                                </div>
                                <strong>{plantio.alimento.nome_alimento}</strong>
                            </div>)

                    }))}
            </div>
            <button
                className='btn'
                onClick={(e) => handleFinalizarPlantacao(e)}>Finalizar Plantação</button>
        </section>
    )

    function InformacoesPlantio({plantio}) {
        return (
            <div className="informacoes-plantio">
                <p className="nome-alimento">
                    Plantio de {plantio.alimento.nome_alimento}
                </p>
                <p>
                    <strong>Data do plantio: </strong> {plantio.data_plantio}{' '}
                </p>
                <p>
                    <strong>Irrigações necessárias: </strong>{' '}
                    {plantio.alimento.qtd_irrigacao}{' '}
                </p>
                <p>Será colhida em <strong>{2}</strong> dias </p>
                <button className="btn" onClick={(e) => handleRegar(e)}>
                    Regar
                    <span className="preco">
                        <img src="/coin.png" alt="" />
                        2
                    </span>
                </button>
            </div>
        )
    }
}

function ImagensPlantio({nome_alimento}) {
    return (
        <>
            <img
                src={`/${nome_alimento}.png`}
                className="alimento-menor"
            />
            <img
                src={`/${nome_alimento}.png`}
                className="alimento-menor"
            />
            <img
                src={`/${nome_alimento}.png`}
                className="alimento-menor"
            />
        </>
    )
}