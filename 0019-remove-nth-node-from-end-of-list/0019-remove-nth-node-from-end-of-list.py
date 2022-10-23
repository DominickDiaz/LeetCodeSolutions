# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        current = dummy.next
        count = 0
        while current != None: 
            count += 1
            current = current.next
        current = dummy.next
       
        if n == count:
            head = head.next;
            return head;
        
        
        counter = 0
        
        while current:
            counter += 1
            if counter == count - n:
                current.next = current.next.next
            current = current.next
            
        return dummy.next
            