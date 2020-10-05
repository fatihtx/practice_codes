class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub_palindrome = ''
        
        for i in range(len(s)):
            for j in range(len(s),i,-1):
                if len(sub_palindrome) > j - i:
                    break
                elif s[i:j] == s[i:j][::-1]:
                    sub_palindrome = s[i:j]
                    break
  
        return sub_palindrome
