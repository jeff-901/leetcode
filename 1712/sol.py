class Solution(object):
    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        lower_cut = 1
        higher_cut = 1
        ans = 0
        for i in range(n-2):
            if nums[i] * 3 > nums[-1]:
                break
            # cut_val in [lower_cut, higher_cut)
            # cut into [0, i], [i+1, cut_val], [cut_val+1, n-1]
            # therefore, cut_val in [i+1, n-2]
            lower_cut = max(lower_cut, i + 1)
            while (lower_cut < n - 1 and nums[lower_cut] - nums[i] < nums[i]):
                lower_cut += 1
            higher_cut = max(higher_cut, lower_cut)
            while(higher_cut < n - 1 and nums[-1] - nums[higher_cut] >= nums[higher_cut] - nums[i]):
                higher_cut += 1
            ans += higher_cut - lower_cut
        return ans % (10**9+7)
            