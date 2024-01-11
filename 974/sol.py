class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = {0: 1}
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            if prefix_sum in h:
                ans += h[prefix_sum]
                h[prefix_sum] += 1
            else:
                h[prefix_sum] = 1
        return ans