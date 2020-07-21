
//exemplo 1 

function calcMedia(notas){
    soma = 0
    for (i=0;i<notas.length;i=i+1){
        soma = soma + notas[i]
    }
    return soma / notas.length
}

notasTurma = [5.0,5.0,6.0,6.0,7.0,7.0,8.0,8.0,9.0,9.0]
mt = calcMedia(notasTurma)
console.log(mt)

turma = {"luiz":5,
        "anderson":10};
nota_luiz = turma["luiz"]
console.log(nota_luiz);




function notasFinal(turma){
    for (aluno in turma){
        notas_aluno = turma[aluno]  
        console.log(notas_aluno )
        media_aluno = calcMedia(notas_aluno)  
        console.log(aluno +" "  +media_aluno) 
    }    

}

turmaFinal = {"luiz":[5.0,6.0,7.0],
             "anderson":[7.0,8.0,9.0]};
notasFinal(turmaFinal)
