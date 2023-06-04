import './style.css'

import { useQuery } from 'react-query'

import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';

export default function Alimentos() {

    // const { isLoading, error, data } = useQuery('repoData', () =>
    //     fetch('http://localhost:8080/alimento').then(res =>
    //         res.json()
    //     )
    // )

    const handleDragStart = (e) => e.preventDefault();

    // if (isLoading) return 'Carregando...'

    // if (error) return 'Ocorreu um erro! ' + error.message

    const responsive = {
        0: { items: 1 },
        568: { items: 2 },
        1024: { items: 6 },
    };

    const data = [
        {
            id_alimento: 1,
            nome_alimento: "tomate",
            preco_alimento: 5
        },
        {
            id_alimento: 2,
            nome_alimento: "alface",
            preco_alimento: 5
        },
        {
            id_alimento: 3,
            nome_alimento: "rabanete",
            preco_alimento: 5
        },
        {
            id_alimento: 4,
            nome_alimento: "mandioca",
            preco_alimento: 5
        },
        {
            id_alimento: 5,
            nome_alimento: "batata",
            preco_alimento: 5
        },
        {
            id_alimento: 6,
            nome_alimento: "agrião",
            preco_alimento: 5
        },
        {
            id_alimento: 7,
            nome_alimento: "cenoura",
            preco_alimento: 5
        },
        {
            id_alimento: 4,
            nome_alimento: "rucula",
            preco_alimento: 5
        },
        {
            id_alimento: 5,
            nome_alimento: "pepino",
            preco_alimento: 5
        },
    ]

    return (
        <section id='alimentos'>
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
                            <button className='btn btn-secondary'>adicionar</button>
                        </div>
                    )
                })}
            </AliceCarousel>
            <button className='btn'>Adicionar alimentos automaticamente</button>
            <small>Se clicar no botão acima, o sistema vai usar seu saldo para plantar os alimentos automaticamente</small>
        </section>
    )
}