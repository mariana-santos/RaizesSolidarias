import validator from "validator";

export function validaCampo(campo, setError) {
    //função pra validar se o campo tá vazio ou _ (vindos do patternFormat)
    if (!validator.isEmpty(campo.toString()) && !campo.toString().includes('_')) {
        setError(null)
        return true
    }

    else {
        setError('Campo obrigatório!')
        return false
    }
    
}

export function validaNumber(campo, setError) {
    //função pra validar se o campo tá vazio ou _ (vindos do patternFormat)
    console.log(!validator.isEmpty(campo.toString()), !campo.toString().includes('_'), parseFloat(campo))
    if (!validator.isEmpty(campo.toString()) && !campo.toString().includes('_') && parseFloat(campo) > 0) {
        setError(null)
        return true
    }

    else {
        if (validator.isEmpty(campo.toString()) || campo.toString().includes('_'))
            setError('Campo obrigatório!')
        
        if(parseFloat(campo) <= 0)
            setError('Valor inválido!')

        return false
    }
    
}

export function validaEmail(email, setErrorEmail) {
    //se for válido e não for vazio retorna true e remove o erro
    if (!validator.isEmpty(email) && validator.isEmail(email)) {
        setErrorEmail(null)
        return true
    }

    //se cair aqui tem algo errado e entram as validações especificas
    else {
        if (validator.isEmpty(email))
            setErrorEmail('Email é obrigatório!')

        if (!validator.isEmail(email))
            setErrorEmail('Email inválido!')

        //Futuramente aqui terá outro if validando se o email é encontrado na nossa base de dados
        return false
    }
}

export function validaSenha(senha, setErrorSenha) {
    if (!validator.isEmpty(senha) && validator.isLength(senha, { min: 8 })) {
        setErrorSenha(null)
        return true
    }
    else {
        if (!validator.isLength(senha, { min: 8 }))
            setErrorSenha('Senha muito curta!')

        if (senha == '') 
            setErrorSenha('Senha é obrigatória!')
        
        return false
    }
}