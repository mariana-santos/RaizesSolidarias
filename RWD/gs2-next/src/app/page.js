import Image from 'next/image'
import styles from './page.module.css'
import Menu from './Components/Menu'

import Link from 'next/link'
import CardInfo from './Components/CardInfo'

export default function Home() {
  return (
    <>
      <main className={styles.main}>
        <div className={styles.blur}></div>
        <Menu />

        <div className={styles.content}>
          <h2>A fome é um problema global que afeta cerca de <strong>828.000.000</strong> de pessoas em todo o mundo.</h2>
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
          <CardInfo numero="Entre 720 e 811 milhões" desc="de pessoas em todo o mundo estavam sofrendo de fome" />
          <CardInfo numero="2,4 bilhões" desc="de pessoas estavam sem acesso regular a alimentos adequados." />
          <CardInfo numero="47%" desc="foi a parcela de países sobrecarregados por preços elevados de alimentos" />
        </section>

        <section className={styles.containerImage}>
          <div className={styles.column}>
            <h2 className='title'>A solução</h2>
            <p>Pensando nisso, a <strong>Raízes Solidárias</strong> foi criada. Nosso projeto consiste em uma <strong>horta solidária </strong>mantida por doações e voluntários para a manutenção da horta e o transporte da colheita de alimentos para famílias necessitadas e ONGs responsáveis. </p>

            <p>Nossos doadores tem a opção de escolher no que seu dinheiro será usado: em sementes de diferentes sementes importantes para a nutrição humana ou para a manutenção da horta, com a irrigação e outros itens voltados à nossa horta!</p>

            <div className={styles.buttons}>
              <Link href="/doar" className='btn'>Seja um doador</Link>
              <Link href="/ser-um-voluntario" className='btn'>Seja um voluntário</Link>
            </div>
          </div>

          <div className={styles.column}>

            <Image src="/img-main.jpg" width={500} height={400} />

          </div>

        </section>

      </div>
    </>
  )
}
