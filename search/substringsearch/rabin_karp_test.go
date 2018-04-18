package substringsearch

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestRabinKarpSearch(t *testing.T) {
	test := func(text, pattern string, expectedPositions ...int) {
		t.Run(text+"_"+pattern, func(tt *testing.T) {
			require.Equal(tt, expectedPositions, RabinKarpSearch([]byte(text), []byte(pattern)))
		})
	}

	test("ababac", "ba", 1, 3)
	test("aaaaaabaaaabababaaaaaab", "aaaa", 0, 1, 2, 7, 16, 17, 18)
	test("0101010101", "010", 0, 2, 4, 6)
	test("0101010101", "101", 1, 3, 5, 7)
}
