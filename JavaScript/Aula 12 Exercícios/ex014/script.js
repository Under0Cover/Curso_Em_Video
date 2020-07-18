function carregar(){
    var mensagem = window.document.getElementById('mensagem')
    var imagem = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    var minuto = data.getMinutes()
    mensagem.innerHTML = `Agora são ${hora} horas e ${minuto} minutos!`
    if (hora < 12) {
        //BOM DIA!
        imagem.src = 'foto-manha.png'
        document.body.style.background = '#f08535'
    } else if (hora < 19) {
        //BOA TARDE
        imagem.src = 'foto-tarde.png'
        document.body.style.background = '#9f6a5b'
    } else {
        // BOA NOITE
        imagem.src = 'foto-noite.png'
        document.body.style.background = '#34484f'
    }
}