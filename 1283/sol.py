class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left = 1
        right = max(nums)
        while(left <= right):
            mid = (left + right) // 2
            s = 0
            for num in nums:
                s += (num + mid - 1) // mid
            if s <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        return left