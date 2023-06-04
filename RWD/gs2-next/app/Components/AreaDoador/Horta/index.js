import './style.css'

import { useQuery } from 'react-query'

export default function Horta() {

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
            id_plantio: 4,
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
            id_plantio: 4,
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

    function renderPlantios() {
        const plantiosDivs = [];

        const totalDivs = Math.ceil(data.length / 4);

        for (let i = 0; i < totalDivs; i++) {
            const plantios = data.slice(i * 4, i * 4 + 4);

            const plantiosElements = plantios.map(plantio => (
                <div key={plantio.id_plantio} className={`plantio ${plantio.alimento.nome_alimento} `}>
                    <div className={`${plantio.alimento.nome_alimento} wrap-icon`}>
                        <img src={`/${plantio.alimento.nome_alimento}.png`} className='alimento-menor'/>
                        {/* <img
                            className='planta'
                            src='/planta.png' 
                            alt={`Imagem ilustrativa de um plantio de ${plantio.alimento.nome_alimento}`} 
                        /> */}
                        <img src={`/${plantio.alimento.nome_alimento}.png`} className='alimento-menor'/>
                        <img src={`/${plantio.alimento.nome_alimento}.png`} className='alimento-menor'/>
                        <InformacoesPlantio plantio={plantio} />
                    </div>
                    <strong>{plantio.alimento.nome_alimento}</strong>
                </div>
            ));

            const div = (
                <div className="row plantios" key={`div_${i}`}>
                    {plantiosElements}
                </div>
            );

            plantiosDivs.push(div)
        }

        const divsRestantes = 4 - plantiosDivs.length;
        for (let i = 0; i < divsRestantes; i++) {
            const emptyDiv = (
                <div className="row plantios" key={`empty_div_${i}`} />
            );
            plantiosDivs.push(emptyDiv);
        }

        return plantiosDivs
    }

    return (
        <section id='horta'>
            {renderPlantios()}
            <button className='btn'>Salvar configuração da horta</button>
        </section>
    )
}

function InformacoesPlantio({plantio}){
    return(
        <div className='informacoes-plantio'>
            <p><strong>Data do plantio: </strong> {plantio.data_plantio} </p>
            <p><strong>Irrigações necessárias: </strong> {plantio.alimento.qtd_irrigacao} </p>
            <p>Será colhida em <strong>{2}</strong> dias </p>
            <button className='btn'>
                Regar
                <span className='preco'>
                    <img src="/coin.png" alt='' />
                    2
                </span>
            </button>
        </div>
    )
}