# Leetcode Problem : Squares of a Sorted Array
# Description : To print out the sqaures of the array and arrange them in a sorted manner

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range (len(nums)):
            nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums
