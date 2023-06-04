import Alimentos from "../Alimentos"
import Horta from "../Horta"

import './style.css'

export default function GerenciarHorta({ setTela }) {
    return (
        <div id="gerenciar-horta">
            <button className="btn btn-secondary" onClick={() => setTela('inicio')}>
                {/* <BsArrowBarLeft /> */}
                Voltar
            </button>
            <Alimentos />
            <Horta />
        </div>
    )
}