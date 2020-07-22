//COMEÇANDO A TRABALHAR COM VETOR
let vetor = [5,8,9,0]
console.log(vetor)
console.log(`Nosso vetor é composto por: ${vetor}`)
console.log('-------------------')
// AUMENTANDO A POSIÇÃO DE VALORES DO VETOR NA POSIÇÃO 4
vetor[3] = 2
console.log(`Nosso vetor é composto por: ${vetor}`)
console.log('-------------------')
// AUMENTANDO A POSIÇÃO DE VALORES DO VETOR E COLOCANDO NA ÚLTIMA POSIÇÃO
vetor.push(7)
console.log(`Nosso vetor é composto por: ${vetor}`)
console.log('-------------------')
// COMO SABER O CUMPRIMENTO DE UM VETOR?
console.log(`Nosso vetor é de ${vetor.length} posições e composto por: ${vetor}`)
console.log('-------------------')
// COLOCANDO OS VALORES DO VETOR EM ORDEM CRESCENTE
console.log(`Nosso vetor antes de ser colocado em ordem é: ${vetor} e depois é: ${vetor.sort()}`)
console.log(`Nosso vetor é composto por: ${vetor}`)
console.log('-------------------')
// SELECIONANDO O VALOR PELA POSIÇÃO DO VETOR
console.log(`O quarto valor do nosso vetor é o ${vetor[3]}`)
console.log(`Nosso vetor é composto por: ${vetor}`)
console.log('-------------------')
// MOSTRANDO OS VALORES DO VETOR SEM A FORMATAÇÃO UM A UM
console.log(`O valor na posição 1 é: ${vetor[0]}`)
console.log(`O valor na posição 2 é: ${vetor[1]}`)
console.log(`O valor na posição 3 é: ${vetor[2]}`)
console.log(`O valor na posição 4 é: ${vetor[3]}`)
console.log(`O valor na posição 5 é: ${vetor[4]}`)
// MOSTRANDO OS VALORES DO VETOR SEM A FORMATAÇÃO EM CONJUNTO
// EXEMPLO ESTÁ NO ARQUIVO "VETOR NA TELA.JS"
console.log('-------------------')
// FAZENDO BUSCA NOS VALORES DO VETOR PARA RETORNAR A POSIÇÃO EM QUE ELE SE ENCONTRA
let pos = vetor.indexOf(8)
console.log(`O valor 8 está na posição: ${pos}`)
// CLARO QUE ISSO AQUI VAI VIRAR UMA VARIÁVEL DENTRO DE UMA VARIÁVEL
console.log('-------------------')
// FAZENDO UMA BUSCA DE VALOR INEXISTENTE PARA RETORNAR A POSIÇÃO -1
let pos1 = vetor.indexOf(4)
console.log(`O valor 4 está na posição: ${pos1}`)
// CASO NÃO QUEIRA QUE O SISTEMAS MOSTRE -1
// PODE FAZER UM IF - ELSE
console.log('-------------------')
if (pos1 == -1) {
    console.log(`O valor não foi encontrado`)
} else {
    console.log(`O valor 4 está na posição: ${pos}`)
}