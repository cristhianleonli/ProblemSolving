package main

import "fmt"

func main() {
	r := removeElement([]int{2, 2, 2, 1, 3, 0, 4, 2}, 2)
	fmt.Println("result:", r)
}

func removeElement(nums []int, val int) int {
	i := 0
	n := 0
	c := 0

	for n < len(nums) {
		if nums[n] == val {
			c++
		} else {
			nums[i] = nums[n]
			i++
		}
		n++
	}

	return len(nums) - c
}
