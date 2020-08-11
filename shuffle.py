class Solution:
    def shuffle(self, nums, n):
        return_list = list()
        for i in range(n):
            return_list.append(nums[i])
            return_list.append(nums[n+i])
        return return_list
        
sol = Solution()
nums = [2,3,5,1,3]
n = 3
print (sol.shuffle(nums,n))
