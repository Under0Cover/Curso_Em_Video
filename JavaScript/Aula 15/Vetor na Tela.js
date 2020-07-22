let valores = [8, 1, 7, 4, 2, 9]

// MOSTRANDO O VETOR COMPLETO USANDO O FOR
for (let pos=0; pos < valores.length; pos++) {
    console.log(`A posição ${pos} tem o valor ${valores[pos]}`)
}
console.log('-------------------')
// USAR O SORT AQUI PRA VISUALIZAR A DIFERENÇA ENTRE AS RESPOSTAS
valores.sort()
// MOSTRANDO O MESMO VETOR, COM O FOR - IN
for (let pos in valores) {
    console.log(`A posição ${pos} tem o valor ${valores[pos]}`)
}