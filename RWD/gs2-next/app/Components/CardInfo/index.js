import Link from 'next/link'
import './style.css'

export default function CardInfo({ titulo, desc, tem_botao, txt_botao }){

    const usuario = typeof window !== 'undefined' ? JSON.parse(sessionStorage.getItem("usuario")) : null;

    return(
        <div className="card">
            <h2>{titulo}</h2>
            <p>{desc}</p>
            {tem_botao && 
                <Link href={usuario ? '/perfil' : '/cadastro'} className='btn'>{txt_botao}</Link>}
        </div>
    )
}