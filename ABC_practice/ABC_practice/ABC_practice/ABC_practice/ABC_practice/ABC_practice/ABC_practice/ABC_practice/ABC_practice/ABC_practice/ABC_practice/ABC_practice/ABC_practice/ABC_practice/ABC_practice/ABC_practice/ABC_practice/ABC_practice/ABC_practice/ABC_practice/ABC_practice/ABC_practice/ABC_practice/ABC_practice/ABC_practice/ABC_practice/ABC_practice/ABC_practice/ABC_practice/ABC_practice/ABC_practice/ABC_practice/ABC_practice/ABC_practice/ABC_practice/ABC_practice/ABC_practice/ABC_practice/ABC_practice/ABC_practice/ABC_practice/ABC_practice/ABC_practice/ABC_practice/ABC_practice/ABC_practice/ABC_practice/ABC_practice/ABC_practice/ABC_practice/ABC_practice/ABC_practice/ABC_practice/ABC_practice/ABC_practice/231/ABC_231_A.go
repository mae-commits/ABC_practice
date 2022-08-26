package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	input = strings.TrimSpace(input)
	metre, err := strconv.ParseFloat(input, 64)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(metre / 100)
}
