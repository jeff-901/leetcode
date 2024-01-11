class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n - 1
        left = 0
        right = n - 1
        while(left < right - 1):
            middle = (right + left) / 2
            if nums[middle] < nums[middle - 1]:
                right = middle
            elif nums[middle] < nums[middle + 1]:
                left = middle
            else:
                return middle
        return right