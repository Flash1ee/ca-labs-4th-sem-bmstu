package polinom

import (
	"errors"
	"fmt"
	"sort"
)

// DifTable if difference table for making Newton polinom
type DifTable [][]float64

// PrintTable is func for output
func (tb DifTable) PrintTable() {
	for _, str := range tb {
		for _, num := range str {
			fmt.Printf("%6.3f ", num)
		}
		fmt.Print("\n")
	}
	fmt.Print("\n")
}

// GetDots is func which return interpolar table
func GetDots(arr ArrDot, x float64, power int) (ArrDot, error) {
	res := make(ArrDot, 0)
	left, right, err := arr.GetPos(x)
	if !err {
		fmt.Print("error")
		return res, errors.New("input x out of table")
	}
	res, cnt := append(res, arr[left], arr[right]), 2
	left--
	right++
	for cnt < power+1 {
		if left >= 0 {
			res = append(res, arr[left])
			left--
			cnt++
		}
		if right < len(arr) && cnt < power+1 {
			res = append(res, arr[right])
			right++
			cnt++
		}
	} //sort.Sort(res)
	return res, nil
}

// NewtonInterpolation return value f(x)
func NewtonInterpolation(arr ArrDot, x float64, n int) (DifTable, float64, error) {
	dots, err := GetDots(arr, x, n)
	if err != nil {
		return nil, 0, err
	}
	res := NewtonTablePreFill(n, dots)
	polinom, xOfPolinom := dots[0].y, 1.0
	// Fill other table
	for i := 2; i < n+2; i++ {
		for j := 0; j < len(dots)-i+1; j++ {
			res[j][i] = (res[j][i-1] - res[j+1][i-1]) / (res[j][0] - res[j+i-1][0])
			if j == 0 {
				xOfPolinom *= (x - res[i-2][0])
				polinom += (xOfPolinom * res[j][i])
			}
		}
	}
	return res, polinom, nil
}

// DifTablePreFill is func which fill two columns of DifTable
func NewtonTablePreFill(size int, dots ArrDot) DifTable {
	res := make(DifTable, size+1)
	for i := 0; i < len(dots); i++ {
		res[i] = make([]float64, size+2)
		res[i][0], res[i][1] = dots[i].x, dots[i].y
	}
	return res
}

// HermitTablePreFill is func which fill three columns of DifTable
func HermitTablePreFill(size int, dots ArrDot) DifTable {
	res := make(DifTable, size+1)
	k, der := 0, 0
	for i := 0; i < size+1; i += 2 {
		res[i] = make([]float64, size+2)
		res[i][0], res[i][1], res[i][2] = dots[k].x, dots[k].y, dots[k].derY
		if i+1 < size+1 {
			res[i+1] = make([]float64, size+2)
			res[i+1][0], res[i+1][1], res[i+1][2] = dots[k].x, dots[k].y, dots[der].derY
			der++
		}
		k++
	}
	return res
}

// InvertInterpolation is func which make InvertInterpolation
func InvertInterpolation(arr ArrDot, n int) (DifTable, float64, error) {
	arr.AxisSwap()
	sort.Sort(arr)
	res, polinom, err := NewtonInterpolation(arr, 0, n)
	if err != nil {
		fmt.Println("error", err)
		return nil, 0, err
	}
	return res, polinom, nil
}

// GetHermitPolinom is func which get polinom of Hermit
func GetHermitPolinom(tb ArrDot, x float64, n int) (DifTable, float64, error) {
	dotsTb, err := GetDots(tb, x, n/2)
	if err != nil {
		panic(err)
	}
	res := HermitTablePreFill(n, dotsTb)
	polinom, xOfPolinom := dotsTb[0].y, 1.0
	for i := 2; i < n+2; i++ {
		for j := 0; j < len(res)-i+1; j++ {
			if res[j][0]-res[j+i-1][0] != 0 {
				res[j][i] = (res[j][i-1] - res[j+1][i-1]) / (res[j][0] - res[j+i-1][0])
			}
			if j == 0 {
				xOfPolinom *= (x - res[i-2][0])
				polinom += (xOfPolinom * res[j][i])
			}

		}
	}
	return res, polinom, nil
}

// HermitInterpolation is func which return diff table and polinom of Hermit
func HermitInterpolation(arr ArrDot, x float64, n int) (DifTable, float64, error) {
	tb, polinom, err := GetHermitPolinom(arr, x, n)

	return tb, polinom, err
}
