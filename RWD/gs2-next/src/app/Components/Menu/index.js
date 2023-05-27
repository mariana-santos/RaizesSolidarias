import Link from 'next/link'
import styles from './index.css'
import Button from '../Button'

export default function Menu() {
    return (
        <header>
            <Link href='/'> <h1>Raízes Solidárias</h1> </Link>
            <nav>
                <Button />
                <ul>
                    <li>
                        <Link href="/noticias">Notícias</Link>
                    </li>
                    <li>
                        <Link href="/combate-a-fome">Combate à fome</Link>
                    </li>
                    <li>
                        <Link href="/combate-a-fome">Como a tecnologia pode ajudar</Link>
                    </li>
                    <li>
                        <Link href="/raizes-solidarias">Conheça o projeto</Link>
                    </li>
                </ul>
            </nav>
        </header>
    )
}