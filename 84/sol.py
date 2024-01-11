class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        for idx, h in enumerate(heights):
            earliest = idx
            while stack and h <= stack[-1][1]:
                ans = max(ans, stack[-1][1] * (idx - stack[-1][0]))
                earliest, _ = stack.pop()
            stack.append([earliest, h])
        idx = len(heights)
        while stack:
            ans = max(ans, stack[-1][1] * (idx - stack[-1][0]))
            stack.pop()
        return ans