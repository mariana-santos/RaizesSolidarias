import Alimentos from "../Alimentos"
import Horta from "../Horta"

import './style.css'

import { useState } from "react"

export default function GerenciarHorta({ setTela, setSaldo, saldo, setAnimation }) {

    const [novosPlantios, setNovosPlantios] = useState([])

    return (
        <div id="gerenciar-horta">
            <button className="btn btn-secondary" onClick={() => setTela('inicio')}>
                {/* <BsArrowBarLeft /> */}
                Voltar
            </button>
            <Alimentos 
                setNovosPlantios={setNovosPlantios} 
                novosPlantios={novosPlantios} 
                saldo={saldo}
                setSaldo={setSaldo}
                setAnimation={setAnimation}
            />
            <Horta 
                novosPlantios={novosPlantios} 
                saldo={saldo}
                setSaldo={setSaldo}
                setAnimation={setAnimation}
                setNovosPlantios={setNovosPlantios} 
            />
        </div>
    )
}