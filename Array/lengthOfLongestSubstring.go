func lengthOfLongestSubstring(s string) int {
    if len(s) <= 1 {
        return len(s)
    }

    start := 0
    longest := 0
    charToIndex := map[rune]int{}

    for i, c := range s {
        charIndex, exist := charToIndex[c]

        if exist && charIndex >= start {
            longest = max(longest, i - charIndex)
            start = charIndex + 1
        }

        charToIndex[c] = i
    }

    return longest
}
