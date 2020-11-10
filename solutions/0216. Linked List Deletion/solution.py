# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, target):
        prev = curr = LLNode(None, node)

        while curr.next:
            if curr.next.val == target:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return prev.next
