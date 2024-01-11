class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        cnt = [1, 0]
        total = 0
        for num in arr:
            total ^= (num & 1)
            ans += cnt[total ^ 1]
            cnt[total] += 1
        return ans % (10**9+7)