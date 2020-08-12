class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out_list = list()
        sorted_nums = sorted(nums)
        for i in nums:
            index_list_of_i = sorted_nums.index(i) # all other indexes = [index for index, value in enumerate(sorted_nums) if value == i]
            out_list.append(index_list_of_i)
        return out_list
    
    #return [sorted(nums).index(a) for a in nums]
