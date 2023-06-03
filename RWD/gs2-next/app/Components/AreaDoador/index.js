import { useState } from "react"

// import Campo from "../Campo"

import validator from "validator"

import '../../styles/form.css'

import './style.css'

import 'react-calendar/dist/Calendar.css';

import Campo from "../Campo"

import moment from "moment"
import { ToastContainer, toast } from "react-toastify"

import 'react-toastify/dist/ReactToastify.css';
import { RiMoneyDollarCircleFill } from "react-icons/ri"
import { NumericFormat } from "react-number-format"

import { QueryClient, QueryClientProvider } from 'react-query'
import Alimentos from "./Alimentos";

import { validaCampo } from "../../utils/validacao";

import { useMutation } from "react-query";

export default function AreaVoluntario() {

    const [carregando, setCarregando] = useState(false)

    const hoje = new Date();

    const [data, setData] = useState(hoje);

    const [novoDeposito, setNovoDeposito] = useState(false)

    const [valorDoacao, setValor] = useState(0)
    const [errorValor, setErrorValor] = useState(null)

    const [animation, setAnimation] = useState('')

    const [saldo, setSaldo] = useState(0)

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

    const cadastrarDoador = async (dados_doador) => {
        const response = await fetch('http://localhost:8080/doador', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_doador),
        });
     
        const data = await response.json();

        if (!response.ok || data.error) {
            toast.error(response.error)
            throw new Error('Erro ao cadastrar o doador');
        }
        else{
            console.log(data)
            sessionStorage.setItem('doador', JSON.stringify(data));
            toast.success('Depósito realizado com sucesso! Obrigada pela sua contribuição.')
        }

        return data;
    };

    const atualizarDoador = async (dados_doador) => {
        const response = await fetch(`http://localhost:8080/doador/${dados_doador.id_usuario}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_doador),
        });

        if (!response.ok) {
            toast.error('Erro ao atualizar dados');
            throw new Error('Erro ao atualizar o usuário');
        }
        else{
            sessionStorage.setItem('doador', JSON.stringify(dados_doador));
            // TODO: AQUI VAMOS FAZER MAIS UMA REQUISIÇÃO P CADASTRAR A DOAÇÃO
        }

        toast.success('Sucesso ao atualizar os dados!');
    };

    const { mutate } = useMutation(cadastrarDoador);
    const { depositar } = useMutation(atualizarDoador);

    function handleNovaDoacao(e) {
        e.preventDefault();

        // console.log(valorDoacao)
        if(validaCampo(valorDoacao, setErrorValor)){

            const usuario = typeof window !== 'undefined' ? JSON.parse(sessionStorage.getItem("usuario")) : null;

            if(!sessionStorage.getItem("doador")){

                const usuario_doador = {
                    ...usuario,
                    nivel_doador: 1,
                    moedas_doador: valorDoacao
                };
    
                mutate(usuario_doador)

            } else{
                // TODO: nesse caso, como o usuario doador ja existe pegar o valor das moedas e só acrescentar a doação, 
                // além criar uma lógica pra atualizar o nível
                const usuario_doador = {
                    ...usuario,
                    nivel_doador: 1,
                    moedas_doador: valorDoacao
                };
    
                atualizarDoador(usuario_doador)
            }

            // toast.success('Depósito realizado com sucesso! Obrigada pela sua contribuição.')
            // setNovoDeposito(!novoDeposito)
            // setAnimation('shake')
    
            // setTimeout(() => setAnimation(''), 500)
        }

        
    }

    const queryClient = new QueryClient()

    return (
        <form onSubmit={handleSubmit} id="doacao">
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
                        <div id="nova-doacao">
                            <h3>Nova doação</h3>
                            <Campo 
                                type="text"
                                label="Valor do depósito (R$)"
                                icon={<RiMoneyDollarCircleFill />}
                                temMask
                                errorMsg={errorValor}
                            >
                                <NumericFormat 
                                    prefix={'R$ '}
                                    decimalScale={2}
                                    fixedDecimalScale
                                    decimalSeparator=","
                                    thousandSeparator="."
                                    allowNegative={false}
                                    placeholder="Digite o valor"
                                    value={valorDoacao}
                                    onValueChange={(valor) => setValor(valor.floatValue)}
                                />
                            </Campo>
                            <div className="wrap-btn">
                                <button type="button" className="btn" onClick={handleNovaDoacao}>Enviar</button>
                                { errorValor && <span class="error"> &nbsp; </span>}
                            </div>
                            
                        </div>
                    ) }
                </div>

                <QueryClientProvider client={queryClient}>
                    <Alimentos />
                </QueryClientProvider>


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