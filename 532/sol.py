class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = {}
        ans = 0
        if k == 0:
            for num in nums:
                cnt[num] = cnt.get(num, 0) + 1
            for val in cnt:
                if cnt[val] > 1:
                    ans += 1
            return ans
        for num in nums:
            if num not in cnt:
                ans += cnt.get(k + num, 0)
                ans += cnt.get(num - k, 0)
                cnt[num] = 1

        return ans