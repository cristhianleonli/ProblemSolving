package main

import "fmt"

func main() {
	// r := majorityElement([]int{2, 2, 1, 1, 1, 2, 2})
	r := majorityElement([]int{3, 2, 3})
	fmt.Println(r)
}

func majorityElement(nums []int) int {
	memo := make(map[int]int)
	greatest := -1
	greatest_count := -1

	for _, n := range nums {
		memo[n]++

		if memo[n] > greatest_count {
			greatest = n
			greatest_count = memo[n]
		}
	}

	return greatest
}
