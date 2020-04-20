# Level: Hard
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if s == "" or k == 0:
            return ""

        distinct_substring = {}

        substring_length = 0
        max_substring_length = 0

        start = 0
        max_start, max_end = 0, 0

        for end, c in enumerate(s):
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

    def _init_key_or_increase_value(self, d, key):
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1

    def get_max_length_substring_size_k(self, s, k):
        if not s or len(s) == 0 or k <= 0:
            return 0

        # Identify the window start and end.
        substring_chars = {}
        start, end = 0, 0

        while True:
            self._init_key_or_increase_value(substring_chars, s[end])
            end += 1

            if len(substring_chars) == k:
                break

        # Init the max and current of substring.
        max_len = current_len = len(substring_chars)

        # Slide the [start, end] window to find the max length of the substring.
        while end < len(s):
            self._init_key_or_increase_value(substring_chars, s[end])

            while len(substring_chars) > k:
                substring_chars[s[start]] -= 1
                if substring_chars[s[start]] == 0:
                    del substring_chars[s[start]]
                start += 1

            current_len = end - start + 1

            max_len = max(max_len, current_len)
            end += 1

        return max_len


s = Solution()

print('pass' if s.get_max_length_substring_size_k('', 2) == 0 else 'fail')
print('pass' if s.get_max_length_substring_size_k('abc', 0) == 0 else 'fail')
print('pass' if s.get_max_length_substring_size_k('abc', 1) == 1 else 'fail')
print('pass' if s.get_max_length_substring_size_k('abcbcaddadaadefg', 2) == 8 else 'fail')
print('---')
print('pass' if s.lengthOfLongestSubstringKDistinct('', 2) == '' else 'fail')
print('pass' if s.lengthOfLongestSubstringKDistinct('abc', 0) == '' else 'fail')
print('pass' if s.lengthOfLongestSubstringKDistinct('abc', 1) == 'a' else 'fail')
print('pass' if s.lengthOfLongestSubstringKDistinct('abcbcaddadaadefg', 2) == 'addadaad' else 'fail')
