import "sort"

type Interval struct {
    Start int
    End   int
}

func merge(intervals [][]int) [][]int {
    if len(intervals) == 0 {
        return nil
    }

    // Convert to slice of Interval for easier sorting
    intervalsI := make([]Interval, len(intervals))
    for i, interval := range intervals {
        intervalsI[i] = Interval{interval[0], interval[1]}
    }

    // Sort by start time
    sort.Slice(intervalsI, func(i, j int) bool {
        return intervalsI[i].Start < intervalsI[j].Start
    })

    result := make([][]int, 0)
    current := intervalsI[0]

    for i := 1; i < len(intervalsI); i++ {
        if current.End >= intervalsI[i].Start {
            // Merge intervals
            if current.End < intervalsI[i].End {
                current.End = intervalsI[i].End
            }
        } else {
            // Add current interval to result and move to next
            result = append(result, []int{current.Start, current.End})
            current = intervalsI[i]
        }
    }

    // Add the last interval
    result = append(result, []int{current.Start, current.End})

    return result
}
