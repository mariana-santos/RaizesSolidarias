import './globals.css'
import { Quicksand } from 'next/font/google'

const font = Quicksand({ subsets: ['latin'] })

export const metadata = {
  title: 'Raízes Solidárias',
  description: 'um website ...',
}

export default function RootLayout({ children }) {
  return (
    <html lang="pt-br">
      <body className={font.className}>{children}</body>
    </html>
  )
}
