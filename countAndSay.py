class Solution:
    def sequence_finder (self, in_array: str) -> str:
        in_array = list(in_array)
        ret_list = list()
        for i,v in enumerate(reversed(in_array)):
            if i == 0:
                prev = v
                count = 1
            else:
                if v != prev:
                    ret_list.append(prev)
                    ret_list.append(str(count))
                    prev  = v
                    count = 1
                else:
                    count += 1
                
            if len(in_array) == i+1:
                ret_list.append(prev)
                ret_list.append(str(count))
                
        ret_list.reverse()
        return(''.join(ret_list))
    
    def countAndSay(self, n: int) -> str:
        for i in range(n-1):
            if i == 0:
                seq = "1"
            seq = self.sequence_finder(seq)
        return seq if n != 1 else "1" 
