import './style.css'

import { useQuery } from 'react-query'

import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';

export default function Alimentos() {

    const { isLoading, error, data } = useQuery('repoData', () =>
        fetch('http://localhost:8080/alimento').then(res =>
            res.json()
        )
    )

    const handleDragStart = (e) => e.preventDefault();

    if (isLoading) return 'Carregando...'

    if (error) return 'Ocorreu um erro! ' + error.message

    const responsive = {
        0: { items: 1 },
        568: { items: 2 },
        1024: { items: 5 },
    };

    return (
        <section id='alimentos'>
            <AliceCarousel mouseTracking responsive={responsive} disableButtonsControls>
                {data.map((alimento) => {
                    return (
                        <div className='alimento' key={alimento.alimento_id} role="presentation" onDragStart={handleDragStart}>
                            <div className='wrap-icon'>
                                <img src={`/${alimento.nome_alimento}.png`} alt={`Imagem ilustrativa de um ${alimento.nome_alimento}}`} />
                            </div>
                            <h3>{alimento.nome_alimento}</h3>
                            <p className='preco'>
                                <img src="/coin.png" alt='' />
                                {alimento.preco_alimento}
                            </p>
                        </div>
                    )
                })}
            </AliceCarousel>
        </section>
    )
}