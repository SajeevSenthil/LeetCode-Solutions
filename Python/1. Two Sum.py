class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] + nums[i]  == target:
                    nums[0] = i
                    nums[1] = j
        return nums[0:2]
