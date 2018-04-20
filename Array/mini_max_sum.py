# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#
# Input Format
#
# A single line of five space-separated integers.


def mini_max_sum(arr):
  min_num = min(arr)
  max_num = max(arr)
  sum_all = sum(arr)
  
  return (sum_all - max_num, sum_all - min_num)
