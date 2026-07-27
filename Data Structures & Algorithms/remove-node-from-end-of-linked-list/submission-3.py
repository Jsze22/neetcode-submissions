# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head
        slow = head
        counter = 0
        prev = None

        while counter < n:
            fast = fast.next
            counter +=1
        if not fast:
            return head.next
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        prev.next = slow.next
        
        return head


            

        
        