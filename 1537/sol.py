class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        a_max = 0
        b_max = 0
        while(left < len(nums1) and right < len(nums2)):
            a = nums1[left]
            b = nums2[right]
            if a < b:
                a_max += a
                left += 1
            elif a > b:
                b_max += b
                right += 1
            else:
                a_pre = a_max
                b_pre = b_max
                a_max = max(a_pre, b_pre) + a
                b_max = max(a_pre, b_pre) + b
                left += 1
                right += 1
        while(left < len(nums1)):
            a_max += nums1[left]
            left += 1
        while(right < len(nums2)):
            b_max += nums2[right]
            right += 1
        return max(a_max, b_max) % (10**9+7)
