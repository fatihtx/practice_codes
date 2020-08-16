class Solution:
    def balancedStringSplit(self, s: str) -> int:
        list_s = list(s)
        count_l = 0
        count_r = 0
        return_count = 0
        for i in list_s:
            if i == "L":
                count_l += 1
            if i == "R":
                count_r += 1
            if count_l == count_r and count_l != 0:
                return_count += 1
                count_r =0
                count_l =0
        return return_count

    '''
    def balancedStringSplit(self, s: str) -> int:
    res = cnt = 0         
    for c in s:
        cnt += 1 if c == 'L' else -1            
        if cnt == 0:
            res += 1
    return res  
    '''
