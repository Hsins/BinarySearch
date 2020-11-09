# No.                 : 0016
# Name                : 3-6-9
# Difficulty          : Easy
# Author              : Hsins <hsinspeng@gmail.com>
# Time Complexity     : O(n)
# Space Complexity    : O(1)

# [SOLUTION]
class Solution:
    @staticmethod
    def solve(n):
        result = []
        word = "clap"

        for i in range(1, n + 1):
            num = str(i)
            if (i % 3  == 0) or ('3' in num) or ('6' in num) or ('9' in num):
                result.append(word)
            else:
                result.append(num)

        return result

# [TESTING]
import pytest


test_cases = [
    (0, []),
    (-1, []),
    (16, ["1", "2", "clap", "4", "5", "clap", "7", "8", "clap", "10", "11", "clap", "clap", "14", "clap", "clap"]),
]

@pytest.mark.parametrize("n, expected", test_cases)
def test_solution(n, expected):
    assert Solution().solve(n) == expected
