import Image from 'next/image'
import styles from '../app/styles/page.module.css'
import Menu from '../app/Components/Menu'

import Link from 'next/link'
import CardInfo from '../app/Components/CardInfo'
import Noticias from '../app/Components/Noticias'
import Footer from '../app/Components/Footer'

import { Raleway } from 'next/font/google'

const font = Raleway({ subsets: ['latin'] })

import '../app/globals.css'

import { Quicksand } from 'next/font/google'

const fontBody = Quicksand({ subsets: ['latin'] })

export default function Home() {

  const usuario = typeof window !== 'undefined' ? JSON.parse(sessionStorage.getItem("usuario")) : null;

  return (
    <div className={fontBody.className} id='home'>
      <main className={styles.main}>
        <div className={styles.blur}></div>
        <Menu />

        <div className={styles.content}>
          <h2 className={font.className}>A fome é um problema global que afeta cerca de <strong>828.000.000</strong> de pessoas em todo o mundo.</h2>
          <p>Saiba como ajudar doando ou se voluntariando na nossa Horta Solidária. </p>

          <div className={styles.buttons}>
            <Link href="/doar" className='btn'>Seja um doador</Link>
            <Link href="/ser-um-voluntario" className='btn'>Seja um voluntário</Link>
          </div>
        </div>
      </main>

      <div className={styles.container}>
        <h2 className="title">O problema</h2>

        <p className={styles.metade}>Em 2020, os dados relacionados à fome <strong>subiram de forma extrema no mundo todo</strong>.
          Muitas regiões sofreram (e ainda sofrem) com a falta de acesso a alimentos básicos, como <strong>arroz, trigo e milho.</strong>
        </p>

        <section className={styles.cardsWrapper}>
          <CardInfo titulo="Entre 720 e 811 milhões" desc="de pessoas em todo o mundo estavam sofrendo de fome" />
          <CardInfo titulo="2,4 bilhões" desc="de pessoas estavam sem acesso regular a alimentos adequados." />
          <CardInfo titulo="47%" desc="foi a parcela de países sobrecarregados por preços elevados de alimentos" />
        </section>

        <section className={styles.containerImage} id='solucao'>
          <div className={styles.column}>
            <h2 className='title'>A solução</h2>
            <p>Pensando nisso, a <strong>Raízes Solidárias</strong> foi criada. Nosso projeto consiste em uma <strong>horta solidária </strong>mantida por doações e voluntários para a manutenção da horta e o transporte da colheita de alimentos para famílias necessitadas e ONGs responsáveis. </p>

            <p>Nossos doadores tem a opção de escolher no que seu dinheiro será usado: em sementes de diferentes <strong>alimentos</strong> importantes para a nutrição humana ou para a manutenção da horta, com a irrigação e outros itens voltados ao <strong>bom funcionamento do sistema</strong></p>

            <div className={styles.buttons}>
              <Link href={usuario ? '/perfil' : '/login'} className='btn'>Seja um doador</Link>
              <Link href={usuario ? '/perfil' : '/login'} className='btn'>Seja um voluntário</Link>
            </div>
          </div>

          <div className={styles.column}>
            <Image src="/img-main.jpg" width={500} height={400} />
          </div>
        </section>

        <h2 className="title">Como ajudar</h2>

        <p className={styles.metade}>Existem muitas formas diferentes de <strong>contribuir com o nosso projeto</strong> e isso fará uma diferença enorme na vida de famílias que se beneficiam da nossa horta! Veja como ajudar:
        </p>

        <section className={styles.cardsWrapper} id='como-ajudar'>
          <CardInfo titulo="Sendo um voluntário" desc="Ajude na manutenção e plantio da horta sempre que quiser!" tem_botao txt_botao="agendar trabalho voluntário" />
          <CardInfo titulo="Sendo um transportador" desc="É só cadastrar seus dados e agendar um horário para levar nossas colheitas para as famílias." tem_botao txt_botao="Agendar transporte" />
          <CardInfo titulo="Sendo um doador" desc="Para isso, você pode doar qualquer valor e selecionar quaisquer alimentos quiser para serem plantados na horta!" tem_botao txt_botao="DOAR" />
        </section>

        <section id="noticias">
          <h2 className='title'>Notícias</h2>
          <Noticias />

        </section>

      </div>

      <Footer />
    </div>
  )
}
