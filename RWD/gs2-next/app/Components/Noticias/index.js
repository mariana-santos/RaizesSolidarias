import styles from '../../styles/page.module.css'

// import noticias from '../../assets/data/noticias.json'

import CardNoticia from '../CardNoticia'

import { useQuery } from 'react-query'

export default function Noticias() {

    const { isLoading, error, data } = useQuery('repoNoticiasData', () =>
        fetch(`http://localhost:8080/noticia/`)
        .then((res) => res.json())
    );

    if (isLoading) return 'Carregando...'

    if (error) return 'Ocorreu um erro: ' + error.message

    return (
        <section className={styles.cardsWrapper}>
            {data.map((noticia) => {
                return (
                    <CardNoticia
                        imagem={noticia.imagem}
                        titulo={noticia.titulo}
                        key={noticia.id}
                        id={noticia.id}
                    />
                )
            })}
        </section>
    )
}