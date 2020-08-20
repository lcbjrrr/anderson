package main

import (
	"net/http"
	"fmt"
	"io/ioutil"
)

func main() {

	resp, err := http.Get("http://127.0.0.1:8888/dominio/")

	if err != nil {
		fmt.Println("Ocorreu um erro:", err)
	}

	if resp.StatusCode == 200 {
		fmt.Println("Site: foi carregado com sucesso!")

		body, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			print(err)
		}else{
			fmt.Print(string(body))
		}
		
		

	} else {
		fmt.Println("Site: esta com problemas. Status Code:", resp.StatusCode)
	}

}