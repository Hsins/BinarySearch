# No.                 : 0297
# Name                : List Calculator
# Difficulty          : Easy
# Author              : Hsins <hsinspeng@gmail.com>
# Time Complexity     : O(n)
# Space Complexity    : O(1)

# [SOLUTION]
class Solution:
    @staticmethod
    def solve(nums, op, val):
        return {
          '+': [num + val for num in nums],
          '-': [num - val for num in nums],
          '*': [num * val for num in nums],
          '/': [num // val for num in nums]
        }.get(op)

# [TESTING]
import pytest


test_cases = [
    ([3, 1, 6], "+", 4, [7, 5, 10]),
    ([3, -4, 1], "*", 2, [6, -8, 2]),
]

@pytest.mark.parametrize("nums, op, val, expected", test_cases)
def test_solution(nums, op, val, expected):
    assert Solution().solve(nums, op, val) == expected
