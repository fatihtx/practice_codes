class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_lenght = 1
        start = 0
        
        p_table = [[0 for x in range(len(s))] for x in range(len(s))]
        
        mlenght = 1
        start = 0
        #for itself l=1
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    p_table[i][j] = True
        
        # calculate l=2
        l=2
        for i in range(len(s)-1):
            j = i + l - 1
            if s[i] == s[j]:
                p_table[i][j] = True
                mlenght = 2
                start = i
        
        l=3
        while l <= len(s):
            for i in range(len(s) - l + 1):
                j = i + l - 1
                if s[i] == s[j] and p_table[i+1][j-1] == True:
                    p_table[i][j] = True
                    if mlenght < l:
                        mlenght = l
                        start = i
            l += 1
   
        return s[start:start+mlenght]
