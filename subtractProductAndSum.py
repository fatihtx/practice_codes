class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list_n = [int(x) for x in str(n)]
        result_m = math.prod(list_n)
        result_s = sum(list_n)
        return result_m - result_s
        
 '''
s = lambda n: n if n < 10 else n % 10 + s(n//10)
p = lambda n: n if n < 10 else (n%10) * p(n//10) 

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return p(n) - s(n)
 '''
