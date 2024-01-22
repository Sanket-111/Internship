package main

import (
	"fmt"
	"io"
	"net/http"
)

func requestHanding(w http.ResponseWriter, r *http.Request) {
	body, err := io.ReadAll(r.Body)

	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(string(body))

	resp := "Hello from Server"

	w.Write([]byte(resp))
}

func main() {

	http.HandleFunc("/", requestHanding)
	fmt.Println("Server Listning on Port no 3000")
	http.ListenAndServe("0.0.0.0:3000", nil)

}
