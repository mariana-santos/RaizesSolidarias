import { useEffect, useState } from "react"

import '../../styles/form.css'

import './style.css'

import 'react-toastify/dist/ReactToastify.css';

import Alimentos from "./Alimentos";

import NovaDoacao from "./NovaDoacao";
import GerenciarHorta from "./GerenciarHorta";

export default function AreaVoluntario() {

    const [tela, setTela] = useState('inicio')

    const [valorDoacao, setValor] = useState(0)
    const [errorValor, setErrorValor] = useState(null)

    const [animation, setAnimation] = useState('')

    const [saldo, setSaldo] = useState(50)

    const atualizarSaldo = (novoSaldo) => {
        setSaldo(novoSaldo);
    };

    useEffect(() => {

        const usuarioDoador = JSON.parse(sessionStorage.getItem("doador"))
        if(usuarioDoador) setSaldo(usuarioDoador.moedas_doador)

    }, [])

    return (
        <form id="doacao">
            <div className="row-heading">
                <div className="heading">
                    <h2>Olá, Mariana!</h2>
                    <small>Bem vindo(a) à área do doador. Aqui você pode realizar novos depósitos e gerenciar nossa horta que alimenta várias famílias semanalmente!</small>
                </div>

                <div className="wrap-moedas">
                    <span>{saldo}</span>
                    <div className="moeda">
                        <img src="/coin.png" className={animation} />
                    </div>
                    <small>meu saldo</small>
                </div>
            </div>

            <div className="row-body">

                {tela === 'inicio' ?
                    (<div className="row inicio">
                        <div className="column">
                            <img src="/illustr-horta.png" />
                            <p>Aqui você poderá usar seu saldo para fazer <strong>novos plantios de alimentos ou irrigar os plantios existentes na horta</strong>. Se você preferir, o nosso <strong>sistema escolhe os itens para você!</strong></p>
                            <button className="btn" onClick={() => setTela('gerenciar-horta')}>Gerenciar horta comunitária</button>
                        </div>
                        <div className="column">
                            <img src="/illustr-doacao.svg" />
                            <p>Para aumentar seu saldo, <strong>realize uma nova doação pra nossa horta solidária!</strong> Os valores doados <strong>contribuem na alimentação de famílias carentes</strong> semanalmente. </p>
                            <button className="btn" onClick={() => setTela('nova-doacao')}>Realizar nova doação</button>
                        </div>
                    </div>)
                    : tela === 'nova-doacao' ?
                        (<NovaDoacao 
                            setTela={setTela} 
                            setAnimation={setAnimation}
                            setSaldo={setSaldo}
                            saldo={saldo}
                        />)
                    :
                        (<GerenciarHorta 
                            setTela={setTela} 
                            saldo={saldo}
                            setSaldo={atualizarSaldo}
                            setAnimation={setAnimation}
                        />)}
            </div>
        </form>
    )
}