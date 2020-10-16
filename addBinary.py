class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a,2)
        int_b = int(b,2)
        add_ab = int_a + int_b
        bin_ab = bin(add_ab)
        return(str(bin_ab)[2:])
