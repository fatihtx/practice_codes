class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        letter_dict = dict()
        list_of_uniq_char_S = list(set(S))
        list_of_uniq_char_J = list(set(J))
        for i in list_of_uniq_char_J:
            count = count + S.count(i) 
        return count   # sum([1 for i in S if i in J])
