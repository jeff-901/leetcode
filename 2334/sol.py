class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        stack = []
        for idx, num in enumerate(nums):
            bar = threshold // num + 1
            earliest = idx
            if stack: 
                while stack and stack[-1][1] < bar:
                    earliest, _ = stack.pop()
            if stack:
                if idx >= stack[-1][1] + stack[-1][0] - 1:
                    return idx - stack[-1][0] + 1
                if earliest + bar < stack[-1][0] + stack[-1][1] - 1:
                    stack.append([earliest, bar])
            else:
                if idx - earliest + 1 >= bar:
                    return idx - earliest + 1
                stack.append([earliest, bar])
        return -1