class Solution:
    def solve(self, n):
        ans = 0
        while n:
            ans += 1
            n = n & (n << 1)

        return ans
