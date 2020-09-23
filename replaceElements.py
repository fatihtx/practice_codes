class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        value = -1
        out_list = list()
        for i in reversed(arr):
            out_list.append(value)
            if value < i:
                value = i   
        return reversed(out_list)
