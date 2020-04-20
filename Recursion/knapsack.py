# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a capacity ‘C’.
# The goal is to get the maximum profit out of the items in the knapsack.
# Each item can only be selected once, as we don’t have multiple quantities of any item.


class KnapsackOptimizer:
    def __init__(self, weights, profits, capacity):
        self.weights = weights
        self.profits = profits
        self.capacity = capacity
        self.cache = [[-1 for x in range(capacity+1)] for y in range(len(profits))]

    def _find_max_profit_from_index(self, capacity_left, current_index):
        if capacity_left <= 0 or current_index >= len(self.weights):
            return 0

        if self.cache[current_index][capacity_left] != -1:
            return self.cache[current_index][capacity_left]

        # Take the item.
        profit_1 = 0
        if self.weights[current_index] <= capacity_left:
            profit_1 = self.profits[current_index] + \
                self._find_max_profit_from_index(capacity_left - self.weights[current_index], current_index+1)

        # Not take the item.
        profit_2 = self._find_max_profit_from_index(capacity_left, current_index+1)

        # Take what's having better profit.
        self.cache[current_index][capacity_left] = max(profit_1, profit_2)
        return max(profit_1, profit_2)

    def find_max_profit(self):
        return self._find_max_profit_from_index(self.capacity, 0)


knapsack_optimizer = KnapsackOptimizer([2, 3, 1, 4], [4, 5, 3, 7], 5)
print(knapsack_optimizer.find_max_profit())
