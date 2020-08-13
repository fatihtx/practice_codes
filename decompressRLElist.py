class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        returnl = list()
        for freq,val in zip(nums[::2],nums[1::2]):
            fl = [val]*freq
            returnl = returnl + fl
        return returnl
