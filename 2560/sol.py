class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = min(nums)
        right = max(nums)
        n = len(nums)
        while(left <= right):
            mid = (left + right) // 2
            cnt = 0
            last = 0
            for i in range(n):
                if last:
                    last = 0
                    continue
                if nums[i] <= mid:
                    last = 1
                    cnt += 1
                    if cnt >= k:
                        break
            if cnt >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left