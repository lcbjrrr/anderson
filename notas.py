


def calc_media(notas):
    soma = 0
    for i in range(0,len(notas),1):
        soma = soma + notas[i]
    return soma / len(notas)

notas_turma = [5,10,6.0,6.0,7.0,7.0,8.0,8.0,9.0,9.0]
mt = calc_media(notas_turma)
print(mt)



def media_dicionario_turma(dic_turma):
    soma=0
    for nome_aluno in dic_turma:
        nota_aluno = dic_turma[nome_aluno]
        soma = soma + nota_aluno
    return soma/ len(dic_turma)

turma_dic = {"luiz":5.0,
        "anderson":10.0}
mdt = media_dicionario_turma(turma_dic)
print(mdt)



def notas_final(turma):
    for nome_aluno in turma:
        notas_aluno = turma[nome_aluno]
        media_aluno = calc_media(notas_aluno)
        print(nome_aluno +" "  +str(media_aluno)) 

turma_final = {"luiz":[5,6,7],
             "anderson":[7,8,9]}
notas_final(turma_final) 








