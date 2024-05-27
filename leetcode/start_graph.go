package main

import "fmt"

func main() {
	result := findCenter([][]int{{1, 2}, {2, 3}, {4, 2}})
	fmt.Println(result)
}

func findCenter(edges [][]int) int {
	counter := make(map[int]int)

	for _, l := range edges {
		if _, ok := counter[l[0]]; ok {
			counter[l[0]] += 1
		} else {
			counter[l[0]] = 0
		}

		if _, ok := counter[l[1]]; ok {
			counter[l[1]] += 1
		} else {
			counter[l[1]] = 0
		}
	}

	fmt.Println(counter)
	for k, v := range counter {
		if v == len(edges)-1 {
			return k
		}
	}

	return -1
}
