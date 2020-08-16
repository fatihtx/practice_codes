digit_c = lambda x: 1 if x<10 else 1 + digit_c(x//10)

class Solution:
    def findNumbers(self, nums: List[int]) -> int: 
        lict_r =    list(map(lambda x:len(str(x)),nums))
        list_even = list(filter(lambda x: x%2 == 0 ,lict_r))
        return len(list_even)
