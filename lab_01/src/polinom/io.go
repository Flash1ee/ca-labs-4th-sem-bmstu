package polinom

import (
	"bufio"
	"fmt"
	"io"
	"os"
)

//Dot is one string from file
type Dot struct {
	x    float32
	y    float32
	derY float32
}

// ArrDot is array of dot's from file
type ArrDot []Dot

//ReadFileOfDots is func which read table of dot's from file and return array of Dots
func ReadFileOfDots(f *os.File) ArrDot {
	rd := bufio.NewReader(f)
	var (
		arr ArrDot
		cur Dot
	)
	for {
		n, err := fmt.Fscanln(rd, &cur.x, &cur.y, &cur.derY)
		if err == io.EOF {
			break
		}
		if n != 3 {
			panic("bad file string")
		}
		arr = append(arr, cur)
	}
	return arr
}

// PrintDots is func which print arr of dot's in console
func PrintDots(arr *ArrDot) {
	fmt.Printf("%6s %6s %6s\n", "X", "Y", "Y'")
	for _, el := range *arr {
		fmt.Printf("%6.3f %6.3f %6.3f\n", el.x, el.y, el.derY)
	}
}

// ReadParams is func which read two params : x - num which we must to find, n : power of Newton polinom
func ReadParams() (float32, int) {
	var (
		x float32
		n int
	)
	_, err := fmt.Scan(&x)
	if err != nil {
		panic(err)
	}
	_, err = fmt.Scan(&n)
	if err != nil || n < 1 || n > 4 {
		panic(err)
	}
	return x, n
}

// PrintParams is func which print params
func PrintParams(x float32, n int) {
	fmt.Printf("X : %6.3f\nn : %6d\n", x, n)
}
