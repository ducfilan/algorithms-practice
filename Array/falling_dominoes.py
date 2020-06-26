# Hi, here's your problem today. This problem was recently asked by Twitter:
#
# Given a string with the initial condition of dominoes, where:
#
# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side
#
# Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.
#
# Example:
# Input:  ..R...L..R.
# Output: ..RR.LL..RR
# Here is your starting point:
#
# class Solution(object):
#   def pushDominoes(self, dominoes):
#     # Fill this in.
#
# print Solution().pushDominoes('..R...L..R.')
# # ..RR.LL..RR


class Solution(object):
    def _change_state(self, current_state, falling_positions):
        next_falling_positions = set()

        for position in falling_positions:
            current_position_state = current_state[position]

            is_current_position_balanced = len(current_state) >= 3 and \
                ((
                    position >= 2 and
                    current_position_state == 'L' and
                    current_state[position - 1] == '.' and
                    current_state[position - 2] == 'R' and
                    (position - 2) not in next_falling_positions
                ) or
                    (
                    position <= len(current_state) - 3 and
                    current_position_state == 'R' and
                    current_state[position + 1] == '.' and
                    current_state[position + 2] == 'L'
                ))

            if is_current_position_balanced:
                continue
            elif current_position_state == 'L' and position > 0 and current_state[position - 1] == '.':
                current_state[position - 1] = 'L'
                next_falling_positions.add(position - 1)
            elif current_position_state == 'R' and position < (len(current_state) - 1) and current_state[position + 1] == '.':
                current_state[position + 1] = 'R'
                next_falling_positions.add(position + 1)

        if not next_falling_positions:
            return current_state

        return self._change_state(current_state, next_falling_positions)

    def pushDominoes(self, dominoes):
        falling_positions = [i for i, domino in enumerate(dominoes) if domino == 'L' or domino == 'R']

        return ''.join(self._change_state(list(dominoes), falling_positions))


print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR

print(Solution().pushDominoes(''))
print(Solution().pushDominoes('L'))
print(Solution().pushDominoes('LL'))
print(Solution().pushDominoes('R.L'))
print(Solution().pushDominoes('R..L'))