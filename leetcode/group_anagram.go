package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	items := []string{"cat", "tac", "bat", "tab"}
	result := groupAnagrams(items)
	fmt.Println(result)
}

func groupAnagrams(strs []string) [][]string {
	m := map[string][]string{}

	for _, word := range strs {
		f := key(word)
		p, ok := m[f]

		if ok {
			p = append(p, word)
			m[f] = p
		} else {
			m[f] = []string{word}
		}
	}

	r := [][]string{}
	for _, v := range m {
		r = append(r, v)
	}

	return r
}

func key(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}

func key2() {}
