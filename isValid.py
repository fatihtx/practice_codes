class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        matching_paranthesis = {'(':')','[':']','{':'}'}
        for b in s:
            if b in  matching_paranthesis.keys():
                stack.append(b)
            else:
                if not stack or b != matching_paranthesis[stack.pop()]:
                    return False
        return not stack
