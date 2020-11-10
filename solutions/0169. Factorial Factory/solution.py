# No.                 : 0169
# Name                : Factorial Factory
# Difficulty          : Easy
# Author              : Hsins <hsinspeng@gmail.com>
# Time Complexity     : O(n)
# Space Complexity    : O(1)

# [SOLUTION]
class Solution:
    @staticmethod
    def solve(n):
        # boundary condition
        if n <= 0:
            return 1

        # calculate factorial
        for i in range(1, n):
            n *= i

        return n

# [TESTING]
import pytest


test_cases = [
    (0, 1),
    (5, 120),
]

@pytest.mark.parametrize("n, expected", test_cases)
def test_solution(n, expected):
    assert Solution().solve(n) == expected
