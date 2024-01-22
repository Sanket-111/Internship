package main

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
)

func main() {
	data := []string{
		"Hello from Client1", "Hello from Client2", "Hello from Client3", "Hello from Client4",
	}

	for i := 0; i < len(data); i++ {
		// jsonData, err := json.Marshal(data[i])
		resp, err := http.Post("http://server-container:3000", "text/plain", bytes.NewBufferString(data[i]))
		if err != nil {
			fmt.Println(err)
			return
		}

		defer resp.Body.Close()

		body, err := io.ReadAll(resp.Body)

		if err != nil {
			fmt.Println(err)
			return
		}

		fmt.Println(string(body))
	}

}
