# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, node, k):
        slow, fast = node, node
        
        # move fast pointer K step ahead of slow pointer
        for i in range(k):
            fast = fast.next
        
        # move fast and slow pointer both until the next of fast pointer is None
        while fast.next:  
            fast = fast.next
            slow = slow.next

        return slow.val
