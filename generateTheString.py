class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2 == 0:
            list_a = (n-1)*['a']
            list_a.append('b')
        else:
            list_a = n*['a']
        return ''.join(list_a)
