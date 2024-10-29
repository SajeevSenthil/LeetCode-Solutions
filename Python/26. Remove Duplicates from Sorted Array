class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()
        index = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        del nums[index+1:]
        return len(nums)
