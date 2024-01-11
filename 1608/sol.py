class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        right = len(nums)
        while(left <= right):
            mid = (left + right) // 2
            count = 0
            for ele in nums:
                if ele >= mid:
                    count += 1
            if mid == count:
                return mid
            elif mid < count:
                left = mid + 1
            else:
                right = mid - 1
        return -1