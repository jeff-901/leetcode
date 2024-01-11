class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        mask = 0
        ans = 0
        for end in range(len(nums)):
            while nums[end] & mask:
                mask ^= nums[start]
                start += 1
            # print(start, end)
            mask ^= nums[end]
            ans = max(ans, end - start + 1)
        return ans