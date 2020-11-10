# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        curr = LLNode(None, node)
        count = 0

        while curr.next:
            count = count + 1
            curr = curr.next

        return count
