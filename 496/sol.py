class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h = {}
        stack = []
        for ele in nums2:
            while(stack and stack[-1] < ele):
                h[stack.pop()] = ele
            stack.append(ele)
        while(stack):
            h[stack.pop()] = -1
        for i in range(len(nums1)):
            nums1[i] = h[nums1[i]]
        return nums1

