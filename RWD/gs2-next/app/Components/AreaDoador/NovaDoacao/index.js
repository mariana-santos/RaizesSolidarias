import { validaCampo } from "../../../utils/validacao";
import Campo from "../../Campo";

import { useMutation } from "react-query";

import { useState } from "react";

import { RiMoneyDollarCircleFill } from "react-icons/ri"
import { NumericFormat } from "react-number-format"

import { toast } from "react-toastify"

export default function NovaDoacao({ setTela, setAnimation, setSaldo }) {

    const [valorDoacao, setValor] = useState(0)
    const [errorValor, setErrorValor] = useState(null)

    const cadastrarDoacao = async (dados_doacao) => {
        const response = await fetch('http://localhost:8080/doacao', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_doacao),
        });

        const data = await response.json();
        console.log(data)

        if (!response.ok || data.error) {
            toast.error(data.error)
            throw new Error('Erro ao cadastrar doação!');
        }
        else {
            toast.success('Depósito realizado com sucesso! Obrigado pela sua contribuição.')
            setAnimation('shake')
            setTimeout(() => setAnimation(''), 500)
        }
        return data;
    };

    const { mutate: doacaoMutate } = useMutation(cadastrarDoacao);

    const cadastrarDoador = async (dados_doador) => {
        const response = await fetch('http://localhost:8080/doador', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados_doador),
        });

        const data = await response.json();
        console.log(data)

        if (!response.ok || data.error) {
            toast.error(response.error)
            throw new Error('Erro ao cadastrar o doador');
        }
        else {
            sessionStorage.setItem('doador', JSON.stringify(data));
            const dados_doacao = {
                id_doacao: 0,
                // TODO: Formatar a data de acordo com o que o json pede
                data_doacao: new Date(),
                qtd_moedas_doacao: valorDoacao,
                ...dados_doador,
            }

            return cadastrarDoacao(dados_doacao);
        }
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
        else {
            sessionStorage.setItem('doador', JSON.stringify(dados_doador));
            const dados_doacao = {
                id_doacao: 0,
                // TODO: Formatar a data de acordo com o que o json pede
                data_doacao: new Date(),
                qtd_moedas_doacao: valorDoacao,
                ...dados_doador,
            }

            return cadastrarDoacao(dados_doacao);
        }
    };

    const cadastrarDoadorMutation = useMutation(cadastrarDoador);
    const depositarMutation = useMutation(atualizarDoador);

    function handleNovaDoacao(e) {
        e.preventDefault();

        // console.log(valorDoacao)
        if (validaCampo(valorDoacao, setErrorValor)) {

            const usuario = typeof window !== 'undefined' ? JSON.parse(sessionStorage.getItem("usuario")) : null;
            const usuarioDoador = typeof window !== 'undefined' ? JSON.parse(sessionStorage.getItem("doador")) : null;

            if (!usuarioDoador) {

                const usuario_doador = {
                    ...usuario,
                    nivel_doador: 1,
                    moedas_doador: valorDoacao
                };

                cadastrarDoadorMutation.mutate(usuario_doador)

            } else {
                // TODO: nesse caso, como o usuario doador ja existe, criar uma lógica pra atualizar o nível
                const usuario_doador = {
                    ...usuario,
                    nivel_doador: 1,
                    moedas_doador: usuarioDoador.moedas_doador + valorDoacao
                };

                depositarMutation.mutate(usuario_doador);
            }
        }
    }

    return (
        <div id="nova-doacao">
            <button className="btn btn-secondary" onClick={() => setTela('inicio')}>
                {/* <BsArrowBarLeft /> */}
                Voltar
            </button>
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
                <button type="button" className="btn" onClick={handleNovaDoacao}>Realizar doação</button>
                {errorValor && <span className="error"> &nbsp; </span>}
            </div>
        </div>
    )
}