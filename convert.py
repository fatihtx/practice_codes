class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zig_list = list()
        if numRows == 1:
            return s
        for i in range(len(s)):
            m = i % (2*(numRows-1))
            if m <= (numRows-1):
                zig_list.append(m)
            else:
                zig_list.append(2*(numRows-1) - m)
        zip_list = list(zip(s,zig_list)) 
        zip_list.sort(key= lambda x:x[1])
        return(''.join([x[0] for x in zip_list]))  
