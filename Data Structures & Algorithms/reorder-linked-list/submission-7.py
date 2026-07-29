# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        first = head
        second = prev
        
        while second:
            temp_first = first.next
            temp_second = second.next

            first.next = second
            second.next = temp_first

            first = temp_first
            second = temp_second





        