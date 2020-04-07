# Any number will be called a happy number if, after repeatedly replacing it with a number equal to
# the sum of the square of all of its digits, leads us to number ‘1’.
# All other (not-happy) numbers will never reach ‘1’.
# Instead, they will be stuck in a cycle of numbers which does not include ‘1’.


class HappyNumber:
    def __init__(self, number):
        self.number = number
        self.memo = {}

    def _calculate_digits_sum(self, number, is_memo_needed=False):
        if number in self.memo:
            sum = self.memo[number]
            del self.memo[number]
            
            return sum

        sum = 0

        for digit in str(number):
            sum += int(digit) * int(digit)

        if is_memo_needed:
            self.memo[number] = sum

        return sum

    def check(self):
        slow_pointer, fast_pointer = self.number, self.number

        while True:
            fast_pointer = self._calculate_digits_sum(
                self._calculate_digits_sum(fast_pointer, True),
                True
            )
            slow_pointer = self._calculate_digits_sum(slow_pointer)

            if slow_pointer == fast_pointer:
                break

        return slow_pointer == 1


h = HappyNumber(23)
print(h.check())

h = HappyNumber(12)
print(h.check())

h = HappyNumber(10)
print(h.check())
