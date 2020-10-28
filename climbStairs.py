class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        if n == 4:
            return 5
        if n > 2:
            return self.climbStairs(n-4) + 2* self.climbStairs(n-3) + self.climbStairs(n-2)
