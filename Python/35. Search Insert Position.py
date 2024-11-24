class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if len(nums) == 0:
                return 0
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)
