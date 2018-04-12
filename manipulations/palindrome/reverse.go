package palindrome

// Reverse a string
func Reverse(s string) string {
	size := len(s)
	result := make([]rune, size)
	for i, c := range s {
		result[size-(1+i)] = c
	}
	return string(result)
}
