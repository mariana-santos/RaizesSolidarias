import Link from 'next/link'
import styles from './index.css'
import Button from '../Button'
import * as React from "react";

import { Raleway } from 'next/font/google'

const font = Raleway({ subsets: ['latin'] })

import { useRouter } from 'next/router';

import { useState, useEffect } from 'react';

export default function Menu() {

    const router = useRouter();
    const [domLoaded, setDomLoaded] = useState(false);

    useEffect(() => {
        let prevScrollpos = window.pageYOffset;
        window.onscroll = function () {
            let currentScrollPos = window.pageYOffset;

            if (window.scrollY > 300) {

                if (prevScrollpos < currentScrollPos) {
                    document.querySelector("header").classList.add('scroll');
                } else if (currentScrollPos > window.innerHeight / 2) {
                    document.querySelector("header").classList.remove('scroll');
                    document.querySelector("header").classList.add('expanded');
                } else {
                    document.querySelector("header").classList.remove('expanded');
                }

                prevScrollpos = currentScrollPos;
            }
        }
        setDomLoaded(true);
    }, [])

    const usuario = typeof window !== 'undefined' ? JSON.parse(sessionStorage.getItem("usuario")) : null;

    const handleLogout = () => {
        // Limpeza dos dados no sessionStorage
        if (typeof window !== 'undefined') {
            sessionStorage.removeItem('usuario')
            sessionStorage.removeItem('receptor')
            sessionStorage.removeItem('doador')
            router.push('/login')
        }
    }

    return (
        <header>
            <div className='space'></div>
            <div className='menu-wrapper'>
                <Link href='/' className={font.className}> <h1>Raízes Solidárias</h1> </Link>
                <nav>
                    <Button />
                    <ul>
                        <li>
                            <Link href="/" id='inicio'>Início</Link>
                        </li>
                        <li>
                            <Link href="/#noticias">Notícias</Link>
                        </li>
                        <li>
                            <Link href="/contato">Contato</Link>
                        </li>
                        <li>
                            <Link href="/#solucao">Conheça o projeto</Link>
                        </li>
                        <li>
                            <Link href="/#como-ajudar">Como ajudar</Link>
                        </li>
                    </ul>
                </nav>
            </div>

            {/* O domloaded garante que tudo foi renderizado antes de pegar os dados do usuário pra prevenir o erro "hydration" do nextjs */}
            {domLoaded && (
                <div className='login-area'>

                    {usuario ?
                        (<h2>Olá, <Link href="/perfil">{usuario.nome_usuario.split(' ')[0]}!</Link></h2>) :
                        (<h2><Link href="/login">Bem vindo(a)!</Link></h2>)}

                    {usuario ? (
                        <button onClick={handleLogout}>
                            sair da minha conta
                        </button>
                    ) : (
                        <p>Faça <Link href="/login">login</Link> ou <Link href="/cadastro">cadastre-se</Link></p>
                    )}

                </div>
            )}
        </header>
    )
}
