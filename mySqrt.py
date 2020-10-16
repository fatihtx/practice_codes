class Solution:
    def mySqrt(self, x: int) -> int:
        iteration = 100
        a = float(x)
        if x == 0:
            return 0
        for i in range(iteration):
            mid_x = x
            x = (x + a/x)/2
            int_mid_x = mid_x // 1
            int_x = x // 1
            if int(int_x) == int(mid_x):
                return int(int_x)
