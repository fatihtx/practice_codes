class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        flagb = 0
        
        if len(strs)> 1 :
            strso = strs[0]
        else:   
            return prefix if not strs else strs[0]
        
        for i in range(len(strs[0])):
            strsoi = strso[i]
            temp = ""
            for k in range(1,len(strs)):
                strsk  = strs[k]
                temp = ""
                if len(strsk)-1 >= i:
                    temp = strsk[i]
                    if strsoi != temp:
                        flagb = 1
                        temp = ""
                        break
                else:
                    flagb = 1
                    break
            prefix += temp
            if flagb == 1:
                break
        return prefix
