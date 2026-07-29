# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        fake = ListNode()
        dummy = fake
        

        if not lists:
            return None

        interval = 1
        
        while interval < len(lists):
            for i in range(0, len(lists)- interval, 2 * interval):
                left = lists[i]
                right = lists[i+interval]
                lists[i] = self.mergeTwoLists(left,right)
            interval *= 2
        
        return lists[0]
        



    def mergeTwoLists(self,one:Optional[ListNode], two: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode()
        dummy = fake

        while one and two:
            if one.val <= two.val:
                dummy.next = one
                one = one.next
            else:
                dummy.next = two
                two = two.next
            dummy = dummy.next

        dummy.next = one if one else two
        
        return fake.next


                    
                    


        

        # length = len(lists)
        # another = ListNode()

        # if length == 0:
        #     dummy = another
        #     return None
        # if length == 1:
        #     return lists[0]

        # x = 0
        # head = lists[0]
        # dummy = another
        # front = another

        # while x + 1 < length:
        #     temp = lists[x+1]

        #     while head and temp:

        #         if head.val <= temp.val:
        #             dummy.next = head
        #             head = head.next
                    
        #         else:
        #             dummy.next = temp
        #             temp = temp.next
        #         dummy = dummy.next
            
        #     if head:
        #         dummy.next = head
        #     else:
        #         dummy.next = temp
            
        #     x +=1
        #     head = front.next
        #     dummy = front
        
        # return another.next

            

        