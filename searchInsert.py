class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            index_i = min(range(len(nums)), key = lambda i: abs(nums[i]-target))
            if target > nums[index_i]:
                return index_i + 1
            else:
                return index_i 
