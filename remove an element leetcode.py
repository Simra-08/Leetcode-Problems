# Leetcode Problem : Remove an element
# Description : To remove a specific element from a list and return the new list and its length

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return(len(nums))
        print(nums)


