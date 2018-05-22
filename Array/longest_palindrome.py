# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# 
# Example 1:
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# 
# Input: "cbbd"
# Output: "bb"


 def longest_palindrome(s):
    start, end = 0, 0
    n = len(s)
    
    for i in range(n):
        
        length_1 = expand_from_center(s, i, i, n)
        length_2 = expand_from_center(s, i, i + 1, n)
        
        length = max(length_1, length_2)
        
        if length > end - start:
            start = i - (length - 1) // 2
            end   = i + length // 2
            
    return s[start:end + 1]

def expand_from_center(s, l, r, n):
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
        
    return r - l - 1
