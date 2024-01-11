class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        first, second = 0, 0
        for num in nums[:-1]:
            tmp = first
            first = second
            second = max(first, tmp + num)
        ans = second
        first, second = 0, 0
        for num in nums[1:]:
            tmp = first
            first = second
            second = max(first, tmp + num)
        return max(ans, second)
        
