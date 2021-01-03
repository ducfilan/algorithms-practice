# You are given an array of 1s and 0s. And you are given an integer M, which signifies the number of flips allowed.
# Find the position of zeros which when flipped will produce maximum continuous series of 1s.
# For this problem, return the indices of the maximum continuous series of 1s in order.
# 
# Test Case 1:
# * 		Input: Array = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1], M = 1 
# * 		
# * 		Output: [0, 1, 2, 3, 4]  
# * 		
# Explanation:
# Flip index 2 zero to one
# Test Case 2:
# * 		Input: Array = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1], M = 2 
# * 		
# * 		Output: [3, 4, 5, 6, 7, 8, 9]  
# * 		
# Explanation:
# Flip index 5 and 6 zero’s to one


def max_consecutive_ones(A, M):
    n = len(A)

    left, right = 0, 0
    zero_count = 0

    max_ones_size = 0
    max_left, max_right = 0, 0

    while right < n:
        if zero_count <= M:
            if A[right] == 0:
                zero_count += 1
            right += 1

        if zero_count > M:
            if A[left] == 0:
                zero_count -= 1
            left += 1

        current_substring_size = right - left
        if current_substring_size > max_ones_size and zero_count <= M:
            max_ones_size = current_substring_size
            max_left = left
            max_right = right

    return list(range(max_left, max_right))

print(max_consecutive_ones([1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1], 2))
print(max_consecutive_ones([1, 1, 0, 1, 1, 0, 0, 1, 1, 1], 1))
print(max_consecutive_ones([1, 1, 0, 1, 1, 0, 0, 1, 1, 1], 2))