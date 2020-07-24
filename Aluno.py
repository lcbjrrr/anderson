class Aluno:
    def __init__(self, nome,  sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    

    def nome_completo(self):
        n_c = self.nome + " " +self.sobrenome
        return n_c
    

luiz = Aluno('luiz','barboza')
print(luiz.nome_completo())

