class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret_substr = ''
        temp = ''
        for c in s:
            if c not in temp:
                temp += c
                print(temp)
            else:
                if len(temp) > len(ret_substr):
                    ret_substr = temp
                index_c = temp.index(c)
                temp = temp[index_c+1::] + c
        
        if len(temp) > len(ret_substr):
            ret_substr = temp
                
        return len(ret_substr)
