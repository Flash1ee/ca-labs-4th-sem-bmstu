package polinom

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"sort"
)

//Dot is one string from file
type Dot struct {
	x    float64
	y    float64
	derY float64
}

// ArrDot is array of dot's from file
type ArrDot []Dot

// Len - return len arrDot
func (arr ArrDot) Len() int {
	return len(arr)
}

func (arr ArrDot) Less(i, j int) bool {
	return arr[i].x < arr[j].x
}

func (arr ArrDot) Swap(i, j int) {
	arr[i], arr[j] = arr[j], arr[i]
}

// AxisSwap is func which swap axis x and y
func (arr ArrDot) AxisSwap() {
	for i := range arr {
		arr[i].x, arr[i].y = arr[i].y, arr[i].x
	}
}

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
	sort.Sort(arr)
	return arr
}

// PrintDots is func which print arr of dot's in console
func (arr ArrDot) PrintDots() {
	fmt.Printf("%6s %6s %6s\n", "X", "Y", "Y'")
	for _, el := range arr {
		fmt.Printf("%6.3f %6.3f %6.3f\n", el.x, el.y, el.derY)
	}
	fmt.Println("")
}

// GetPos return position x in input table + bool error
func (arr ArrDot) GetPos(x float64) (int, int, bool) {

	if arr[len(arr)-1].x < x || arr[0].x > x {
		return 0, 0, false
	}
	left, right := -1, -1

	for i := 1; i < len(arr); i++ {
		if arr[i-1].x <= x && arr[i].x >= x {
			left, right = i-1, i
		}
	}
	return left, right, true
}

// ReadParams is func which read two params : x - num which we must to find, n : power of Newton polinom
func ReadParams() (float64, int) {
	var (
		x float64
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
func PrintParams(x float64, n int) {
	fmt.Printf("X : %6.3f\nn : %6d\n", x, n)
}
