class Solution:
    def makeGood(self, s: str) -> str:
        s_list = list(s)
        length_first_s = len(s_list)
        length_next_s = 0
        while length_next_s != length_first_s:
            length_first_s = len(s_list)
            lower_s_list = list(map(lambda x:x.lower(),s_list))
            for i in range (len(s_list)-1):
                if lower_s_list[i] == lower_s_list[i+1] and s_list[i] != s_list[i+1]:
                    del s_list[i:i+2]
                    break
            length_next_s = len(s_list)
        returned_s = ''.join(s_list)
        return returned_s

mg = Solution
print mg.makeGood('aBbACc')
