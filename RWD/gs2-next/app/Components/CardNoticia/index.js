import Link from "next/link";

import './style.css'

export default function CardNoticia({ id, titulo, imagem }){
    return(
        <Link href={`/noticias/${id}`} className="card card-noticia" style={{backgroundImage: `url('${imagem}')`}}>
            <div className="wrap-img" >
                <h3>{titulo}</h3>
            </div>
        </Link>
    )
}