import { useState } from "react"

// import Campo from "../Campo"

import validator from "validator"

import '../../styles/form.css'

import './style.css'

import { Switch, FormControlLabel, } from "@mui/material"

import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

import Moment from "react-moment"
import Campo from "../Campo"
import { GiWeight } from "react-icons/gi"

import moment from "moment"
import { ToastContainer, toast } from "react-toastify"

import 'react-toastify/dist/ReactToastify.css';

export default function AreaTransportador() {

    const [carregando, setCarregando] = useState(false)

    const [habilitado, setHabilitado] = useState(false)

    const [carga, setCarga] = useState(0);

    const [cep, setCep] = useState('');
    const cidade = useState('São Paulo');
    const [logradouro, setLogradouro] = useState('')
    const [numero, setNumero] = useState('')
    const [complemento, setComplemento] = useState('')

    function handleSubmit(e) {

        e.preventDefault();

        // if (validaEmail() && validaSenha()) {
        // setCarregando(true)

        // fetch(`http://localhost:8080/InvestiumAPI/rest/usuario/${email}/${senha}`)
        //   .then((resp) => resp.json())
        //   .then((data) => {
        //     setCarregando(false)
        //     if (data.nome && data.email && data.senha) {
        //       toast.success('Usuário autenticado! Aguarde para ser direcionado.')
        //       const dadosString = JSON.stringify(data);
        //       sessionStorage.setItem("dadosUsuario", dadosString);
        //       setUser(data)
        //       setTimeout(() => {
        //         window.location.href = '/perfil'
        //       }, 2000)
        //     } else {
        //       toast.error('Email ou senha incorretos.')
        //     }
        //   })
        //   .catch((error) => {
        //     console.error(error)
        //     setCarregando(false)
        //   });
        // }

        console.log(data)
    }

    function handleData(data) {
        if (data <= new Date()) {
            handleDataAgendamento()
            // Futuramente esse erro só vai aparecer caso seja um novo agendamento: 
            // ou seja, se o dia selecionado não tiver nenhum agendamento cadastrado 
            // (que é quando o formulário de novo agendamento é mostrado)
            toast.error("A data não pode ser hoje ou dias anteriores!")
        }
        else setData(data)
    }

    function handleDataAgendamento(e) {
        if (data <= new Date()) {

        }
    }

    function handleSelecaoChange(e) {
        setTurno(e.target.value);
    };

    return (
        <form onSubmit={handleSubmit} id="transporte">
            <ToastContainer
                position="bottom-right"
                autoClose={2000}
                closeOnClick
                pauseOnHover
            />
            <div className="row-heading">
                <div className="heading">
                    <h2>Área do transportador</h2>
                    <small>Bem vindo(a) à área do transportador! Aqui você pode cadastrar os dados do seu veículo e das colheitas disponíveis para entrega.</small>
                </div>

                <div className="wrap-switch">
                    <FormControlLabel
                        value="habilitado"
                        control={<Switch value={habilitado} onChange={(e) => setHabilitado(e.target.checked)} />}
                        label={`${habilitado ? 'Desabilitar' : 'Habilitar'} área do transportador`}
                        labelPlacement="start"
                    />
                </div>
            </div>

            <div className="row-body">
                {!habilitado && <div className="mask">
                    Para transportar uma nova colheita a algum de nossos destinos, habilite a área do transportador no botão acima
                </div>}

                <div className="transporte">

                    {/* Se a tabela transporte ainda não existir pra esse usuário, vai ser mostrado esse bloco pra cadastrar os dados iniciais da tabela */}
                    <div className="novo-agendamento">
                        <h3>Dados iniciais: </h3>

                        <p>Endereço:</p>
                        <small>É importante que seu endereço seja na cidade de <strong>São Paulo</strong>, que é onde nossa horta é realizada</small>

                        <Campo
                            type="text"
                            value={cep}
                            onChange={(e) => setCep(e.target.value)}
                            label="CEP"
                            placeholder="Digite seu CEP"
                        />

                        <Campo
                            type="text"
                            value={logradouro}
                            onChange={(e) => setLogradouro(e.target.value)}
                            label="Logradouro (rua)"
                            placeholder="Digite seu logradouro"
                        />

                        <Campo
                            type="text"
                            value={numero}
                            onChange={(e) => setNumero(e.target.value)}
                            label="Número"
                            placeholder="Digite seu número"
                        />

                        <Campo
                            type="text"
                            value={complemento}
                            onChange={(e) => setComplemento(e.target.value)}
                            label="Complemento"
                            placeholder="Digite seu complemento"
                        />

                        <p>Capacidade de carga do veículo:</p>
                        <Campo
                            type="number"
                            icon={<GiWeight />}
                            value={carga}
                            onChange={(e) => setCarga(e.target.value)}
                            min={1}
                        />

                        <button type="submit" className="btn">Salvar</button>
                    </div>

                </div>
            </div>
        </form>
    )
}