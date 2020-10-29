class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = 0
        for i,v in enumerate(nums1):
            if k == n:
                break
            if v > nums2[k]:
                #print(i)
                nums1.insert(i,nums2[k])
                nums1.pop(len(nums1)-1)
                k += 1
            elif (i>0 and nums1[i-1] > nums1[i]) or m == 0 or i>=m+k:
                #print(i)
                nums1[i] = nums2[k]
                k += 1
            #print(nums1)
