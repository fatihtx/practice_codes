class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum_cc = max(candies)
        return_list = list()
        for i in candies:
            if i+extraCandies >= maximum_cc:
                return_list.append(True)
            else:
                return_list.append(False)
        return return_list 
 
sol = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print (sol.kidsWithCandies(candies,extraCandies))
