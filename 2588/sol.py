class Solution(object):
    def beautifulSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = {0: 1}
        ans = 0
        total = 0
        for num in nums:
            total ^= num
            if total in cnt:
                ans += cnt[total]
                cnt[total] += 1
            else:
                cnt[total] = 1
        return ans