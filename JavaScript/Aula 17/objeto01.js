let amigo = {nome: 'José', 
    sexo: 'M', 
    peso: 85.4,
    engordar(p){
        console.log('Engordou')
        this.peso += p
    }}
console.log(typeof amigo)
console.log(amigo)
console.log(amigo.nome)
amigo.engordar(2)
console.log(`O ${amigo.nome} pesa ${amigo.peso}/Kg`)

function $almoço()
function _lanche()
function jantar em casa()