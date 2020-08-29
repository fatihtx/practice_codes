class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        list_gt = list()
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if abs(arr[i]-arr[j]) <= a and  abs(arr[j]-arr[k]) <= b and  abs(arr[i]-arr[k]) <= c:
                        good_t = (arr[i],arr[j],arr[k])
                        list_gt.append(good_t)
        
        return len(list_gt)
