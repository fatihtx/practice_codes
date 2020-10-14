class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        total_list = list()
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left_p = i+1
            right_p = len(nums)-1
            while left_p < right_p:
                if nums[i]+nums[left_p]+nums[right_p] == 0:
                    total_list.append([nums[i],nums[left_p],nums[right_p]])
                    while left_p < right_p and nums[left_p] == nums[left_p+1]:
                        left_p += 1
                    while left_p < right_p and nums[right_p] == nums[right_p-1]:
                        right_p -= 1
                    right_p -= 1
                    left_p  += 1
                elif nums[i]+nums[left_p]+nums[right_p] > 0:
                    right_p -= 1
                else:
                    left_p += 1
        
        return total_list
