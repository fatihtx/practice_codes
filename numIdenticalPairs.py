class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter=0
        nums.sort()
        i = 0
        for j in range(1,len(nums)):
            if nums[i] == nums[j]:
                counter += j - i 
            else:
                i = j
        return counter
