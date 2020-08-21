class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        
        maxAreaS = 0
        
        while (left < right):
            print(f"left_index {left} left_value {height[left]}")
            print(f"right_index {right} right_value {height[right]}")
            calculated_area =(right-left) * min(height[left],height[right])
            print(f"calculated_area {calculated_area}")
            maxAreaS = max(maxAreaS,calculated_area)
            print(f"maxAreaS {maxAreaS}")
            
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                #print(left)
                #left += 1
                if(height[left+1] > height[left]):
                    left += 1
                else:
                    right -= 1 
                    
        return maxAreaS
