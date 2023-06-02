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
import { BsCalendarDate } from "react-icons/bs"

import moment from "moment"
import { ToastContainer, toast } from "react-toastify"

import 'react-toastify/dist/ReactToastify.css';
import { MdMoney } from "react-icons/md"
import { RiMoneyDollarCircleFill } from "react-icons/ri"
import { NumericFormat, PatternFormat } from "react-number-format"

export default function AreaVoluntario() {

    const [carregando, setCarregando] = useState(false)

    const hoje = new Date();

    const [data, setData] = useState(hoje);

    const [novoDeposito, setNovoDeposito] = useState(false)
    const [valorDoacao, setValor] = useState(1)

    const [animation, setAnimation] = useState('')


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

    function handleDataAgendamento(e){
        if (data <= new Date()) {
            
        }
    }

    function handleNovaDoacao(e) {
        e.preventDefault();
        toast.success('Depósito realizado com sucesso! Obrigada pela sua contribuição.')
        setNovoDeposito(!novoDeposito)
        setAnimation('shake')

        setTimeout(() => setAnimation(''), 500)

        console.log(animation)
    }

    return (
        <form onSubmit={handleSubmit} id="doacao">
            <ToastContainer 
                position="bottom-right"
                autoClose={2000}
                closeOnClick
                pauseOnHover
            />
            <div className="row-heading">
                <div className="heading">
                    <h2>Olá, Mariana!</h2>
                    <small>Bem vindo(a) à área do doador. Aqui você pode realizar novos depósitos e gerenciar nossa horta que alimenta várias famílias semanalmente!</small>
                </div>

                <div className="wrap-moedas">
                    <span>510</span> 
                    <div className="moeda">
                        <img src="/coin.png" className={animation}/>
                    </div>
                    <small>meu saldo</small>
                </div>
            </div>

            <div className="row-body">

                <div className="novo-deposito">
                    { !novoDeposito ? (
                        <button className="btn" 
                            onClick={() => setNovoDeposito(!novoDeposito)}>Novo depósito</button>
                    ) : (
                        <form id="nova-doacao">
                            <h3>Nova doação</h3>
                            <Campo 
                                type="text"
                                label="Valor do depósito (R$)"
                                icon={<RiMoneyDollarCircleFill />}
                                value={moment(data).format("DD/MM/YYYY")}
                                temMask
                                onChange={(e) => handleDataAgendamento(e)}
                            >
                                <NumericFormat 
                                    prefix={'R$ '}
                                    decimalScale={2}
                                    fixedDecimalScale
                                    decimalSeparator=","
                                    thousandSeparator="."
                                    allowNegative={false}
                                    placeholder="Digite o valor"
                                />
                            </Campo>
                            
                            <button type="button" className="btn" onClick={handleNovaDoacao}>Enviar</button>
                        </form>
                    ) }
                    

                    
                </div>


                <div className="agendamento">

                    {/* Esse bloco só aparece se for um dia futuro e ainda não existir nenhum agendamento no dia */}
                    {/* <div className="novo-agendamento">
                        <h3>Novo agendamento: </h3>

                        <p>Selecione a data no calendário ao lado:</p>
                        <Campo 
                            type="text"
                            icon={<BsCalendarDate />}
                            disabled
                            value={moment(data).format("DD/MM/YYYY")}
                            onChange={(e) => handleDataAgendamento(e)}
                        />
                        
                        <button type="submit" className="btn">Salvar</button>
                    </div> */}
                    
                </div>
            </div>
        </form>
    )
}