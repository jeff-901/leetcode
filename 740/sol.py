class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = max(nums)
        cnt = [0 for _ in range(max_val + 1)]
        for num in nums:
            cnt[num] += 1
        for i in range(2, max_val + 1):
            cnt[i] = max(cnt[i-1], cnt[i-2] + cnt[i] * i)
        return cnt[-1]