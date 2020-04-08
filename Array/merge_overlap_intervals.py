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

        start_pointer = 0
        end_pointer = 1

        while end_pointer < len(self.intervals):
            if self.intervals[start_pointer].end <= self.intervals[end_pointer].start:
                start_pointer += 1
                end_pointer += 1
                continue

            if self.intervals[start_pointer].start <= self.intervals[end_pointer].start and self.intervals[start_pointer].end <= self.intervals[end_pointer].end and self.intervals[start_pointer].end > self.intervals[end_pointer].start:
                self.intervals[1] = Interval(self.intervals[start_pointer].start,
                                             self.intervals[end_pointer].end)
                self.intervals.pop(0)
                continue

            if self.intervals[start_pointer].start <= self.intervals[end_pointer].start and self.intervals[start_pointer].end >= self.intervals[end_pointer].end:
                self.intervals.pop(1)
                continue

        return self.intervals

    def to_list_arrays(self):
        return list(map(
            lambda interval: [interval.start, interval.end],
            self.intervals
        ))


s = Solution([[1, 4], [1, 5], [7, 9]])
s.merge_overlap_interval()
print(s.to_list_arrays())
