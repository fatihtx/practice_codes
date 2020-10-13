class Solution:
    def twoSum (self, nums_list, target):
        out_list = list()
        target_dict = dict()
        for num in nums_list:
            if target - num in target_dict:
                out_list.append(sorted([-target,num,target-num]))
            else:
                target_dict[num] = 1
        return out_list
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        total_list = list()
        uniq_list = list(set(nums))
        for target in uniq_list:
            nums_list_t = nums[:]
            nums_list_t.remove(target)
            out_list = self.twoSum(nums_list_t,-target)
            if out_list:
                for list_in_o in out_list:
                    if list_in_o not in total_list:
                        total_list.append(list_in_o)
        return total_list
