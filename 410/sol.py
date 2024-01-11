class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = max(nums)
        right = sum(nums)
        while(left <= right):
            mid = (left + right) // 2
            cnt = 0
            s = 0
            for num in nums:
                if s + num > mid:
                    cnt += 1
                    s = num
                else:
                    s += num
            cnt += 1
            if cnt <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left