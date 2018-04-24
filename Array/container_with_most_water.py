# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.


def container_with_most_water(height):
    l, r = 0, len(height) - 1
    prev_height_l, prev_height_r = 0, 0
    
    max_area = 0
    
    while l < r:
        if height[l] > prev_height_l or height[r] > prev_height_r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            
        if height[l] < height[r]:
            prev_height_l = max(prev_height_l, height[l])
            l += 1
        else:
            prev_height_r = max(prev_height_r, height[r])
            r -= 1
            
    return max_area

print('pass' if container_with_most_water([1,1]) == 1 else 'fail')
print('pass' if container_with_most_water([1,1,4,3,1,1,1]) == 6 else 'fail')
print('pass' if container_with_most_water([2,3,4,5,18,17,6]) == 17 else 'fail')
