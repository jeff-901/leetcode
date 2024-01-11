class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        ans = 0
        for idx, ele in enumerate(s):
            if ele == "(":
                stack.append(idx)
            elif ele == ")":
                stack.pop()
                if len(stack) > 0:
                    ans = max(ans, idx - stack[-1])
                else:
                    stack.append(idx)
        return ans