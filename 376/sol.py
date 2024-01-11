class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while(i < n - 1 and nums[i] == nums[i+1]):
            i += 1
        if i == n - 1:
            return 1
        bigger = nums[i+1] > nums[i]
        ans = 2
        i += 2
        while(i < n):
            if (bigger and nums[i] < nums[i-1]) or (not bigger and nums[i] > nums[i-1]):
                bigger = not bigger
                ans += 1
            i += 1
        return ans