class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                if i == n - 1:
                    return True
                if i < 2 or nums[i] > nums[i-2]:
                    for j in range(i+1, n):
                        if nums[j] <= nums[j-1]:
                            return False
                    return True
                if nums[i+1] <= nums[i-1]:
                    return False
                for j in range(i+2, len(nums)):
                    if nums[j] <= nums[j-1]:
                        return False
                return True
        return True
