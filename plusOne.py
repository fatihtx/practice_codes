class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] + carry == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
            else:
                digits[i] += carry
                break
        return digits
