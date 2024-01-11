class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        prefix = 0
        vis = {0}
        ans = 0
        for j in range(len(nums)):
            prefix += nums[j]
            if prefix - target in vis:
                ans += 1
                prefix = nums[j]
                vis = {nums[j]}
            else:
                vis.add(prefix)
        return ans
