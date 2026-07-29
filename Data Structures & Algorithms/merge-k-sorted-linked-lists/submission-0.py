# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        length = len(lists)
        another = ListNode()

        if length == 0:
            dummy = another
            return None
        # if not lists[0]:
        #     return None
        if length == 1:
            return lists[0]

        x = 0
        head = lists[0]
        dummy = another
        front = another

        while x + 1 < length:
            temp = lists[x+1]

            while head and temp:

                if head.val <= temp.val:
                    dummy.next = head
                    head = head.next
                    
                else:
                    dummy.next = temp
                    temp = temp.next
                dummy = dummy.next
            
            if head:
                dummy.next = head
            else:
                dummy.next = temp
            
            x +=1
            head = front.next
            dummy = front
        
        return another.next

            

        