# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def solve(self, root):
        prev = curr = LLNode(0, None)

        # keep a queue to store current node of tree
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            curr.next = LLNode(node.val)
            curr = curr.next

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return prev.next
