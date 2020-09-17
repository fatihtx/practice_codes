class Solution:
    def sumZero(self, n: int) -> List[int]:
        list_n = list()
        if n%2 != 0:
            list_n.append(0) 
        for i in range(1,n//2+1):
            list_n.append(i)
            list_n.append(-i)
        return list_n  
