class Solution(object):
    def countTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        j = 0
        n = len(nums)
        cnt = {}
        for i in range(n):
            for j in range(n):
                val = nums[i] & nums[j]
                cnt[val] = cnt.get(val, 0) + 1
        for i in range(n):
            for val in cnt:
                if nums[i] & val == 0:
                    ans += cnt[val]
        return ans
