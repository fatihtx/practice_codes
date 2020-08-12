class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        list_s = list(s) 
        merged_list = [(indices[i], list_s[i]) for i in range(0, len(list_s))]
        merged_list.sort()
        out = list(zip(*merged_list))
        return ''.join(out[1])
