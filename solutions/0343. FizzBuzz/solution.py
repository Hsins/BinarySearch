class Solution:
    def solve(self, n):
        result = []
        for num in range(1, n + 1):
            # check and concatenate "Fizz" and "Buzz"
            word = "Fizz" if num % 3 == 0 else ""
            word += "Buzz" if num % 5 == 0 else ""

            # append the word if not empty or the string of number
            result.append(word or f'{num}')
        return result
