package palindrome

import (
	"strings"
	"testing"
)

func TestMinCuts(t *testing.T) {
	type testCase struct {
		input    string
		expected int
	}
	for _, c := range []testCase{
		{"ababb", 2},
		{"bbaba", 2},
		{"apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp", 452},
	} {
		actual := minCut(c.input)
		if actual != c.expected {
			t.Logf("expected: %v\nactual: %v", c.expected, actual)
			t.FailNow()
		}
	}
}

func minCut(str string) int {
	sSlice := strings.Split(str, "")

	for i := 0; i < len(sSlice); i++ {

	}

	return 0
}
