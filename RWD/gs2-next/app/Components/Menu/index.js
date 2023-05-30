'use client'

import Link from 'next/link'
import styles from './index.css'
import Button from '../Button'
import * as React from "react";

import { Raleway } from 'next/font/google'

const font = Raleway({ subsets: ['latin'] })

export default function Menu() {

    React.useEffect(() => {
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
    }, [])

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
                            <a href="/#noticias">Notícias</a>
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
            </div>

            <div className='login-area'>
                    <Link href="/perfil">
                        <h2>Bem vindo(a), <strong>Mariana!</strong></h2>
                    </Link>
                    <p>Faça <Link href="/login">login</Link> ou <Link href="/cadastro">cadastre-se</Link></p>
                </div>
        </header>
    )
}