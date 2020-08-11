class Solution:
    def runningSum(self, nums):
        return_list=list()
        for i in range(len(nums)):
            sumx = 0
            for k in range(i+1):
                sumx = sumx + nums[k]
            return_list.append(sumx)
        return return_list
        
        
        

sol = Solution()
nums = [1,2,3,4] 
print (sol.runningSum(nums))
