class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
### Examples ###

s = Solution()
num = [3,2,2,3]
assert s.removeElement(num, 3) == 2

num = [0,1,2,2,3,0,4,2]