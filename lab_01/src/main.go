package main

import (
	"fmt"
	"os"

	"./polinom"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Not correct!\n Correct: main.go <file.txt>")
		os.Exit(1)
	}
	f, err := os.Open(os.Args[1])
	if err != nil {
		fmt.Printf("Can't open file %s\n Error: %s\n", os.Args[1], err)
		os.Exit(1)
	}
	arrDots := polinom.ReadFileOfDots(f)
	fmt.Println("Input x (we will find y(x))\nInput n - power of Newton polinom")
	x, n := polinom.ReadParams()

	polinom.PrintDots(&arrDots)
	polinom.PrintParams(x, n)
}
