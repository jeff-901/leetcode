class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while(left <= right):
            mid = (left + right) // 2
            cnt = 0
            i = 0
            for j, num in enumerate(nums):
                while(num - nums[i] > mid):
                    i += 1
                cnt += j - i
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1
        return left
            