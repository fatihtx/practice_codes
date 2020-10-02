class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_lenght = 1
        start = 0
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                flag = True
                for k in range((j - i + 1)//2):
                    if s[i+k] != s[j-k]:
                        flag = False
                if flag and (j - i + 1 > max_lenght):
                    start = i
                    max_lenght = j - i + 1
                    
        return s[start:start+max_lenght]
