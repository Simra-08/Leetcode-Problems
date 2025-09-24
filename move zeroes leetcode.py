# Leetcode Problem : Move Zeroes
# Description : To move all the zeroes in a sorted array to the last

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        for j in range (1,len(nums)):
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1