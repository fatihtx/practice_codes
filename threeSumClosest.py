class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        out_t = ''
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            lp = i+1
            rp = len(nums)-1
            #print(f'i = {i}')
            while lp < rp:
                sum_n = nums[i]+nums[lp]+nums[rp]
                #print(f'nums[i]= {nums[i]}, nums[lp]= {nums[lp]}, nums[rp]= {nums[rp]} ')
                #print(f'sum_n= {sum_n}')
                #print(f'out_t= {out_t}')
                #print (lp)
                #print (rp)
                if out_t == '' or abs(sum_n - target) <= abs(out_t - target):
                    out_t = sum_n
                    #while lp < rp and nums[lp] == nums[lp+1]:
                    #    lp += 1
                    #while lp < rp and nums[rp] == nums[rp-1]:
                    #    rp -= 1
                    if sum_n - target > 0:
                        rp -= 1
                    else:
                        lp += 1
                elif sum_n - target > 0 and abs(sum_n - target) > abs(out_t - target):
                    rp -= 1
                else:
                    lp += 1
        return out_t      
