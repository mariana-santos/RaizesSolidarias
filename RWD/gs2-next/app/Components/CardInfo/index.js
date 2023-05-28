import './style.css'

export default function CardInfo({ numero, desc }){
    return(
        <div className="card">
            <h2>{numero}</h2>
            <p>{desc}</p>
        </div>
    )
}