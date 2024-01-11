class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1 = "".join([chr(c) for c in nums1])
        ans = 0
        cur = ""
        for num in nums2:
            cur += chr(num)
            if cur in s1:
                ans += 1
            else:
                cur = cur[1:]
        return ans