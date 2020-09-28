class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        needle_len = len(needle)
        for i in range(len(haystack)):
            if i+needle_len > len(haystack):
                return -1
            if haystack[i:i+needle_len] == needle:
                return i
        return -1
