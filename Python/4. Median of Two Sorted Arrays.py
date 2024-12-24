from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        C = []
        n = len(nums1)
        m = len(nums2)
        for i in range(n):
            C.append(nums1[i])
        for j in range(m):
            C.append(nums2[j])
        C.sort()
        if len(C) % 2 == 0:
            median = (C[len(C)//2] + C[len(C)//2 - 1])/2
        else:
            pos = (len(C) - 1)//2
            median = C[pos]
        return median
