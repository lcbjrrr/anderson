filme = {
    "O Rei Leao": [9,5],
    "50 Tons de Cinza": [17,5],
    "Little & Stitch": [8,5],
    "Tarzan": [14,5],
}
while True:
    Escolha = input("Qual filme voce quer assistir?:").strip().title()
    if Escolha in filme:
        age = int(input("Quantos anos voce tem?").strip())
        
        
        if age>= filme[Escolha][0]:
            num_de_assentos = filme[Escolha][1]
            if num_de_assentos>0:   
                print("Aproveite o filme!")
            filme[Escolha][1] = filme[Escolha][1]-1
        else:
                print("Desculpe, esgotamos!")
    else:
        print("Voce eh muito novo para assistir ao filme")


else: 
        print("Nao temos esse filme")




