# Leetcode Problem : Remove the duplicates from a sorted array
# Description : To remove the duplicates using the two pointers method

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      if not nums:
         return 0
       
      i=0
      for j in range (1,len(nums)):
        if nums[i]!=nums[j]:
            i += 1
            nums[i]=nums[j]

      return i+1     

