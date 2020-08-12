class Solution:
    def numberOfSteps (self, num: int) -> int:
        count =0
        while num>0:
            if num%2 == 0:
                num=num/2
                count +=1
            else:
                num=num-1
                count+=1
        return count # while n != 0: n, c = n - 1 if n % 2 else n//2, c + 1
