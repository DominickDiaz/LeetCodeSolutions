# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        holder = set()
        node = head
        
        if not node or not node.next:
            return False
        
        while node:
            if node not in holder:
                holder.add(node)
            elif node in holder:
                return True
            node = node.next
            
        return False
            