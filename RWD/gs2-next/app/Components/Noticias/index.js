import styles from '../../styles/page.module.css'

import noticias from '../../assets/data/noticias.json'

import CardNoticia from '../CardNoticia'

export default function Noticias() {
    return (
        <section className={styles.cardsWrapper}>
            {noticias.map((noticia) => {
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