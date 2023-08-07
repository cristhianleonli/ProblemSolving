package main

import "fmt"

func plusMinus(arr []int32) {
	weightPerElement := float32(1) / float32(len(arr))

	var negatives float32 = 0
	var positives float32 = 0
	var zeros float32 = 0

	for _, number := range arr {
		if number == 0 {
			zeros += weightPerElement
		} else if number > 0 {
			positives += weightPerElement
		} else {
			negatives += weightPerElement
		}
	}

	fmt.Printf("%.6f\n%.6f\n%.6f", positives, negatives, zeros)
}

func main() {
	plusMinus([]int32{-4, 3, -9, 0, 4, 1})
}
