class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        ans = 1
        left = 1
        n = len(nums)
        cost = nums[0]
        target = 0
        while(left < n):
            cost += nums[left]
            if nums[target]*(left-target+1) - cost <= k:
                ans += 1
            else:
                cost -= nums[target]
                target += 1
            left += 1
        return ans
        