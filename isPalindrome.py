class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 0:
            return x == 0
        
        nbr_digits = math.floor(math.log10(x))+1
        
        mask_msb = 10**(nbr_digits-1)
        
        for i in range(nbr_digits//2):
            if x % 10 != x // mask_msb:
                return False
            x %= mask_msb
            x //= 10
            mask_msb //= 100
        
        return True
