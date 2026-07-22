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
        self.print_list(first)
        self.print_list(second)
        final = ListNode()
        dummy = final

        while second:
            temp_first = first.next
            dummy.next = first
            first = temp_first
            dummy = dummy.next
            temp_second = second.next
            dummy.next = second
            second = temp_second
            dummy = dummy.next

        if first:
            dummy.next = first
    
    def print_list(self, head):
        curr = head

        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next

        print("None")





        