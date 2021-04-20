package main

import (
	"fmt"
	"os"
	"sort"

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
	defer f.Close()
	arrDots := polinom.ReadFileOfDots(f)
	sort.Sort(arrDots)

	fmt.Println("Input table:")
	arrDots.PrintDots()

	fmt.Println("Input x value\nInput n - power of Newton polinom")
	x, n := polinom.ReadParams()

	tb, res, err := polinom.NewtonInterpolation(arrDots, x, n)
	if err != nil {
		fmt.Println("error", err)
		os.Exit(1)
	}
	fmt.Println("Input params:")
	polinom.PrintParams(x, n)
	fmt.Println("Result table:")
	tb.PrintTable()
	fmt.Println("Result f(x):")
	fmt.Println(res)

	_, polinomHermit, _ := polinom.HermitInterpolation(arrDots, x, n)
	fmt.Println("Polinom Hermit is")
	fmt.Println(polinomHermit)

	invRes, invPolinom, err := polinom.InvertInterpolation(arrDots, n)
	if err != nil {
		fmt.Println("error", err)
		os.Exit(1)
	}

	fmt.Println("Result table invert:")
	invRes.PrintTable()
	fmt.Println("Result f(x) invert:")
	fmt.Println(invPolinom)
}
