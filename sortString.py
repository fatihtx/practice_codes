class Solution:
    def sortString(self, s: str) -> str:
        new_s = ''
        list_c = list(s)
        while list_c:
            uniq_e = list(set(list_c))
            len_list = len(uniq_e)
            for i in range(len_list):
                min_element = min(uniq_e)
                uniq_e.remove(min_element)
                list_c.remove(min_element)
                new_s += min_element
            uniq_e = list(set(list_c))
            len_list = len(uniq_e)
            for i in range(len_list):
                max_element = max(uniq_e)
                uniq_e.remove(max_element)
                list_c.remove(max_element)
                new_s += max_element
        return new_s
