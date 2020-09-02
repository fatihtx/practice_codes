class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        return_l = list()
        for c in S:
            if c == '(' and count > 0: return_l.append(c) 
            if c == ')' and count > 1: return_l.append(c) 
            count += 1 if c== '(' else -1
        return ('').join(i for i in return_l)
