class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = list()
        for k,i in enumerate(index):
            target.insert(i,nums[k])
        return target
