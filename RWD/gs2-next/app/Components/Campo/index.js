import './style.css'

export default function Campo (props){
    const { label, errorMsg, id, icon, 
            type, placeholder, value, temMask,
            onChange, accept, onKeyUp, disabled, min
        } = props
    return(
        <div className={`campo ${disabled ? 'disabled' : ''} ${icon ? 'has-icon' : ''}`}>
            <label htmlFor={id}>{label}</label>
            <div className="wrap_input">
                {icon}
                { temMask ? (props.children) : 
                    <input 
                        type={type} 
                        placeholder={placeholder} 
                        id={id} 
                        value={value}
                        onChange={onChange}
                        onKeyUp={onKeyUp}
                        accept={accept}
                        disabled={disabled}
                        min={min}
                    />
                }
            </div>
            { errorMsg != null && <span className='error' > {errorMsg} </span> }
        </div>
    )
}