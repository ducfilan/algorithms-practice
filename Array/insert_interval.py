class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def insert(intervals, new_interval):
    merged = []

    if not intervals or len(intervals) == 0:
        return new_interval

    intervals = [Interval(i[0], i[1]) for i in intervals]
    intervals.append(Interval(new_interval[0], new_interval[1]))

    intervals.sort(key=lambda interval: interval.start)

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        next_interval = intervals[i]

        if next_interval.start <= end:
            end = max(end, next_interval.end)
        else:
            merged.append([start, end])

            start = next_interval.start
            end = next_interval.end

    merged.append([start, end])

    return merged


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
