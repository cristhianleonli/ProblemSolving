package main

import "fmt"

func main() {
	rotate([]int{1, 2, 3, 4, 5, 6, 7}, 3)
}

func rotate(nums []int, k int) {
	x, b := (nums)[:(len(nums)-k)], (nums)[(len(nums)-k):]
	nums = append(b, x...)
	fmt.Println(nums)
}
