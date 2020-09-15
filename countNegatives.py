class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for row in range(m):
            all_neg = False
            for column in range(n):
                if grid[row][column] >= 0:
                    count += 1
                else:
                    if grid[row][0] < 0:
                        all_neg = True
                    break
            if all_neg:
                break
                
        return m*n - count
