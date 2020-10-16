class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_split = s.split()
        return len(s_split[-1]) if s_split else 0
