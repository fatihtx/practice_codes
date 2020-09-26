# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head_prt = temp_prt = ListNode()
        
        while l1 or l2:
            if l1 and (not l2 or l2.val >= l1.val):
                temp_prt.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp_prt.next = ListNode(l2.val)
                l2 = l2.next
                print(temp_prt)
            temp_prt = temp_prt.next
            
        return head_prt.next
