package palindrome

import (
	"fmt"
	"strings"
)

const (
	Boundary = '|'
)

func min(values ...int) int {
	if len(values) < 1 {
		panic("expected at least one value")
	}
	a := values[0]
	for _, x := range values[1:] {
		if x < a {
			a = x
		}
	}
	return a
}

func max(values ...int) int {
	if len(values) < 1 {
		panic("expected at least one value")
	}
	a := values[0]
	for _, x := range values[1:] {
		if x > a {
			a = x
		}
	}
	return a
}

func findMax(values ...int) (int, int) {
	if len(values) < 1 {
		panic("expected at least one value")
	}
	pos := 0
	value := values[0]
	for i, x := range values[1:] {
		if x > value {
			value = x
			pos = i + 1
		}
	}
	return pos, value
}

func boundariedString(s string) string {
	t := make([]rune, 2*len(s)+1)

	for i := 0; i < len(t); i++ {
		if i%2 == 0 {
			t[i] = Boundary
			continue
		}
		t[i] = rune(s[i/2])
	}

	t[len(t)-1] = '|'
	return string(t)
}

func ManachersAlgorithm(s string) (int, int) {
	var (
		P   = make([]int, 2*len(s)+1)
		T   = boundariedString(s)
		C   = 0
		R   = -1
		rad int
	)
	// fmt.Printf("S = %v\n", s)
	// fmt.Printf("T = %v\n", T)

	for i := range T {
		if i <= R {
			rad = min(P[2*C-i], R-i)
		} else {
			rad = 0
		}

		for {
			if !((i+rad < len(T)) &&
				(i-rad >= 0) &&
				(T[i-rad] == T[i+rad])) {
				break
			}
			rad++
		}

		P[i] = rad
		if i+rad-1 > R {
			C = i
			R = i + rad - 1
		}
	}

	// log.Printf("P=%+v", P)

	// Extract word
	pos, pDiameter := findMax(P...)

	// log.Printf("pos=%v", pos)
	// log.Printf("pDiameter=%v", pDiameter)
	pRad := pDiameter - 1

	start := (pos - pRad) / 2
	end := (pos + pRad) / 2
	// log.Printf("%s", T[start*2:end*2])
	return start, end
}

func splitStringIntoPalindromeSlice(s string) (result []string) {
	if len(s) <= 1 {
		return strings.Split(s, "")
	}

	start, end := ManachersAlgorithm(s)

	result = append(result, splitStringIntoPalindromeSlice(s[:start])...)
	if x := s[start:end]; x != "" {
		result = append(result, s[start:end])
	}
	result = append(result, splitStringIntoPalindromeSlice(s[end:])...)
	return
}

func minCut_manacher(s string) (cuts int) {
	if len(s) <= 1 {
		return 0
	}
	x := splitStringIntoPalindromeSlice(s)
	// d, _ := json.MarshalIndent(x, "", "\t")
	// fmt.Printf("%s\n", d)
	y := ""
	for i, m := range x {
		if y == m {
			panic(fmt.Sprintf("got consecutive [%s] at position %d", m, i))
		}
		y = m
	}

	return len(splitStringIntoPalindromeSlice(s)) - 1
}
