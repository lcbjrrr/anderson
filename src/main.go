package main

import (
	"fmt"
	"pacote"
)

func main(){
	nome := "luiz";
	sobrenome := "barboza";
	
	luiz:= pacote.NomeCompleto(nome,sobrenome)
	fmt.Println(luiz)
}