
class Aluno{
    String nome;
    String sobrenome;

    Aluno(String nome, String sobrenome){
        this.nome=nome;
        this.sobrenome=sobrenome;
    }

    String nome_completo(){
        String n_c = this.nome + " " +this.sobrenome;
        return n_c;
    }

    public static void main(String[] args) {
        Aluno luiz = new Aluno("Luiz","Barboza Jr"); 
        System.out.println(luiz.nome_completo());

    }

}