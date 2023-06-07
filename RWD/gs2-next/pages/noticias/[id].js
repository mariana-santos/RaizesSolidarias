import Footer from "../../app/Components/Footer";
import Menu from "../../app/Components/Menu";

import './style.css'

import noticias from '../../app/assets/data/noticias.json'

import { Quicksand } from 'next/font/google'

import Noticias from "../../app/Components/Noticias";

const fontBody = Quicksand({ subsets: ['latin'] })

import { useQuery } from "react-query";
import { useState, useEffect } from "react";

export default function Noticia({ id }) {

  const [noticia, setNoticia] = useState({})

    const { isLoading, error, data } = useQuery('repoNoticiasData', () =>
        fetch(`http://localhost:8080/noticia/`)
        .then((res) => res.json())
    );

    useEffect(() => {
      if (data && Array.isArray(data)) {
        const filteredNoticia = data.find((noticia) => noticia.id == id);
        setNoticia(filteredNoticia || {});
      }
    }, [data, error, isLoading, id])

    if (isLoading) return 'Carregando...'

    if (error) return 'Ocorreu um erro: ' + error.message

    console.log(noticia)

    return (
      <div>
        <section id="noticia" className={fontBody.className}>
          <Menu />

          <main className="principal">
            <div className="imagem" style={{backgroundImage: `url(${noticia.imagem})`}} />
            <div className="desc">
              <h2 className="title">{noticia.titulo}</h2>
              <p className="content">{noticia.resumo}</p>
            </div>
          </main>

          <section id="texto">

            <div className="content">
              <h2>{noticia.titulo}</h2>
              <p>{noticia.conteudo}</p>
            </div>
            

            <div id="relacionados">
              <h3 className="title">Outros assuntos</h3>  
              <Noticias />
            </div>
          </section>

          <Footer />
        </section>
      </div>
    );
  }
  
  export async function getServerSideProps({ params }) {
    const { id } = params;
    return {
      props: {
        id
      }
    };
  }
  