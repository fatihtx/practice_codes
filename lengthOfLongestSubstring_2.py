class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hits = {}
        mx = 0
        start = 0
        
        for i,c in enumerate(s):
            
            if c in hits and hits[c] >= start:
                mx = max(mx,i-start)
                start = hits[c]+1
            hits[c] = i
            
        return max(mx,len(s)-start)
