import { Accordion, AccordionSummary, AccordionDetails, } from "@mui/material"
import { MdOutlineKeyboardArrowDown } from 'react-icons/md'

import { useMutation } from "react-query";

import { toast } from "react-toastify";

export default function Destino({ destino, ehTransportado, destinosDisponiveis, setDestinosDisponiveis, destinosTransportados, setDestinosTransportados }) {

    const removerDestino = async (id_usuario) => {
        console.log(id_usuario)
        console.log(destino)
        const response = await fetch(
            `http://localhost:8080/receptor_destino/${id_usuario}/${destino.id_destino}`,
            {
                method: "DELETE"
            }
        );

        if (!response.ok) {
            toast.error("Erro ao remover destino!");
        } else {
            toast.success(
                "Destino removido com sucesso. Esperamos que consiga transportar para novos destinos em breve!"
            );
            setDestinosTransportados((destinos) =>
                destinos.filter(
                    (receptor_destino) =>
                        receptor_destino.destino.id_destino !== destino.id_destino
                )
            );
            setDestinosDisponiveis((destinos) => [...destinos, destino]);
        }
    };

    function handleRemoverDestino(e) {
        e.preventDefault()

        const usuario = JSON.parse(sessionStorage.getItem("receptor"))
        console.log(usuario.id_usuario)
        removerDestinoMutation.mutate(usuario.id_usuario)
    }

    const removerDestinoMutation = useMutation(removerDestino);

    const adicionarDestino = async (receptor_destino) => {
        const response = await fetch("http://localhost:8080/receptor_destino/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(receptor_destino)
        });

        if (!response.ok) {
            toast.error("Erro ao adicionar destino!");
        } else {
            toast.success(
                "Destino adicionado com sucesso. Esperamos que consiga levar muitas colheitas aos destinos!"
            );

            setDestinosDisponiveis((destinos) =>
                destinos.filter((destino) => destino.id_destino !== receptor_destino.destino.id_destino)
            );
            setDestinosTransportados((destinos) => [...destinos, receptor_destino]);
        }
    };

    const adicionarDestinoMutation = useMutation(adicionarDestino);

    function handleAdicionarDestino(e, destino) {
        e.preventDefault()

        const usuario = JSON.parse(sessionStorage.getItem("receptor"))

        const receptor_destino = {
            receptor: usuario,
            destino: destino
        }

        console.log(receptor_destino)
        adicionarDestinoMutation.mutate(receptor_destino)
    }

    return (
        <Accordion className="destino">
            <AccordionSummary expandIcon={<MdOutlineKeyboardArrowDown />} className="resumo">
                <p>
                    <strong>Destino #{("00" + destino.id_destino).slice(-4)}: </strong>
                    <small>{destino.endereco_destino}</small>
                </p>
            </AccordionSummary>

            <AccordionDetails className="detalhes">
                <p>
                    <a href={`https://www.google.com/maps/search/${destino.endereco_destino}`} target="_blank">
                        <strong>Endereço: </strong>{destino.endereco_destino}
                    </a>
                </p>
                <p><strong>Responsável: </strong>{destino.responsavel_destino}</p>
                <p><strong>Contato: </strong>{destino.cel_destino}</p>
                <p><strong>Quantidade de dependentes: </strong>{destino.qtd_dependentes_destino}</p>

                {ehTransportado ?
                    <>
                        <a className="btn"
                            target="_blank"
                            href={`https://wa.me/55${destino.cel_destino}`}>
                            Entrar em contato
                        </a>
                        <button
                            className="btn btn-tertiary"
                            onClick={(e) => handleRemoverDestino(e, destino)}>
                            Remover dos meus destinos
                        </button>
                    </> :
                    <>
                        <button
                            className="btn"
                            onClick={(e) => handleAdicionarDestino(e, destino)}>
                            Adicionar aos meus destinos
                        </button>
                    </>}

            </AccordionDetails>
        </Accordion>
    )
}