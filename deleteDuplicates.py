# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp_ptr = head
        if tmp_ptr is None:
            return
        while tmp_ptr.next:
            if tmp_ptr.val == tmp_ptr.next.val:
                new = tmp_ptr.next.next
                #tmp_ptr.next = None
                tmp_ptr.next = new
            else:
                tmp_ptr = tmp_ptr.next
        return head
                
