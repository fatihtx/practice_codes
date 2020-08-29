# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number_list = list()
        curr = head
        while curr:
            number_list.append(curr.val)
            curr = curr.next 
        return int("".join(str(i) for i in number_list),2)

 '''
        answer = 0
        while head: 
            answer = 2*answer + head.val 
            head = head.next 
        return answer 
 '''
