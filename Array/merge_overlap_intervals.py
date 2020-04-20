# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
# Assumption: all intervals are sorted by increasing and start of the interval is less than the end of the interval.


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def __init__(self, intervals):
        self.intervals = list(map(
            lambda interval: Interval(interval[0], interval[1]),
            intervals
        ))

    def merge_overlap_interval(self):
        if len(self.intervals) <= 1:
            return self.intervals

        self.intervals.sort(key=lambda interval: interval.start)

        start = self.intervals[0].start
        end = self.intervals[0].end

        merged_intervals = []

        for i in range(1, len(self.intervals)):
            next_interval = self.intervals[i]

            if next_interval.start <= end:
                end = max(next_interval.end, end)
            else:
                merged_intervals.append(Interval(start, end))
                start = next_interval.start
                end = next_interval.end

        merged_intervals.append(Interval(start, end))

        return merged_intervals

    def to_list_arrays(self, intervals):
        return list(map(
            lambda interval: [interval.start, interval.end],
            intervals
        ))


s = Solution([[1, 4], [1, 5], [7, 9]])
print(s.to_list_arrays(s.merge_overlap_interval()))
