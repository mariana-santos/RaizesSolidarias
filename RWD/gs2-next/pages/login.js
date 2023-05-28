import Image from 'next/image'

import Menu from '../app/Components/Menu'

import Link from 'next/link'

import Footer from '../app/Components/Footer'

import { Raleway } from 'next/font/google'

const font = Raleway({ subsets: ['latin'] })

import '../app/globals.css'

import { Quicksand } from 'next/font/google'

const fontBody = Quicksand({ subsets: ['latin'] })

export default function Login() {
  return (
    <div className={fontBody.className}>
      <main className='form-wrapper'>

        <Menu />

        <div className=''>
          
        </div>
      </main>

      <div className=''>
        

      </div>

      <Footer />
    </div>
  )
}
