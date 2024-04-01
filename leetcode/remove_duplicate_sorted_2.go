package main

import "fmt"

func main() {
	r := removeDuplicates([]int{0, 0, 1, 1, 1, 1, 2, 3, 3})
	fmt.Println(r)
}

func removeDuplicates(nums []int) int {
	memo := make(map[int]int)
	i := 0

	for _, n := range nums {
		if memo[n] < 2 {
			memo[n]++
			nums[i] = n
			i++
		}
	}

	return i
}
