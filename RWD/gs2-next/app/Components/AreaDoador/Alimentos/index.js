import './style.css'

import { useQuery } from 'react-query'

import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';
import { toast } from 'react-toastify';
import { useEffect } from 'react';
import moment from 'moment';

import useSound from 'use-sound';

export default function Alimentos({ setNovosPlantios, novosPlantios, saldo, setSaldo, setAnimation }) {

    // const { isLoading, error, data } = useQuery('repoData', () =>
    //     fetch('http://localhost:8080/alimento').then(res =>
    //         res.json()
    //     )
    // )

    const handleDragStart = (e) => e.preventDefault();

    // if (isLoading) return 'Carregando...'

    // if (error) return 'Ocorreu um erro! ' + error.message

    const [somSaldo] = useSound(
        '/coins.wav',
        { volume: 0.25 }
    )

    const responsive = {
        0: { items: 1 },
        568: { items: 2 },
        1024: { items: 6 },
    };

    const data = [
        {
            id_alimento: 1,
            nome_alimento: "tomate",
            preco_alimento: 5,
            tempo_colheita: 2,
            qtd_irrigacao: 2
        },
        {
            id_alimento: 2,
            nome_alimento: "alface",
            preco_alimento: 5,
            tempo_colheita: 2,
            qtd_irrigacao: 2
        },
        {
            id_alimento: 3,
            nome_alimento: "rabanete",
            preco_alimento: 5,
            tempo_colheita: 2,
            qtd_irrigacao: 2
        },
        {
            id_alimento: 4,
            nome_alimento: "mandioca",
            preco_alimento: 5,
            tempo_colheita: 2,
            qtd_irrigacao: 2
        },
        {
            id_alimento: 5,
            nome_alimento: "batata",
            preco_alimento: 5,
            tempo_colheita: 2,
            qtd_irrigacao: 2
        },
        {
            id_alimento: 6,
            nome_alimento: "agrião",
            preco_alimento: 5,
            tempo_colheita: 2,
            qtd_irrigacao: 2
        },
        {
            id_alimento: 7,
            nome_alimento: "cenoura",
            preco_alimento: 5,
            tempo_colheita: 2,
            qtd_irrigacao: 2
        },
        {
            id_alimento: 4,
            nome_alimento: "rucula",
            preco_alimento: 5,
            tempo_colheita: 2,
            qtd_irrigacao: 2
        },
        {
            id_alimento: 5,
            nome_alimento: "pepino",
            preco_alimento: 5,
            tempo_colheita: 2,
            qtd_irrigacao: 2
        },
    ]

    function handleAdicionarAlimento(e, alimento) {
        if (e) e.preventDefault();

        const plantio = {
            id_plantio: 1,
            data_plantio: 'data',
            espaco_plantio: 5454,
            //TODO: ALTERAR PRO FORMATO QUE O JAVA PEDE E PRO DIA DE HOJE
            data_plantio: moment(new Date()).format('MM/DD/YYYY'),
            alimento: alimento
        };

        if (novosPlantios.length < 12 && saldo >= alimento.preco_alimento){
            setNovosPlantios(plantios => [...plantios, plantio]);
            setSaldo(saldo - alimento.preco_alimento)
            setAnimation('shake')
            setTimeout(() => setAnimation(''), 500)
            somSaldo()
        } else{
            if(novosPlantios.length >= 12) 
                toast.error('Opa! Limite excedido. Finalize a plantação para plantar mais.');

            if(saldo < alimento.preco_alimento) 
                toast.error('Opa! Você não tem moedas o suficiente para adicionar esse alimento à horta. Por favor, faça uma nova doação para continuar');
        } 
    }

    const adicionarAlimentosRecursivamente = (novosPlantios) => {
        if (novosPlantios.length < 12) {
            const indexAlimentoAleatorio = Math.floor(Math.random() * data.length);
            const alimento = data[indexAlimentoAleatorio];

            // TODO: ver pq nao ta atualizando o saldo com essa lógica
            if(saldo >= alimento.preco_alimento){
                handleAdicionarAlimento(null, alimento);
                setTimeout(() => adicionarAlimentosRecursivamente([...novosPlantios, alimento]), 100); // Passa o novo estado atualizado como argumento
            }

            else toast.error('Opa! Você não tem moedas o suficiente para adicionar esse alimento à horta. Por favor, faça uma nova doação para continuar')
        }

        else toast.success(`Plantios adicionados à horta automaticamente com sucesso! 
        Não se esqueça de finalizar a plantação no fim da página!`)
    };

    function adicionarAlimentosAutomaticamente(e) {
        e.preventDefault();
        adicionarAlimentosRecursivamente(novosPlantios);
    }


    return (
        <section id='alimentos'>
            <small>Se clicar no botão abaixo, o sistema vai usar seu saldo para plantar os alimentos automaticamente.
            </small>
            <small><strong> Lembre-se de finalizar a plantação no botão abaixo da horta!</strong></small>
            <button
                className='btn'
                onClick={(e) => adicionarAlimentosAutomaticamente(e)}>
                Adicionar alimentos automaticamente
            </button>

            <h3>Alimentos disponíveis para adicionar à horta</h3>
            <AliceCarousel mouseTracking responsive={responsive} disableButtonsControls>
                {data.map((alimento) => {
                    return (
                        <div className='alimento' key={alimento.alimento_id} role="presentation" onDragStart={handleDragStart}>
                            <div className='wrap-icon'>
                                <img src={`/${alimento.nome_alimento}.png`} alt={`Imagem ilustrativa de um ${alimento.nome_alimento}}`} />
                            </div>
                            <h3>{alimento.nome_alimento}
                                <p className='preco'>
                                    <img src="/coin.png" alt='' />
                                    {alimento.preco_alimento}
                                </p>
                            </h3>
                            <button
                                className='btn btn-secondary'
                                onClick={(e) => handleAdicionarAlimento(e, alimento)}
                            >
                                adicionar
                            </button>
                        </div>
                    )
                })}
            </AliceCarousel>
        </section>
    )
}