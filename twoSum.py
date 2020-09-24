class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_n = dict()
        for index,num in enumerate(nums):
            if target-num in dict_n:
                return [dict_n[target-num],index]
            else:
                dict_n[num]=index
