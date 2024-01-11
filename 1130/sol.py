class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [float("inf")]
        res = 0
        for num in arr:
            while stack[-1] <= num:
                res += stack.pop() * min(num, stack[-1])
            stack.append(num)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res