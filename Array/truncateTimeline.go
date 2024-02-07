package main

import (
	"fmt"
)

// First is the number of consecutive samples (N)
// Second is the duration for each sample (D)
type Tuple struct {
	First  int
	Second int
}

func truncateTimeline(timeline []Tuple, X int) []Tuple {
	var truncated []Tuple

	for _, tuple := range timeline {
		if X > 0 {
			totalDuration := tuple.First * tuple.Second

			if totalDuration > X {
				fullSamples := X / tuple.Second
				remainingTime := X % tuple.Second

				if remainingTime > 0 {
					truncated = append(truncated, Tuple{1, tuple.Second - remainingTime})
					tuple.First -= (fullSamples + 1)
				} else {
					tuple.First -= fullSamples
				}

				if tuple.First > 0 {
					truncated = append(truncated, tuple)
				}

				// Since we've truncated X units, set X to 0
				X = 0
			} else {
				X -= totalDuration
			}
		} else {
			truncated = append(truncated, tuple)
		}
	}

	return truncated
}

func main() {
	testCases := []struct {
		timeline []Tuple
		X        int
	}{
		{[]Tuple{{2, 3}, {4, 5}}, 1},
		{[]Tuple{{2, 3}, {4, 5}}, 2},
		{[]Tuple{{2, 3}, {4, 5}}, 3},
		{[]Tuple{{2, 3}, {4, 5}}, 4},
		{[]Tuple{{2, 3}, {4, 5}}, 5},
		{[]Tuple{{2, 3}, {4, 5}}, 6},
		{[]Tuple{{2, 3}, {4, 5}}, 7},
		{[]Tuple{{2, 3}, {4, 5}}, 26},
	}

	for _, testCase := range testCases {
		fmt.Printf("input: timeline = %v X=%d: ", testCase.timeline, testCase.X)
		fmt.Printf("output: %v\n", truncateTimeline(testCase.timeline, testCase.X))
	}
}
