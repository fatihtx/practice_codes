class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        here = sorted(set(nums))
        for i,v in enumerate(here):
            nums[i] = int(v)
        return len(set(nums))
