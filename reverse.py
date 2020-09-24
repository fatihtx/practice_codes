class Solution:
    def reverse(self, x: int) -> int:
        sign = [-1,1][x>0]
        abs_x = abs(x)
        ret_n = 0
        
        while abs_x:
            abs_x, mod_x = divmod(abs_x, 10)
            ret_n = ret_n*10 + mod_x
            
        return sign*ret_n if ret_n.bit_length() < 32 else 0 
