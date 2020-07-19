function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = window.document.getElementById('txtano')
    var res = window.document.querySelector('div#res')
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert('[ERRO] Confira os dados digitados e tente novamente!!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 4) {
                // bebê
                img.setAttribute('src','homem-bebe.png')
            } else if (idade < 15) {
                // criança
                img.setAttribute('src', 'homem-menino.png')
            } else if (idade < 21) {
                // adolecente
                img.setAttribute('src', 'homem-ado.png')
            } else if (idade < 60) {
                // adulto
                img.setAttribute('src', 'homem-adulto.png')
            } else {
                // idoso
                img.setAttribute('src', 'homem-idoso.png')
            }

        } else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 4) {
                // bebê
                img.setAttribute('src','mulher-bebe.png')
            } else if (idade < 15) {
                // criança
                img.setAttribute('src','mulher-menina.png')
            } else if (idade < 21) {
                // adolecente 
                img.setAttribute('src','mulher-menina.pmg')
            } else if (idade < 60) {
                // adulto
                img.setAttribute('src','mulher-adulto.png')
            } else {
                // idoso
                img.setAttribute('src','mulher-idosa.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos.`
        res.appendChild(img)
        // Como eu não possuo Pothoshop e não consigo rodar no meu Note
        // algumas imagens tem tamanhos diferentes
        // e por mais que eu configure, não ficaram centralizadas
    }
}
