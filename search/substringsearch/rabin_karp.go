package substringsearch

import "log"

// RabinKarpSearch returns the indices of text where pattern exists.
// This function returns an empty []int if len(pattern) > len(text)
func RabinKarpSearch(text, pattern []byte) (positions []int) {
	windowSize := len(pattern)
	if windowSize > len(text) {
		return
	}

	// initial sum
	p := sum(pattern)
	h := sum(text[:windowSize])

	// check first window
	if h == p {
		if naiveEquality(text[:windowSize], pattern) {
			positions = append(positions, 0)
		}
	}

	// loop through all incoming bytes after first window
	for i, in := range text[windowSize:] {
		out := text[i]
		h -= int(out)
		h += int(in)

		log.Printf("comparing [%s] with [%s] --> %d", text[i+1:i+1+windowSize], pattern, i+1)

		// check window
		if h == p {
			if naiveEquality(text[i+1:i+1+windowSize], pattern) {
				positions = append(positions, i+1)
			}
		}
	}

	return positions
}

func sum(data []byte) (s int) {
	for _, d := range data {
		s += int(d)
	}
	return
}

func naiveEquality(A, B []byte) bool {
	for i, a := range A {
		if B[i] != a {
			return false
		}
	}
	return true
}
