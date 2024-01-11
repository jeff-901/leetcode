class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = sorted(set(nums))
        start = 0
        for end in range(len(nums)):
            if nums[end] - nums[start] > n - 1:
                start += 1
        return  n - (end - start + 1)