class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if s == "" or k == 0:
            return ""

        distinct_substring = {}

        substring_length = 0
        max_substring_length = 0

        start, end = 0, 0
        max_start, max_end = 0, 0

        for i, c in enumerate(s):
            end = i
            substring_length += 1

            if c not in distinct_substring:
                distinct_substring[c] = 1
            else:
                distinct_substring[c] += 1

            if len(distinct_substring) > k:
                if distinct_substring[s[start]] > 1:
                    distinct_substring[s[start]] -= 1
                else:
                    del distinct_substring[s[start]]
                start += 1
                substring_length -= 1

            if substring_length > max_substring_length:
                max_substring_length = substring_length
                max_start = start
                max_end = end

        return s[max_start:max_end + 1]


s = Solution()
print(s.lengthOfLongestSubstringKDistinct('abcbcaddadaadefg', 2))
