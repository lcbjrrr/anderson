
 


function Aluno( n,  sn){
    this.nome = n
    this.sobrenome =sn
    

    this.nome_completo = function() {
        n_c = this.nome + " " +this.sobrenome;
        return n_c;
    }


}

luiz = new Aluno("Luiz","Barboza");
console.log(luiz.nome_completo())

