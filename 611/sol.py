class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > num:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans