'''
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, 
i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.

Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

def fruit_in_basket(fruits):
    n = len(fruits)

    left, right = 0, 0
    max_fruits = 0

    basket_count = 2
    fruits_in_basket = set()

    while right < n:
        if not fruits[right] in fruits_in_basket:
            fruits_in_basket.add(fruits[right])

        if len(fruits_in_basket) <= basket_count:
            right += 1
        else:
            fruits_in_basket.remove(fruits[left])
            left += 1

        current_fruit_count = right - left
        if current_fruit_count > max_fruits:
            max_fruits = current_fruit_count

    return max_fruits

print(fruit_in_basket([]))
print(fruit_in_basket(['A', 'B', 'C', 'A', 'C']))
print(fruit_in_basket(['A', 'B', 'C', 'B', 'B', 'C']))