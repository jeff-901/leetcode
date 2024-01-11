class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        cnt = {n: 1}
        i = 0
        total = n
        ans = 0
        while(nums[i] != k):
            if nums[i] < k:
                total -= 1
            else:
                total += 1
            if total in cnt:
                cnt[total] += 1
            else:
                cnt[total] = 1
            i += 1
        i += 1
        ans += cnt.get(total, 0) + cnt.get(total-1, 0)
        while(i < n):
            if nums[i] < k:
                total -= 1
            else:
                total += 1
            ans += cnt.get(total, 0) + cnt.get(total-1, 0)
            i += 1
        return ans
