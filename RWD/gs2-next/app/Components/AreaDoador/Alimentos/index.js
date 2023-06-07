import './style.css'

import { useQuery } from 'react-query'

import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';
import { toast } from 'react-toastify';
import { useEffect } from 'react';
import moment from 'moment';

import useSound from 'use-sound';

export default function Alimentos({ setNovosPlantios, novosPlantios, saldo, setSaldo, setAnimation }) {

    const { isLoading: alimentosLoading, error: alimentosError, data: alimentosData } = useQuery('repoalimentosData', () =>
        fetch('http://localhost:8080/alimento').then((res) => res.json())
    );


    const [somSaldo] = useSound(
        '/coins.wav',
        { volume: 0.25 }
    )

    const handleDragStart = (e) => e.preventDefault();

    if (alimentosLoading) return 'Carregando...'

    if (alimentosError) return 'Ocorreu um erro! ' + error.message

    const responsive = {
        0: { items: 2 },
        568: { items: 3 },
        1024: { items: 6 },
    };

    function handleAdicionarAlimento(e, alimento) {
        if (e) e.preventDefault();

        const plantio = {
            id_plantio: 1,
            espaco_plantio: novosPlantios.length + 1,
            data_plantio: moment(new Date()).format('YYYY-MM-DD'),
            alimento: alimento
        };

        if (novosPlantios.length < 12 && saldo >= alimento.preco_alimento) {
            setNovosPlantios(plantios => [...plantios, plantio]);
            setSaldo(saldo - alimento.preco_alimento)
            setAnimation('shake')
            setTimeout(() => setAnimation(''), 500)
            somSaldo()
        } else {
            if (novosPlantios.length >= 12)
                toast.error('Opa! Limite excedido. Finalize a plantação para plantar mais.');

            if (saldo < alimento.preco_alimento)
                toast.error('Opa! Você não tem moedas o suficiente para adicionar esse alimento à horta. Por favor, faça uma nova doação para continuar');
        }
    }

    const adicionarAlimentosRecursivamente = (novosPlantios) => {
        if (novosPlantios.length < 12) {
            const indexAlimentoAleatorio = Math.floor(Math.random() * alimentosData.length);
            const alimento = alimentosData[indexAlimentoAleatorio];

            // TODO: ver pq nao ta atualizando o saldo com essa lógica
            if (saldo >= alimento.preco_alimento) {
                handleAdicionarAlimento(null, alimento);
                setTimeout(() => adicionarAlimentosRecursivamente([...novosPlantios, alimento]), 100);
            }

            else toast.error('Opa! Você não tem moedas o suficiente para adicionar esse alimento à horta. Por favor, faça uma nova doação para continuar')
        }

        else toast.success(`Plantios adicionados à horta automaticamente com sucesso! 
        Não se esqueça de finalizar a plantação no fim da página!`)
    }

    const adicionarAlimentosAutomaticamente = async (e) => {
        e.preventDefault();

        for (let i = 0; i < 12; i++) {
            if (novosPlantios.length >= 12) {
                toast.error('Opa! Limite excedido. Finalize a plantação para plantar mais.');
                break;
            }

            const indexAlimentoAleatorio = Math.floor(Math.random() * alimentosData.length);
            const alimento = alimentosData[indexAlimentoAleatorio];

            if (saldo < alimento.preco_alimento) {
                toast.error(
                    'Opa! Você não tem moedas o suficiente para adicionar esse alimento à horta. Por favor, faça uma nova doação para continuar'
                );
                break;
            }

            await new Promise((resolve) => setTimeout(resolve, 100)); // Aguardar um intervalo de 100ms

            handleAdicionarAlimento(null, alimento);
        }

        toast.success(`Plantios adicionados à horta automaticamente com sucesso! 
            Não se esqueça de finalizar a plantação no fim da página!`);
    };

    return (
        <section id='alimentos'>
            <small>Se clicar no botão abaixo, o sistema vai usar seu saldo para plantar os alimentos automaticamente.
            </small>
            <small><strong> Lembre-se de finalizar a plantação no botão abaixo da horta!</strong></small>
            <button
                className='btn'
                onClick={(e) => adicionarAlimentosAutomaticamente(e)}>
                Adicionar automaticamente
            </button>

            <h3>Alimentos disponíveis para adicionar à horta</h3>
            <AliceCarousel mouseTracking responsive={responsive} disableButtonsControls>
                {alimentosData.map((alimento) => {
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