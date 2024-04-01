package main

import "fmt"

func main() {
	r := removeDuplicates([]int{1, 1, 2})
	fmt.Println("result:", r)
}

func removeDuplicates(nums []int) int {
	i := 0

	fmt.Println(nums)

	for n := 1; n < len(nums); n++ {
		if nums[n] != nums[i] {
			i++
			nums[i] = nums[n]
		}
	}

	fmt.Println(nums)
	return i + 1
}
