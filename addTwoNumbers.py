class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret_ptr = temp_ptr = ListNode()
        add_1 = 0
        
        while l1 or l2:
            
            try:
                l1_val = l1.val
            except:
                l1_val = 0
            try:
                l2_val = l2.val
            except:
                l2_val = 0
                
            temp_ptr.next = ListNode((l1_val + l2_val + add_1) % 10)
            if l1_val + l2_val + add_1 >= 10:
                add_1 = 1
            else:
                add_1 = 0
            
            try:
                l1 = l1.next
            except:
                pass
            try:
                l2 = l2.next
            except:
                pass
            
            temp_ptr = temp_ptr.next
        
        if add_1:
            temp_ptr.next = ListNode(1)
            
        return ret_ptr.next 
